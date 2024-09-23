# Source: https://usaco.guide/general/io

num = int(input())
f = False
for i in range(2, num):
    if(num % i == 0):
        f = 1
        break
if(f): print("no")
else: print("yes")