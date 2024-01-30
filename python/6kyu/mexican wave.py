# In this simple Kata your task is to create a function that turns a string into a Mexican Wave. 
# You will be passed a string and you must return that string in an 
# array where an uppercase letter is a person standing up. 

def wave(people):
    ans = []
    for i in range(len(people)):
        if people[i] == " ":
            continue
        if i == 0:
            x = slice(1, len(people))
            s = people[i].upper() + people[x]
        elif i == (len(people)-1):
            y = slice(0, len(people)-1)
            s = people[y] + people[i].upper()
        else:
            x = slice(0, i)
            y = slice(i+1, len(people))
            s = people[x] + people[i].upper() + people[y]
        ans.append(s)
    return ans