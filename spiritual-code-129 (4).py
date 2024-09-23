# Source: https://usaco.guide/general/io

num = int(input())
ans = 0
for i in range(1,num + 1):
    res = 0
    for j in range(1, i):
        if i % j == 0: res += j
    if res == i:
        print(f"{res} is a perfect number")
        ans += res
print(ans)