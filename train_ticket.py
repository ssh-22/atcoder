# C - Train Ticket
# https://atcoder.jp/contests/abc079/tasks/abc079_c
S = input()
n = len(S) - 1
TOTAL = 7
for i in range(1 << n):
    x = S[0]
    for j in range(n):
        if i & 1 << j:
            x += "+"
        else:
            x += "-"
        x += S[j + 1]
    if eval(x) == TOTAL:
        print(f"{x}={TOTAL}")
        break
    else:
        continue
    break
