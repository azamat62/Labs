def palindrome(a):
    txt = a[::-1]
    return txt == txt[::-1]
print (palindrome(str(input())))