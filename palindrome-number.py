# Method 1 ✅


# def isPalindrome(x: int):
#     a = list(str(x))
#     b = a[::-1]

#     if a == b:
#         return True
#     else:
#         return False
        
# print(isPalindrome(121))


# Method 2 ✅


# def isPalindrome(x: int):
#     s = str(x)
#     return s == s[::-1]

# print(isPalindrome(121))


# Method 3 ✅


def isPalindrome(x: int):
    s = str(x)
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True

print(isPalindrome(121))