res = {
    "Rock": {"Rock": 0, "Paper": -1, "Scissors": 1},
    "Paper": {"Rock": 1, "Paper": 0, "Scissors": -1},
    "Scissors": {"Rock": -1, "Paper": 1, "Scissors": 0}
}

a = input()
b = input()
print(res[a][b])
