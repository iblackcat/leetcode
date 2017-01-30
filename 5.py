#! D:/Program_Files/Python
#_*_ coding:utf8

import sys

def longestPalindrome(s):
    le = len(s)
    start = 0
    end = 0
    for i in range(0, le-1):
        if le - i < ((end - start + 1) >>1):
            break
        j = 0
        while i - j >= 0 and i + j < le:
            if s[i-j] != s[i+j]:
                break
            else:
                j += 1
        if (j << 1) - 1 > end - start + 1:
            start = i - j + 1
            end = i + j - 1
        j = 0
        while i - j >= 0 and i + 1 + j < le:
            if s[i-j] != s[i+j+1]:
                break
            else:
                j += 1
        if j<<1 > end - start + 1:
            start = i - j + 1
            end = i + j
    ans = s[start:end+1]
    return ans
a = 'b'
for i in range(0, 999):
    a += 'b'
print longestPalindrome("bbbbabbbb")
#print longestPalindrome('cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc')
    
    
