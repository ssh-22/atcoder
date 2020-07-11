n, m = [int(input()) for i in range(2)]
k = list(map(int, input().split()))

bool_flag = False

for a in k:
    for b in k:
        for c in k:
            for d in k:
                if a + b + c + d == m:
                    bool_flag = True
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break

if bool_flag:
    print("Yes")
elif not bool_flag:
    print("No")
