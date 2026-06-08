# ちょうほうけい　長方形　직사각형

# 1. 겹침(else) 2. 선겹칩 3. 점 겹침 4. 떨어짐


T = int(input())
for tc in range(1, T+1):
    ax1, ay1, ax2, ay2 = map(int, input().split())
    bx1, by1, bx2, by2 = map(int, input().split())

    world = [[0] * 1001 for _ in range(1001)]


