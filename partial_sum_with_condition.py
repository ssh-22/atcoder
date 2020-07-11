"""
問題 6:　K個以内部分和問題
n 個の正の整数 a[0],a[1],…,a[n−1]a[0],a[1],…,a[n−1] と正の整数 A が与えられる。
これらの整数から K 個以内の整数を選んで総和が A になるようにすることが可能か判定せよ。
可能ならば "YES" と出力し、不可能ならば "NO" と出力せよ。
"""
from typing import List, Union

INF = float("inf")


def min_partial_sum(n: int, a: List[int], A: int) -> Union[int, float]:
    dp = [[INF for i in range(A + 1)] for j in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(A + 1):
            if j >= a[i]:
                dp[i + 1][j] = min(dp[i][j - a[i]] + 1, dp[i][j])
            else:
                dp[i + 1][j] = dp[i][j]
    return dp[n][A]


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    a = [int(i) for i in input().split()]
    A = int(input())
    dp = min_partial_sum(n, a, A)
    if dp <= k:
        print("YES")
    else:
        print("NO")
