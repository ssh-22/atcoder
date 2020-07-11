"""
問題 2:　ナップサック問題
n 個の品物があり、i 番目の品物のそれぞれ重さと価値がweight[i],value[i]weight[i],value[i] となっている (i=0,1,...,n−1i=0,1,...,n−1)。
これらの品物から重さの総和が W を超えないように選んだときの、価値の総和の最大値を求めよ。
"""
from typing import List


def knapsack(n: int, weight: List[int], value: List[int], W: int):
    dp = [[0 for i in range(W + 1)] for j in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for w in range(W + 1):
            if w >= weight[i]:
                dp[i + 1][w] = max(dp[i][w - weight[i]] + value[i], dp[i][w])
            else:
                dp[i + 1][w] = dp[i][w]
    return dp[n][W]


if __name__ == "__main__":
    n = int(input())
    wv = [map(int, input().split()) for _ in range(n)]
    w, v = map(list, zip(*wv))
    W = int(input())
    print(knapsack(n, w, v, W))
