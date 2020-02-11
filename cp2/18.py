with open("hightemp.txt", encoding="utf-8") as f:
    lst = [line.split() for line in f.readlines()]
    lst.sort(key=lambda x:x[2],reverse=True) 
    for line in lst:
        print(line)