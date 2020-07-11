# C - たくさんの数式
# https://atcoder.jp/contests/arc061/tasks/arc061_a
S = input()
n = len(S)
ans = 0
# 計算量: O(2**n*n)
for i in range(1 << n - 1):
    # 0からn-1番目までの数のうち、何番目の後にj番目に+を挿入するか
    x = S[0]
    for j in range(n - 1):
        if i & 1 << j:
            # +をjとj+1の間に挿入する
            x += '+'
        x += S[j + 1]
    ans += sum(map(int, x.split('+')))
print(ans)
