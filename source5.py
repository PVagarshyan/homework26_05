arr = [i for i in range(1, 10001) if sum([j for j in range(1, i) if i%j == 0]) == i]
print(arr)
