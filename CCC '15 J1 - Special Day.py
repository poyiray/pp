a = int(input())
b = int(input())

res = ""
if(a < 2): res = "Before"
elif(a > 2): res = "After"
else: 
    if(b < 18): res = "Before"
    elif(b > 18): res = "After"
    else: res = "Special"
print(res)