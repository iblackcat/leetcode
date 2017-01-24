def myPow(x, n):
    flag=0
    if n<0:
        n=-n
        flag=1
    ans=1
    i=0
    now=x
    while(n!=0):
        if (n&1==1):
            ans*=now
        i+=1
        n=(n>>1)
        now*=now
    if flag==0:
        return ans
    else:
        return 1.0/ans
print(myPow(4.323423,-333))
