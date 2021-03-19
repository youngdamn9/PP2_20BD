res, cnt = [], {}
while True:
    s = input().split()
    for i in range(len(s)):
        if i == '.': break
    for i in s:
        if i in cnt.keys(): cnt[i] += 1
        else: cnt[i] = 1
#for i, j in cnt.items():
#    res.append((j, i))
print(sorted(cnt))