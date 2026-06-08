score = {'bogeom' : 89,
         'sangho' : 100,
         'IU' : 78,
         'sori' : 76,
         'hejun' : 85
         }

# print(score.items())
# print(score.values())

max_v = max(score.values())
for key, value in score.items():
    if value == max_v:
        result = key

print(result)




max_v = 0
best = ""

for key, value in score.items():
    if value > max_v:
        max_v = value # 최댓값 갱신 코드   ★★★★★암기필요 ★★★★★
        best = key  #  최댓값 갱신 되었을때 학생 

print(best)