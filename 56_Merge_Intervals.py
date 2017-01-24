class Interval(object):
    def __init__(self,s=0,e=0):
        self.start = s
        self.end = e
def cmp(a,b):
    if a.start>b.start: return 1
    elif a.start==b.start: return 0
    else: return -1
def merge(intervals):
    n = len(intervals)
    if n==0: return []
    intervals=sorted(intervals,cmp)
    l=1
    ans=[]
    ans+=[intervals[0]]
    for i in range(1,n):
        if ans[l-1].end>=intervals[i].start:
            ans[l-1].end=max(ans[l-1].end,intervals[i].end)
        else:
            ans+=[intervals[i]]
            l+=1
    return ans

a = Interval(-100,1000)
c = Interval(-1000,-200)
b = Interval(8,19)
d = Interval(15,18)
ans = merge([a,b,c,d])
for i in range(0, len(ans)):
    print(ans[i].start, ans[i].end)
