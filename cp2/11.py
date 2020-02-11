import re

with open("hightemp.txt", encoding="utf-8") as f:
    line = re.sub("\t", " ", f.read())
    print(line)

