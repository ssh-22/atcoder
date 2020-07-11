"""
問題 1:　最大和問題
n 個の整数 a[0],a[1],…,a[n−1]a[0],a[1],…,a[n−1] が与えられる。
これらの整数から何個かの整数を選んで総和をとったときの、総和の最大値を求めよ。
また、何も選ばない場合の総和は 0 であるものとする。
"""


def max_sum(n, a) -> int:
    dp = [0 for i in range(n + 1)]
    for i in range(n):
        if a[i] >= 0:
            dp[i + 1] = dp[i] + a[i]
        else:
            dp[i + 1] = dp[i]
    return max(dp)


if __name__ == "__main__":
    n = int(input())
    a = [int(i) for i in input().split()]
    print(max_sum(n, a))
