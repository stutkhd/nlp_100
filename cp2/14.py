def head_n(n):
    with open("hightemp.txt", encoding="utf-8") as f:
        lines = f.read().splitlines()
        for i in range(n):
            print(lines[i])
head_n(24)