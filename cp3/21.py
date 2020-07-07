import re

def load(file):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()

article = load(r"C:\Users\stutk\OneDrive\Desktop\nlp_100\cp3\british_article.txt")
s = re.findall(r"[[]]", article)