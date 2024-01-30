# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    amt = {}
    for i in seq:
        if i in amt.keys():
            amt[i] += 1
        else:
            amt[i] = 1
    for n, a in amt.items():
        if a%2 == 1:
            return n