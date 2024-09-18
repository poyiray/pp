first = input()
last = input()
birth = int(input())
print(f"Hello {first} {last}.\nYou are {2024 - birth} years old.\nYou are {('old enough' if 2024 - birth >= 18 else 'not old enough')} to drink")