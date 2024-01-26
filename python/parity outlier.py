# You are given an array (which will have a length of at least 3, but could be very large)
# containing integers. The array is either entirely comprised of odd integers
# or entirely comprised of even integers except for a single integer N.
# Write a method that takes the array as an argument and returns this "outlier" N.

def find_outlier(integers):
    # stores amounts of odd and even nums
    amt_odds = 0
    amt_even = 0
    # check if most elements are odd or even
    for i in range(3):
        if amt_even >= 2 or amt_odds >= 2:
            break
        if integers[i]%2 == 0:
            amt_even += 1
        else:
            amt_odds += 1
    # looks for outlier
    # even outlier
    if amt_odds > amt_even:
        for i in integers:
            if i%2 == 0:
                return i
    # odd outlier
    else:
        for i in integers:
            if i%2 == 1:
                return i