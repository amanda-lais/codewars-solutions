def comp(a, b):
    if a == None or b == None:
        return False
    c = []
    for i in a:
        c.append(i*i)
    for i in b:
        if i in c:
            c.remove(i)
        else:
            return False
    return True