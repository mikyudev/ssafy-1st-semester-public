char = "Hello World"

print(char[0:1:1], end =' ')
print(char[-1:-2:-1])


print(char[0::2]) # = [0:12:2]

print(char[-1::-1]) # = [-1:-12:-1]

#////////////////// 밑에가 깔끔 정답 /////////////////////

# length = len(char)
# print(length)  참고 

print(char[0], char[-1])
print(char[::2])
print(char[::-1])
