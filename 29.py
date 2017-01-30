import sys

def divide(dividend, divisor):
    if (divisor == 0):
        return sys.maxint
    sign = 1
    ans = 0
    if (dividend < 0):
        sign = -sign
        dividend = -divident
    if (divisor < 0):
        sign = -sign
        divisor = -divisor
    while (dividend >= divisor):
        dividend -= divisor
        ans += 1
    if (sign == 1):
        return ans
    else :
        return -ans

print(divide(5,0))
        
