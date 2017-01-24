class trie(object):
    def __init__(self,x):
        self.val=x
        self.ch=[None]*26

def groupAnagrams(strs):
    tree=trie(-1)
    size=len(strs)
    ans=[]
    for i in range(0,size):
        tmp=''.join(sorted(strs[i]))
        le=len(tmp)
        p=tree
        for j in range(0,le):
            loc=int(tmp[j],36)-int('a',36)
            if p.ch[loc]==None:
                p.ch[loc]=trie(-1)
            p=p.ch[loc]
        if p.val!=-1:
            ans[p.val]+=[strs[i]]
        else:
            p.val=len(ans)
            ans+=[[strs[i]]]
    return ans

print(groupAnagrams(['nde','dne','abc','ee','eb','bca']))
