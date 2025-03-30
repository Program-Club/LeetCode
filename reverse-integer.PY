# Method 1 ✅

def reverse(x):
        sign = 1 if x >= 0 else -1

        x = abs(x)

        ret = sign * int(str(x)[::-1])

        if ret > 2 ** 31 - 1 or ret < -2 ** 31:
            return 0
        else:
            return ret

print(reverse(120))