"""
당구 시뮬레이션 (Pygame) — GIF처럼 창에서 바로 조작/재생
- 마우스로 수구 위에서 드래그: 드래그 길이=힘, 방향=샷 방향 → 마우스 버튼을 떼면 샷 실행
- 키보드: [R] 리셋, [C] 수구 배치 모드, [O] 목적구 배치 모드, [ESC] 종료
- (배치 모드에서) 마우스 클릭으로 해당 공을 원하는 위치로 옮길 수 있음
- 포켓 6개(모서리 4 + 중앙 2), 간단 물리(마찰, 쿠션 반사, 공-공 충돌) 포함

실행 방법
    pip install pygame
    python billiards_pygame.py

참고/제한
- 실제 물리 완벽 재현 X(스핀/회전손실/쿠션 모따기 등 미반영). 연습/데모용.
- 단위: 테이블은 9ft 규격(2.84m x 1.42m)을 픽셀로 스케일링.
"""
from __future__ import annotations
import math
import pygame
from dataclasses import dataclass, field
from typing import List, Tuple

# === 기본 설정 ===
WIN_W, WIN_H = 1200, 600
FPS = 120

TABLE_W_M, TABLE_H_M = 2.84, 1.42  # 9ft 기준(m)
BALL_R_M = 0.028575                 # 57.15mm/2
POCKET_R_M = 0.080                  # 간이 포켓 반경(m)
FRICTION = 0.25                     # 속도 감쇠 계수(초당)
ELASTIC = 0.98                      # 쿠션 반사 탄성
STOP_EPS = 0.02                     # m/s 이하 정지 간주
DT = 1.0 / FPS                      # 시뮬 dt

SCALE = min(WIN_W / TABLE_W_M, WIN_H / TABLE_H_M)
OFF_X = (WIN_W - TABLE_W_M * SCALE) / 2
OFF_Y = (WIN_H - TABLE_H_M * SCALE) / 2

# 색상
GREEN = (13, 90, 55)
DARK_GREEN = (5, 60, 35)
WHITE = (235, 235, 235)
YELLOW = (250, 215, 50)
RED = (220, 70, 70)
BLACK = (20,20,20)
GRAY = (200, 200, 200)
BLUE = (70, 140, 220)

@dataclass
class Vec2:
    x: float
    y: float
    def __add__(self, o: 'Vec2') -> 'Vec2': return Vec2(self.x+o.x, self.y+o.y)
    def __sub__(self, o: 'Vec2') -> 'Vec2': return Vec2(self.x-o.x, self.y-o.y)
    def __mul__(self, k: float) -> 'Vec2': return Vec2(self.x*k, self.y*k)
    __rmul__ = __mul__
    def __truediv__(self, k: float) -> 'Vec2': return Vec2(self.x/k, self.y/k)
    def dot(self, o: 'Vec2') -> float: return self.x*o.x + self.y*o.y
    def norm(self) -> float: return math.hypot(self.x, self.y)
    def unit(self) -> 'Vec2':
        n = self.norm()
        return self / n if n > 1e-9 else Vec2(0.0, 0.0)
    def tuple(self) -> Tuple[float,float]: return (self.x, self.y)

@dataclass
class Ball:
    pos: Vec2
    vel: Vec2 = field(default_factory=lambda: Vec2(0.0, 0.0))
    r: float = BALL_R_M
    mass: float = 0.17
    color: Tuple[int,int,int] = WHITE
    pocketed: bool = False

    def apply_impulse(self, J: Vec2):
        self.vel = self.vel + (J / self.mass)

# 유틸: m<->px 변환

def m2p(v: Vec2) -> Tuple[int,int]:
    return int(OFF_X + v.x*SCALE), int(OFF_Y + v.y*SCALE)

def p2m(px: Tuple[int,int]) -> Vec2:
    x = (px[0]-OFF_X)/SCALE
    y = (px[1]-OFF_Y)/SCALE
    return Vec2(x,y)

# 테이블 경계 내부 여부

def inside_table(v: Vec2) -> bool:
    return 0+BALL_R_M <= v.x <= TABLE_W_M-BALL_R_M and 0+BALL_R_M <= v.y <= TABLE_H_M-BALL_R_M

# 포켓 좌표(m)

def pockets_m() -> List[Vec2]:
    return [
        Vec2(0,0), Vec2(TABLE_W_M/2,0), Vec2(TABLE_W_M,0),
        Vec2(0,TABLE_H_M), Vec2(TABLE_W_M/2,TABLE_H_M), Vec2(TABLE_W_M,TABLE_H_M)
    ]

# 선분-원 교차(중심선 기준, 반지름 여유)

def segment_hits_circle(A: Vec2, B: Vec2, C: Vec2, r: float) -> bool:
    AB = B - A
    AC = C - A
    ab2 = AB.dot(AB)
    if ab2 < 1e-12:
        return AC.norm() <= r
    t = max(0.0, min(1.0, AC.dot(AB)/ab2))
    H = A + AB*t
    return (H - C).norm() <= r

# 물리: 쿠션 반사

def reflect_cushion(ball: Ball):
    x, y = ball.pos.x, ball.pos.y
    r = ball.r
    if x - r < 0 and ball.vel.x < 0:
        ball.pos.x = r
        ball.vel.x *= -ELASTIC
    if x + r > TABLE_W_M and ball.vel.x > 0:
        ball.pos.x = TABLE_W_M - r
        ball.vel.x *= -ELASTIC
    if y - r < 0 and ball.vel.y < 0:
        ball.pos.y = r
        ball.vel.y *= -ELASTIC
    if y + r > TABLE_H_M and ball.vel.y > 0:
        ball.pos.y = TABLE_H_M - r
        ball.vel.y *= -ELASTIC

# 물리: 공-공 충돌(탄성, 정상 성분)

def collide(a: Ball, b: Ball):
    delta = b.pos - a.pos
    dist = delta.norm()
    min_d = a.r + b.r
    if dist < min_d and dist > 1e-9:
        # 위치 분리(겹침 해소)
        overlap = (min_d - dist)
        push = delta.unit() * (overlap/2)
        a.pos = a.pos - push
        b.pos = b.pos + push
        # 속도 교환(정상 성분)
        nrm = (b.pos - a.pos).unit()
        rel = b.vel - a.vel
        vn = rel.dot(nrm)
        if vn < 0:
            m1, m2 = a.mass, b.mass
            J = (-(1+1.0) * vn) / (1/m1 + 1/m2)
            imp = nrm * J
            a.apply_impulse(-imp)
            b.apply_impulse(imp)

# 포켓 판정

def pocket_check(ball: Ball):
    if ball.pocketed:
        return
    for p in pockets_m():
        if (ball.pos - p).norm() <= POCKET_R_M:
            ball.pocketed = True
            ball.vel = Vec2(0,0)
            return

# 한 스텝 업데이트

def step(balls: List[Ball]):
    # 충돌
    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            a, b = balls[i], balls[j]
            if a.pocketed or b.pocketed: continue
            collide(a,b)
    # 이동/마찰/쿠션/포켓
    for b in balls:
        if b.pocketed: continue
        b.pos = b.pos + b.vel * DT
        # 마찰 감쇠
        b.vel = b.vel * max(0.0, 1.0 - FRICTION*DT)
        if b.vel.norm() < STOP_EPS:
            b.vel = Vec2(0,0)
        reflect_cushion(b)
        pocket_check(b)

# 드로잉

def draw_table(screen):
    screen.fill(BLACK)
    # 천
    rect = pygame.Rect(OFF_X, OFF_Y, TABLE_W_M*SCALE, TABLE_H_M*SCALE)
    pygame.draw.rect(screen, GREEN, rect, border_radius=18)
    # 포켓
    for p in pockets_m():
        pygame.draw.circle(screen, BLACK, m2p(p), int(POCKET_R_M*SCALE))
        pygame.draw.circle(screen, DARK_GREEN, m2p(p), int(POCKET_R_M*SCALE), 3)


def draw_balls(screen, balls: List[Ball]):
    for b in balls:
        if b.pocketed: continue
        pygame.draw.circle(screen, b.color, m2p(b.pos), int(b.r*SCALE))
        pygame.draw.circle(screen, BLACK, m2p(b.pos), int(b.r*SCALE), 2)


def draw_ui(screen, font, msg_lines: List[str]):
    x, y = 12, 10
    for s in msg_lines:
        img = font.render(s, True, (240,240,240))
        screen.blit(img, (x,y))
        y += img.get_height() + 4


def any_moving(balls: List[Ball]) -> bool:
    return any((not b.pocketed) and (b.vel.norm() > 0) for b in balls)

# 메인

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIN_W, WIN_H))
    pygame.display.set_caption("Billiards Simulation — Drag to Shoot")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("pretendard, nanumgothic, malgungothic, arial", 18)

    # 초기 배치
    cue = Ball(pos=Vec2(0.5, TABLE_H_M*0.5), color=WHITE)
    obj = Ball(pos=Vec2(1.6, TABLE_H_M*0.5), color=YELLOW)
    balls = [cue, obj]

    placing = None  # 'cue' or 'obj'
    dragging = False
    drag_start = None
    aim_vec = Vec2(0,0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:  # 리셋
                    for b in balls:
                        b.pocketed = False
                        b.vel = Vec2(0,0)
                    cue.pos = Vec2(0.5, TABLE_H_M*0.5)
                    obj.pos = Vec2(1.6, TABLE_H_M*0.5)
                elif event.key == pygame.K_c:  # 수구 배치 모드
                    placing = 'cue'
                elif event.key == pygame.K_o:  # 목적구 배치 모드
                    placing = 'obj'
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 좌클릭
                    mpos = p2m(pygame.mouse.get_pos())
                    if placing:
                        # 배치 모드: 클릭 위치로 옮기기 (테이블 내부 & 겹침 방지)
                        if inside_table(mpos):
                            target = cue if placing=='cue' else obj
                            other = obj if placing=='cue' else cue
                            # 겹치지 않게 살짝 조정
                            if (mpos - other.pos).norm() < target.r + other.r + 0.005:
                                # 너무 가까우면 무시
                                pass
                            else:
                                target.pos = mpos
                                target.pocketed = False
                                target.vel = Vec2(0,0)
                        placing = None
                    else:
                        # 드래그 샷: 수구 위에서만 시작
                        if not any_moving(balls) and not cue.pocketed:
                            if (mpos - cue.pos).norm() <= cue.r*1.3:
                                dragging = True
                                drag_start = mpos
                                aim_vec = Vec2(0,0)
                elif event.button == 3:
                    # 우클릭: 배치 모드 토글 끄기
                    placing = None
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and dragging:
                    dragging = False
                    # 샷 실행
                    if aim_vec.norm() > 0.005:
                        dirv = aim_vec.unit()
                        # 드래그 길이(최대 제한)
                        L = min(aim_vec.norm(), 0.8)  # m 단위로 최대치 제한
                        # 힘->초기 속도 스케일(적당히 튜닝)
                        v0 = 4.5 * L / DT * 0.02  # 상대 스케일
                        cue.vel = dirv * v0
            elif event.type == pygame.MOUSEMOTION and dragging:
                mpos = p2m(pygame.mouse.get_pos())
                # 드래그는 "수구에서 반대 방향으로 끌어당기는" 제스처
                aim_vec = (drag_start - mpos)

        # 물리 업데이트
        if any_moving(balls):
            step(balls)

        # 그리기
        draw_table(screen)
        draw_balls(screen, balls)

        # 조준선/게이지 표시
        hud = [
            "마우스: 수구에서 드래그→샷 | [C] 수구 배치, [O] 목적구 배치, [R] 리셋, [ESC] 종료",
        ]
        if placing:
            hud.append(f"배치 모드: {'수구' if placing=='cue' else '목적구'} — 테이블 안을 클릭해서 이동")
        if dragging and not cue.pocketed:
            # 조준선 (드래그 시작점=수구 위치 근처, aim_vec 방향으로)
            base = drag_start
            dirv = aim_vec.unit()
            L = aim_vec.norm()
            # 수구에서 반대방향으로 선
            A = cue.pos
            B = cue.pos + dirv * (min(L, 0.8))
            pygame.draw.line(screen, BLUE, m2p(A), m2p(B), 3)
            # 힘 게이지 바
            hud.append(f"힘(상대): {min(L,0.8)/0.8*100:.0f}%  / 길이≈{L:.3f} m")
        # 텍스트
        draw_ui(screen, font, hud)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
