import math
def rotate(matrix):
    size=len(matrix)
    ll=int(math.ceil(float(size)/2))
    ls=int(math.floor(float(size)/2))
    for i in range(0,ll):
        for j in range(0,ls):
            tmp = matrix[i][j]
            matrix[i][j]=matrix[size-1-j][i]
            matrix[size-1-j][i]=matrix[size-1-i][size-1-j]
            matrix[size-1-i][size-1-j]=matrix[j][size-1-i]
            matrix[j][size-1-i]=tmp
m=[[0,1,2],[3,4,5],[6,7,8]]
rotate(m)
print(m)
