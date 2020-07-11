h, w, k = map(int, input().split())
c = [input() for i in range(h)]
ans = 0  # 何通りあるか
for row in range(1 << h):  # h行の選び方は2のh乗通り
    for col in range(1 << w):  # w行の選び方は2のw乗通り
        cnt = 0  # 黒いマスの数
        for i in range(h):
            for j in range(w):
                if row >> i & 1:
                    # h行目を選ぶ場合、該当行は黒ではないのでスキップ
                    continue
                if col >> j & 1:
                    # i列目を選ぶ場合、該当列は黒ではないのでスキップ
                    continue
                if c[i][j] == "#":
                    # 黒の数を数える
                    cnt += 1
        ans += cnt == k  # 黒の数がk個残る選び方が何通りあるか数える
        # if cnt == k:
        #     # 黒の数がk個残る選び方が何通りあるか数える
        #     ans += 1
print(ans)
