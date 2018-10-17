Or, N = map(int, input().split())
max_ = 0
premier_nom_max = ""
nombre_perroquets = 0
for i in range(N):
    Nom, P, C = input().split()
    P = int(P)
    C = int(C)
    nombre_perroquets = (Or-C)//P
    if nombre_perroquets > max_:
        max_ = nombre_perroquets
        premier_nom_max = Nom

if max_ is 0:
    print("Impossible")
else:
    print(max_)
    print(premier_nom_max)
