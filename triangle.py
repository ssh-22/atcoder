n = int(input())
a = list(map(int, input().split()))

ans = 0

for i in a:
    for j in a:
        for k in a:
            if i != j and i != k and j != k:
                total = i + j + k
                max_len = max(i, j, k)
                rest = total - max_len
                if max_len < rest:
                    ans = max(ans, total)
print(ans)
