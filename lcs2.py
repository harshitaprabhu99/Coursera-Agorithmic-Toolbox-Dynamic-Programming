def longestsub(X,Y,m,n):
    l=list()
    for i in range(m+1):
        l.append([None]*(n+1))
    for i in range(m+1):
        for j in range(n+1):
            if i ==0 or j==0:
                l[i][j]=0
            elif X[i-1]==Y[j-1]:
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
    return l[m][n]

a=int(input())
X=list(map(int,input().split(' ',a)))
b=int(input())
Y=list(map(int,input().split(' ',b)))
print(longestsub(X,Y,a,b))
