import sys
sys.stdin = open('21941.txt')




T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))


    current = [0] * N # 현재 배열

    cnt = 0

    for i in range(N):
        if current[i] != arr[i]: # 현재랑 다르면!
            cnt +=1

            for j in range(i, N, i+1):  # 카운트 1 한거 이렇게 바꾸기
                if current[j] == 0:      # m번 배수만큼 카운트 하는데 범위가 i +1 왜??
                    current[j] = 1         # 인덱스는 0 부터 시작해서  2 = 3 번째 친구 -> 2(3) 5(6) 8(9) 이 3의 배수임  ;.;.;
                else:
                    current[j] = 0

    print(f"#{tc} {cnt}")