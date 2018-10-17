L, N = map(int, input().split())
P = list(map(int, input().split()))
H = list(map(int, input().split()))
l = P[-1]
pont = list(range(1, L+1))


def fill_pont(p, h, pont, l=L):
    if h is not 0:
        for i in range(h+1):
            pont[max(0, p-1-i)] = 0
            pont[min(p-1+i, l-1)] = 0
    return pont


for p in P:
    for h in H:
        if(any(pont) is False):
            break
        pont = fill_pont(p, h, pont=pont)


if any(pont) is False:
    print("YES")
else:
    print("NO")
