class Interval(object):
    def __init__(self,s=0,e=0):
        self.start = s
        self.end = e
def find(intervals, s, t, tmp, flag):
    if (s>t):
        if flag==0: return Interval(tmp,s)
        else: return Interval(tmp,t)
    mid=(s+t)/2
    now=intervals[mid]
    if (now.start<=tmp and now.end>=tmp):
        if (flag==0): return Interval(now.start,mid)
        else: return Interval(now.end,mid)
    elif (now.start<=tmp):
        return find(intervals,mid+1,t,tmp,flag)
    else:
        return find(intervals,s,mid-1,tmp,flag)

def merge(intervals,newInterval):
    n = len(intervals)
    if n==0: return [newInterval]
    ss=find(intervals,0,n-1,newInterval.start,0)
    tt=find(intervals,0,n-1,newInterval.end,1)
    newInterval.start=ss.start
    newInterval.end=tt.start
    s=ss.end
    t=tt.end
    print(s,t)
    if (s<=t):
        intervals=intervals[:s+1]+intervals[t+1:]
        intervals[s]=newInterval
    else:
        if (t<0):
            t=-1
        intervals=intervals[:t+1]+[newInterval]+intervals[s:]
    return intervals

a = Interval(-21,-2)
b = Interval(3,5)
c = Interval(6,7)
d = Interval(8,10)
e = Interval(12,16)
f = Interval(1,2)
ans = merge([a,b,c,d,e],f)
for i in range(0, len(ans)):
    print(ans[i].start, ans[i].end)
