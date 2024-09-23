# Source: https://usaco.guide/general/io

cnt = 1;
res = 1;
num = int(input())
while cnt <= num:
    res *= cnt
    cnt += 1
print(res)

res = 1;
num = int(input())
for i in range(1, num + 1):
    res *= i
print(res)