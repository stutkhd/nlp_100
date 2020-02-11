with open("col1.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()
print(set(lines))