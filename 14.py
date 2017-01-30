def longestCommonPrefix(strs):
        ans = ""
        num = 0
        l = len(strs)
        if (l==0):
            return ""
        elif (l==1):
            return strs[0]
        while (1):
            if (num >= len(strs[0])) :
                return ans
            ch = strs[0][num]
            for s in strs[1:] :
                if (num >= len(s)) :
                    return ans
                elif (s[num] != ch) :
                    return ans
            ans += strs[0][num]
            num += 1
        return ""

a = "ans"
b = "abcccccc"
c = "a"
strs = []
print(longestCommonPrefix(strs))
        
