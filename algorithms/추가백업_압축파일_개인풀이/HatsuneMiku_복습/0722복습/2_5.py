my_set1 = {1, 2, 3, 4, 5, 6}
my_set2 = {4, 5, 6, 7, 8, 9}

print(*my_set1 | my_set2)
print(*my_set1 & my_set2)
print(*my_set1 - my_set2)