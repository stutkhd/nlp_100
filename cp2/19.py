from collections import Counter
with open("col1.txt", encoding="utf-8") as f:
    lst = f.read().splitlines()
    c = dict(Counter(lst))
    r = sorted(c.items(), key=lambda x:x[1], reverse=True)
    for k in r:
        print(k[0])