# Write a function that takes an array of numbers 
# (integers for the tests) and a target number. 
# It should find two different items in the 
# array that, when added together, give the 
# target value. The indices of these items should 
# then be returned in a tuple / list (depending 
# on your language) like so: (index1, index2).

def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            if (numbers[i] + numbers[j]) == target:
                return (i, j)