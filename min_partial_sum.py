"""
https://qiita.com/drken/items/a5e6fe22863b7992efdb#%E5%95%8F%E9%A1%8C-5%E6%9C%80%E5%B0%8F%E5%80%8B%E6%95%B0%E9%83%A8%E5%88%86%E5%92%8C%E5%95%8F%E9%A1%8C
問題 5:　最小個数部分和問題　
n 個の正の整数 a[0],a[1],…,a[n−1]a[0],a[1],…,a[n−1] と正の整数 A が与えられる。
これらの整数から何個かの整数を選んで総和が A にする方法をすべて考えた時、選ぶ整数の個数の最小値を求めよ。
A にすることができない場合は -1 と出力せよ。
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
    a = list(map(int, input().split()))
    A = int(input())
    dp = min_partial_sum(n, a, A)
    if dp < INF:
        print(dp)
    else:
        print(-1)
