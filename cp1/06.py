def n_gram(n, text):
    word_lst = text.split()
    chr_lst = "".join(word_lst)
    r_ch = [chr_lst[i:i+n] for i in range(len(chr_lst)-1)]
    return r_ch

a = "paraparaparadise"
b = "paragraph"

X = n_gram(2, a)
Y = n_gram(2, b)

print("和集合:",list(set(X+Y)))

inter_set = [i for i in X if i in Y]
print("積集合:",inter_set)

dif_set = [i for i in X if i not in Y]
print("差集合:",dif_set)
