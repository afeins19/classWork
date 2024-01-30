def isPalindrome(s):
    reverse=""
    for i in range(len(s)-1,-1,-1):
        reverse+=s[i]
    if reverse==s:
        return True
    return False

userString = input("Please input your string: ")
print(isPalindrome(userString))