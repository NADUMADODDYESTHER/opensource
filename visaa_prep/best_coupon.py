X = int(input())
y1 = X * 0.10
y2 = 100
if y1 > y2:
    final_amount = X - y1
else:
    final_amount = X -y2
print(int(final_amount))
