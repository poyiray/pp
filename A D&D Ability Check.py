from random import randrange

a = int(input())
b = randrange(1,21)
print(("yes" if b >= a else "no") + "\n" + str(b))