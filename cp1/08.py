import re
def cipher(text):
    r = ""
    for i in text:
        if re.findall(r"[a-z]", i):
            r+="219-{}".format(ord(i))
        else:
            r+=i
    return r
print(cipher("あおrヴぃま"))
# あお219-114ヴぃま