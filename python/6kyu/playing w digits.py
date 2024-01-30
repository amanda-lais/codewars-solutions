# Given two positive integers n and p, we want to find a
# positive integer k, if it exists, such that the sum of
# the digits of n raised to consecutive powers 
# starting from p is equal to k * n.

def dig_pow(n, p):
    n_str = str(n)
    np_sum = 0
    for i in range(len(n_str)):
        np_sum += int(n_str[i])**p
        p += 1
    if np_sum%n == 0:
        return np_sum/n
    else:
        return -1