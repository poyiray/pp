# Source: https://usaco.guide/general/io

res = ''
x = ''
while x != 'X':
    x = input()
    if len(res) < len(x): res = x
print(res)