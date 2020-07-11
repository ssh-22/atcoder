"""
https://qiita.com/drken/items/a5e6fe22863b7992efdb#%E5%95%8F%E9%A1%8C-4%E9%83%A8%E5%88%86%E5%92%8C%E6%95%B0%E3%81%88%E4%B8%8A%E3%81%92%E5%95%8F%E9%A1%8C
問題 4:　部分和数え上げ問題
n 個の正の整数 a[0],a[1],…,a[n−1]a[0],a[1],…,a[n−1] と正の整数 A が与えられる。
これらの整数から何個かの整数を選んで総和が A になるようにする方法が何通りあるかを求めよ。
ただし、答えがとても大きくなる可能性があるので、1,000,000,009 で割った余りで出力せよ。
"""
from typing import List


def count_partial_sum(n: int, a: List[int], A: int) -> int:
    dp = [[0 for i in range(A + 1)] for j in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(A + 1):
            if j >= a[i]:
                dp[i + 1][j] += dp[i][j - a[i]] + dp[i][j]
                dp[i + 1][j] %= MOD
            else:
                dp[i + 1][j] += dp[i][j]
                dp[i + 1][j] %= MOD
    return dp[n][A]


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    A = int(input())
    MOD = 1000000009
    print(count_partial_sum(n, a, A))
