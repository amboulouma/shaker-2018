S = input().split()
a_pirate = ['a', 'e', 'i', 'o', 'u', 'y', 'b', 'c', 'd', 'f', 'g', 'h',
            'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
count = 0
for c in S:
    if c not in a_pirate:
        count += 1
print(count)

def in_order(a, s):
    return s[a] == a_pirate[a]
