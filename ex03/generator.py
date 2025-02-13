import random


def generator(text, sep=" ", option=None):
    if not ((isinstance(text, str) and text) or (option and option not in ["ordered", "shuffle", "unique"])):
        return print("ERROR")
    lst = text.split(sep)
    new_lst = []
    if (option == "ordered"):
        new_lst = lst
        new_lst.sort()
    elif (option == "shuffle"):
        while len(lst) > 0:
            new_lst.append(lst.pop(random.randint(0, len(lst) - 1)))
    elif (option == "unique"):
        for a in lst:
            if (new_lst.count(a) == 0):
                new_lst.append(a)
    else:
        new_lst = lst
    for a in new_lst:
        yield a
    

