def is_palindrome(str):
    a = "It is palindrome"
    for i in range(len(str)):
        if str[i] != str[len(str)-i-1]:
            a = "It is not palindrome"
    return a
str=input()
print(is_palindrome(str))
