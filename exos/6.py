



def my_filter(func, lst : list) :
    for i in lst :
        if func(i) :
            lst.remove(i)


mots = ["hi", "hello", "world", "ok", "python"]
my_filter(lambda x: len(x) < 3, mots)
print(mots)