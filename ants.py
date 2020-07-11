l, n = [int(input()) for i in range(2)]
x = list(map(int, input().split()))
x_min = max([min(abs(l - i), abs(i - 0)) for i in x])
x_max = max([max(abs(l - i), abs(i - 0)) for i in x])
print(x_min)
print(x_max)
