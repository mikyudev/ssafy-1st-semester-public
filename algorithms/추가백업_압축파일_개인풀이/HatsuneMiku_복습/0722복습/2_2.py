for i in range(0,5):
    print(i, '', end='')

print() 

for i in range(3,13):
    if i%3 == 0:
        print(i, '', end='')

print()

for i in range(20, -11,-1):
    if i%5 ==0:
        print(i, '', end ='')


# range(star, end, step)
# step이 양수 
# start부터 end -1 까지 step만큼 증가 
# step이 음수 
# start 부터 end +1까지 step 만큼 감소 
# 핵심은 항상 수직선 상에서 end를 포함하지 않는다 
# 예) n번 반복하는 반복문을 만들고 싶다
# for i in range(n):