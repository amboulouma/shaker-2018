p, L, g = map(int, input().split())
count = 0
Y = {}
for i in range(p+1):
    for j in range(L+1):
        if i*i + j + i*j - g == 0:
            count += 1
print(count)
