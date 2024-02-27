# Given a string, return a new string where the first and last chars have been exchanged.
# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba

def front_back(str):
    print(str[-1]+str[1:-1]+str[0])
front_back('tanu')
