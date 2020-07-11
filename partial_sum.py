n = int(input())
a = list(map(int, input().split()))
k = int(input())


def dfs(i: int, total: int) -> bool:
    """iまででtotalを作って、残りi以降を調べる
    """
    # print(f"{i=}, {total=}")
    if i == n:
        # n個決め終わったら、今までの和totalがkと等しいかを返す
        return total == k
    if dfs(i + 1, total):
        # a[i]を使わない場合
        return True
    if dfs(i + 1, total + a[i]):
        # a[i]を使う場合
        return True
    # kが作れない時、falseを返す
    return False


if dfs(0, 0):
    print("Yes")
else:
    print("No")
