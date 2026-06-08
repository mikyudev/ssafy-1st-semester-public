t = int(input()) # 테스트 케이스 개수 지정 

for case in range(1,t+1):  # 테스트 케이스 개수 범위 
    numbers = list(map(int,input().split())) # 넘버를 입력받고 , 띄워쓰기 기준 문자열을 리스트로 만든 다음, int를 map으로 전부 적용 한 다음 list로 출력  

    
    odd_sum = 0  # 합계는 0으로 초기화 시켜놓고 

    for n in numbers:  #넘버에 숫자를 도는데
        if n % 2 == 1: # n 이 홀수면 
            odd_sum += n # 합계에 더해라 

    print(f"#{case} {odd_sum}") #출력 
