#1012 유기농배추 구현중
testcase=int(input())
for i in range(testcase):
    m,n,k=input().split()
    m=int(m)
    n=int(n)
    k=int(k)
    graph=[[0 for a in range(m)]for b in range(n)]
    
    for j in range(k):
        target=list(map(int,input().split()))
        graph[target[1]][target[0]]=1
