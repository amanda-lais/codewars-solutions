# Your goal in this kata is to implement a 
# difference function, which subtracts one 
# list from another and returns the result.

def array_diff(a, b):
    c = []
    for i in a:
        if i in b:
            continue
        else:
            c.append(i)
    return c