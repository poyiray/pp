# Source: https://usaco.guide/general/io

num = int(input())
a = 0
b = 1
res = 0
for i in range(1, num):
    res = a + b
    a = b
    b = res
print(res)