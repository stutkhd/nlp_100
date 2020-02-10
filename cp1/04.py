sentence = """Hi He Lied Because Boron
 Could Not Oxidize Fluorine.
  New Nations Might Also Sign 
  Peace Security Clause. Arthur
   King Can."""

lst = sentence[:-1].split()
st = [1, 5, 6, 7, 8, 9, 15, 16, 19]

dic = {}
for i,word in enumerate(lst):
    key = lst[i]
    if i+1 in st:
        dic[i+1] = key[0]
    else:
        dic[i+1] = key[:2]

print(dic)