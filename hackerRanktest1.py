import re
def missingCharacters(s):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    digit =['0','1','2','3','4','5','6','7','8','9']
    alpha1 = []
    digit1 = []
    for i in s:
        if i in alpha:
            alpha.remove(i)
            alpha1.append(i)
        elif i in digit:
            digit.remove(i)
            digit1.append(i)
    print(alpha)
    print(digit)
    print(alpha1)
    print(digit1)
    result = []
    digit.extend(alpha)
    print(digit)
    join = ''.join(digit)
    return join
user = input()
print(missingCharacters(user))
