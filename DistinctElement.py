def solve(array):
    s=set(array)
    return (3*sum(s)-sum(array))//2

array = list(map(int,input().split()))
print(solve(array))