# Move the first letter of each word to the end of it, 
# then add "ay" to the end of the word. Leave punctuation marks untouched.

def pig_it(text):
    punctuation = "!#$%&'()*+,-.z/:;<=>?@[\]^_`{|}~" + '"'
    words = text.split()
    ans = ""
    for i in words:
        if i in punctuation:
            ans += i + ' '
            continue
        x = slice(1, len(i))
        ans += i[x] + i[0] + 'ay '
    no_extra_space = slice(0, len(ans)-1)
    return ans[no_extra_space]