def gold(lst,n,k):
    for i in range(n):
        sm=lst[i]
        if i+1<n:
            for j in range(i+1,n):
                sm += lst[j]
                if sm==k:
                    return i+1 , j+1
                if sm>k:
                    break
n,k=map(int,input().split())
lst=list(map(int,input().split()))[:n]
t = gold(lst,n,k)
print(type(t) == "tuple")
if type(t) == 'tuple':
    for i in t:
        print(i,end=" ")