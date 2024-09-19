a = 0
for i in range(6): a += input() == 'W'

res = 0
if a < 1: res = -1
elif a < 3: res = 3
elif a < 5: res = 2
else: res = 1
print(res)