# cook your dish here

def solve(array):
    l =[]
    c = 1
    for i in range(len(array)-1):
        if array[i] == array[i+1]:
            c += 1
        else:
            l.append(c)
            c = 1
    l.append(c)
    l.sort()
    if len(l) == 1:
        return "YES"
    elif l[-1] == l[-2]:
        return "NO"
    else:
        return "YES"
        
t = int(input())
while t:
    n = int(input())
    array = list(map(int,input().split()))
    array.sort()
    print(solve(array))
    t -= 1