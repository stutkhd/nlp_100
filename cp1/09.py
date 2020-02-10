import random
def typoglycemia(text):
    s_lst = text.split()
    r = []
    for word in s_lst:
        if len(word) <= 4:
            r.append(word)
        else:
            rand_list = "".join(random.sample(word[1:-1], len(word)-2))
            r.append(word[0]+rand_list+word[-1])
    return r
print(*typoglycemia("""I couldn't believe that I could actually
                    understand what I was reading : the phenomenal 
                    power of the human mind ."""))