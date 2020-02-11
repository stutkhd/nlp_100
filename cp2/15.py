def tail_n(n):
    with open("hightemp.txt", encoding="utf-8") as f:
        lines = f.read().splitlines()
        for i in range(1, n+1):
            print(lines[-i])
tail_n(24)