import math
a = 0
for i in range(3):  
    a += len(input())

total = math.ceil(a / 12)
print(f"{total * 12}\n{a - total * 12}\n{total * 14.95}")
