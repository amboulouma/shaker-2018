L = int(input())
N = int(input())
previous_str = list(str(L))
for _ in range(N):
    str_ = list(str(L))
    for c in set(previous_str):
        str_ += list(str(previous_str.count(c)))
        print(previous_str.count(c))
    previous_str = "".join(str_)
    max_ = max(previous_str[2:])
    index_max_sub = previous_str.index(max_)
    print(index_max_sub)
    previous_str = list(previous_str)
    del previous_str[1 + index_max_sub]
    previous_str += [max_]

    print(previous_str)
    print(str_)
print("".join(str_))
