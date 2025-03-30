# Method 1 ✅

# def reverse(x):
#         sign = 1 if x >= 0 else -1

#         x = abs(x)

#         ret = sign * int(str(x)[::-1])

#         if ret > 2 ** 31 - 1 or ret < -2 ** 31:
#             return 0
#         else:
#             return ret

# print(reverse(120))

# Method 2 ✅

# def reverse(x):
#     sign = 1 if x >= 0 else -1
#     x = abs(x)
    
#     reversed_num = 0
#     while x:
#         reversed_num = reversed_num * 10 + x % 10
#         x //= 10

#     reversed_num *= sign

#     return reversed_num if -2**31 <= reversed_num <= 2**31 - 1 else 0

# print(reverse(120))

# Method 3 ✅

# def reverse(x):
#     sign = -1 if x < 0 else 1
#     x = abs(x)
    
#     digits = list(str(x))
#     digits.reverse()
    
#     reversed_num = int("".join(digits)) * sign
    
#     return reversed_num if -2**31 <= reversed_num <= 2**31 - 1 else 0

# print(reverse(120))
