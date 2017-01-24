class trie(object):
    def __init__(self,x):
        self.val=x
        self.fail=None
        self.ch=[None]*26
    
def findSubstring(s,words):
    size=len(words)
    if size==0:
        return []
    n=len(words[0])
    tree=trie(-2)
    tree.fail=tree
    lim=[]
    index=0
    for i in range(0,size):
        p=tree
        for j in range(0,n):
            loc=int(words[i][j],36)-int('a',36)
            if p.ch[loc]==None:
                p.ch[loc]=trie(-1)
            p=p.ch[loc]
        if p.val>=0:
            lim[p.val]+=1
        else:
            p.val=index
            index+=1
            lim+=[1]

    for i in range(0,size):
        p=tree
        for j in range(0,n):
            loc=int(words[i][j],36)-int('a',36)
            k=p.fail
            while k.ch[loc]==None and k.val!=-2:
                k=k.fail
                print(k.val)
            if k.ch[loc]!=None and j!=0:
                p.ch[loc].fail=k.ch[loc]
            else:
                p.ch[loc].fail=k
            print(p.ch[loc].fail.val)
            p=p.ch[loc]
    p=tree
    nums=[]
    for i in range(0,len(s)):
        loc=int(s[i],36)-int('a',36)
        while p.ch[loc]==None and p.val!=-2:
            p=p.fail
        if p.ch[loc]!=None:
            p=p.ch[loc]
        nums+=[p.val]
    j=0
    ans=[]
    ans_tmp=[0]*len(s)
    for i in range(0,n):
        j=i+n-1
        queue=[]
        flag=[0]*index
        now=0
        fail=0
        while j<len(s):
            if nums[j]<0 or (len(queue)>0 and nums[j]==queue[len(queue)-1][0] and j-queue[len(queue)-1][1]<n):
                fail+=1
                if (fail>=n):
                    queue=[]
                    flag=[0]*index
                    now=0
            else:
                fail=0
                if flag[nums[j]]==lim[nums[j]]:
                    for k in range(0,len(queue)):
                        if queue[k][0]==nums[j]:
                            break
                        else:
                            flag[queue[k][0]]-=1
                    now-=k
                    queue=queue[k+1:]
                    queue+=[[nums[j],j]]
                    if now==size:
                        ans_tmp[queue[0][1]-(n-1)]=1
                        #ans+=[queue[0][1]-(n-1)]
                else:
                    queue+=[[nums[j],j]]
                    flag[nums[j]]+=1
                    now+=1
                    if now==size:
                        ans_tmp[queue[0][1]-(n-1)]=1
                        #ans+=[queue[0][1]-(n-1)]
            j+=1
    for i in range(0,len(s)):
        if ans_tmp[i]==1:
            ans+=[i]
    return ans

print(findSubstring("ccaacbbaabcbaddcddbbbddaaaacadbcbbcacdacbc",["bca","bcb","cda"]))
            
