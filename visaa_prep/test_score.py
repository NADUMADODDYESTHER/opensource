N, X, Y = map(int, input().split())
v = 0
if (Y - N * v) % (X - v) == 0 and (Y - N * v) // (X - v) >= 0:
    print("YES")
else:
    print("NO")
