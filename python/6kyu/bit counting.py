# Write a function that takes an integer as input, and returns
# the number of bits that are equal to one in the binary 
# representation of that number. You can guarantee that input is non-negative.

def count_bits(n):
    n = str(bin(n))
    amt = 0
    for i in n:
        if i == "1":
            amt += 1
    return amt