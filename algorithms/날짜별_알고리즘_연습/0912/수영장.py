import sys
sys.stdin = open("swim.txt")

# 1. 종료조건 : 12월을 모두 고려했을 때
# 2. 가지의 수 = 4 개

# 종료조건 12월 모두 고려한 경우
# 가지의 수 4개 , 1일, 1달, 3달, 1년
def recur(month, total_cost):
    global min_answer
    if month > 12:
        # Todo: 최소값 갱신
        min_answer= min(min_answer, total_cost)
        return

    # 1일권으로 다 사는경우
    recur(month + 1, total_cost + days[month] * day)
    # 1달권으로 다 사는경우
    recur(month + 1, total_cost + month1)
    # 3달권으로 다 사는경우
    recur(month + 3, total_cost + month3)
    # 1년권으로 다 사는경우
    recur(month + 12, total_cost + year)

T = int(input())
for tc in range(1, T+1):
    #  이용권 가격들 ( 1일, 1달, 3달, 1년)
    day, month1, month3, year = map(int, input().split())
    # 12개월 이용 계획 (1부터 씀)
    days = [0] + list(map(int, input().split()))
    min_answer = 31 * 12* 3000 # 최대금액 31일 12개월 1일권최대 가격
    recur(1, 0) # 1월부터 시작

    print(f"#{tc} {min_answer}")








T = int(input())
for tc in range(1, T+1):
    #  이용권 가격들 ( 1일, 1달, 3달, 1년)
    day, month1, month3, year = map(int, input().split())
    # 12개월 이용 계획 (1부터 씀)
    days = [0] + list(map(int, input().split()))
    min_answer = 31 * 12* 3000 # 최대금액 31일 12개월 1일권최대 가격
    recur(1, 0) # 1월부터 시작

    print(f"#{tc} {min_answer}")






















