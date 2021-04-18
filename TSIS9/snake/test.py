list = [1, 2, 3]
print(*list)
list.insert(0, 0)
print(*list)
for i in range(len(list) - 1, 0, -1):
    list[i] = list[i-1]
print(*list)