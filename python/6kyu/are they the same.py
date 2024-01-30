# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) 
# that checks whether the two arrays have the "same" elements, 
# with the same multiplicities (the multiplicity of a member is the 
# number of times it appears). "Same" means, here, that the 
# elements in b are the elements in a squared, regardless of the order.

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