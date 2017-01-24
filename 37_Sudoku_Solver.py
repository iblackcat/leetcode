def solveSudoku(board):
    n = len(board)
    bb=[]
    for i in range(0,n):
        bb+=[list(board[i])]
    tag=[]
    for i in range(0,n):
        tmp=[]
        for j in range(0,n):
            tm=[]
            for k in range(0,n):
                tm+=[0]
            tmp+=[tm]
        tag+=[tmp]
    blank=[]
    for i in range(0,n):
        for j in range(0,n):
            if (bb[i][j]!='.'):
                num=int(bb[i][j])-1
                for p in range(0,n):
                    tag[i][p][num]=1
                    tag[p][j][num]=1
                for p in range((i/3)*3,(i/3+1)*3):
                    for q in range((j/3)*3,(j/3+1)*3):
                        tag[p][q][num]=1
            else :
                blank+=[[i,j,-1,-1]]
    i=0
    flag=2
    index=2
    while i<len(blank):
        x=blank[i][0]
        y=blank[i][1]
        num=blank[i][2]
        ind=blank[i][3]
        #print(i,x,y,num)
        if (blank[i][2]>=0):
            for p in range(0,n):
                if ind==tag[x][p][num]:
                    tag[x][p][num]=0
                if ind==tag[p][y][num]:
                    tag[p][y][num]=0
            for p in range((x/3)*3,(x/3+1)*3):
                for q in range((y/3)*3,(y/3+1)*3):
                    if ind==tag[p][q][num]:
                        tag[p][q][num]=0
        num+=1
        while num<n and tag[x][y][num]>0:
            num+=1
        if num==n:
            blank[i][2]=-1
            i-=1
            continue
        else:
            blank[i][2]=num
            blank[i][3]=index
            for p in range(0,n):
                if tag[x][p][num]==0:
                    tag[x][p][num]=index
                if tag[p][y][num]==0:
                    tag[p][y][num]=index
            for p in range((x/3)*3,(x/3+1)*3):
                for q in range((y/3)*3,(y/3+1)*3):
                    if tag[p][q][num]==0:
                        tag[p][q][num]=index
            i+=1
        flag+=1
        index+=1
    i=0
    while i<len(blank):
        x=blank[i][0]
        y=blank[i][1]
        num=blank[i][2]
        #print(x,y,num+1)
        bb[x][y]=str(int(num+1))
        i+=1
    for i in range(0,n):
        board[i]=''.join(bb[i])
#bb=["519748632","783652419","426139875","357986241","264317598","198524367","975863124","832491756","641275983"]
#bb=["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
bb=["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
solveSudoku(bb)
print(bb)
