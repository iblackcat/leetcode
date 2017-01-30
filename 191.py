#! D:/Program_Files/Python
#_*_ coding:utf8

import sys
import math

def hammingWeight(n):
    ans = 0
    while n != 0:
        ans += n&1
        n = n >> 1
    return ans

print hammingWeight(4)
