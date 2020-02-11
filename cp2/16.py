def split_files(n):
    with open("hightemp.txt", encoding="utf-8") as f:
        for i, line in enumerate(f.readlines()):
            with open("lines/{}_line".format(i+1), "w", encoding="utf-8") as file:
                print(line, file=file)
            if i+1==n:
                break
split_files(24)