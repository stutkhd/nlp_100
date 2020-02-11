import re
with open("hightemp.txt", encoding="utf-8") as f:
    lst = [line.split() for line in f.readlines()]

with open("col1.txt", "w", encoding="utf-8") as f:
    for line in lst:
        print(line[0], file=f)

with open("col2.txt", "w", encoding="utf-8") as f:
    for line in lst:
        print(line[1], file=f)