import json
import gzip

def extract(title):
    #rt:テキストファイルを指す, rだとバイナリになる
    with gzip.open(r"C:\Users\stutk\OneDrive\Desktop\nlp_100\cp3\jawiki-country.json.gz", "rt", encoding="utf-8") as f:
        for line in f:
            jsn = json.loads(line)
            if jsn["title"] == title:
                return jsn["text"]
    return ""

def main():
    article = extract("イギリス")
    with open("british_article.txt", "w", encoding="utf-8") as f:
        f.write(article)
if __name__ == "__main__":
    main()