def countAndSay(n):
    if (n<=0):
        return 0
    i = 1
    now = '1'
    last = ''
    while (i < n):
        last = now
        now = ''
        l = len(last)
        count = 0
        for j in range(0,l):
            if (j>0 and last[j] != last[j-1]):
                now += str(count)
                now += last[j-1]
                count = 0
            count += 1
        now += str(count)
        now += last[l-1]
        i += 1
    return now

print countAndSay(0)
print countAndSay(1)
print countAndSay(2)
print countAndSay(3)
print countAndSay(4)
print countAndSay(5)
print countAndSay(8)
