X , Y, Z = map(int, input().split())
if Y >= Z:
    print(0)
else:
    result = (Z - Y) // X
    print(result)
