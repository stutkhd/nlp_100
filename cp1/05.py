def n_gram(n, text):
    word_lst = text.split()
    chr_lst = "".join(word_lst)

    r_ch = [chr_lst[i:i+n] for i in range(len(chr_lst)-1)]
    r_wd = [word_lst[i:i+n]for i in range(len(word_lst)-1)]

    print(f"単語{n}-gram:",r_wd)
    print(f"文字{n}-gram:",r_ch)

n_gram(2, "I am an NLPer")