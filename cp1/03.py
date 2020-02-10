sentence = """Now I need a drink, 
            alcoholic of course, 
            after the heavy lectures 
            involving quantum mechanics."""

lst = sentence[:-1].split()

r = [len(word) for word in lst]
r.append(len(sentence[-1]))
print(r)    