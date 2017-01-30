def strStr(haystack, needle):
    l1 = len(haystack)
    l2 = len(needle)
    if (l1 == 0 and l2 == 0):
        return 0
    for i in range(0,l1):
        if (l1-i < l2):
            return -1
        tag = 1
        for j in range(0,l2):
            if (haystack[i+j] != needle[j]):
                tag = 0
                break
        if (tag == 1):
            return i
    return -1
    
a = ""
b = ""
print(strStr(a,b))
