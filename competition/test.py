L = [1, 3, 10]

def fill_pont(p, h, pont=list(range(1, L[-1]+1)), l=L[-1]):
    for i in range(h+1):
        pont[max(0, p-1-i)] = 0
        pont[min(p-1+i, l-1)] = 0
    return pont

pont = fill_pont(3, 2)
pont = fill_pont(10, 4, pont=pont)

print(any(pont))
