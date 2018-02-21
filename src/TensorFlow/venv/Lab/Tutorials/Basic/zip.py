a = [11,22,33,44,55,66,77,88,99]
b = [1,2,3,4,5,6,7,8,9]
print(list(zip(a,b)))
print(*zip(range(0, len(a), 2), range(2, len(a)+1, 2)))


