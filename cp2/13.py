with open("col1.txt", encoding="utf-8") as col1:
    line1 = col1.read().splitlines()
with open("col2.txt", encoding="utf-8") as col2:
    line2 = col2.read().splitlines()

with open("col_merge.txt", "w", encoding="utf-8") as f:
    for i, j in zip(line1, line2):
        print(i+"\t"+j, file=f)