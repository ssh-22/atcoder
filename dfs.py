M = 2


def dfs(A):
    # 終端条件 --- 10 重ループまで回したら処理して打ち切り
    if len(A) == 3:
        print(A)
        return
    for v in range(M):
        A.append(v)
        dfs(A)
        A.pop()  # これが結構ポイント


dfs([])
