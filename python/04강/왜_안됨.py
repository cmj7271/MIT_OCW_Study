t=int(input())
li=[]
    
def f(n,m):
    s=1
    for x in range(n):
        s *= (m-x) // (n-x)
        
    return s

for x in range(t):
    n,m=map(int,input().split())
    print(int(f(n,m)))