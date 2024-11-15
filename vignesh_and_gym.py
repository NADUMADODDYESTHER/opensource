X, Y, Z = map(int, input().split())
if X > Z:
    print(0)
else:
    if X + Y <= Z:
        print(2)
    else:
        print(1)
