def spiralOrder(matrix):
    m=len(matrix)
    if (m<=0): return []
    n=len(matrix[0])
    if (n<=0): return []
    up=0
    down=m-1
    left=0
    right=n-1
    add=[[0,1],[1,0],[0,-1],[-1,0]]
    ans=[]
    x=0
    y=0
    now=0
    tag=1
    while (len(ans)<m*n):
        if (tag==1):
            ans+=[matrix[x][y]]
        xx=x+add[now][0]
        yy=y+add[now][1]
        if (now==0 and yy<=right)or(now==1 and xx<=down)or(now==2 and yy>=left)or(now==3 and xx>=up):
            x=xx
            y=yy
            tag=1
        else:
            if (now==0): up+=1
            elif (now==1): right-=1
            elif (now==2): down-=1
            elif (now==3): left+=1
            now=(now+1)%4
            tag=0
    return ans

print(spiralOrder([[1],[2]]))
