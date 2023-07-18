# def solve(array , n):
#     if n < 0:
#         return 0
#     if n == 0:
#         return 1
#     for i in range(len(array)):
#         ways += solve(array , n-array[i])
#     return ways

def count(S, m, n ):
    if (n == 0):
        return 1
    if (n < 0):
        return 0
    if (m <=0):
        return 0
    return count( S, m - 1, n ) + count( S, m, n-S[m-1] )
n,m = list(map(int,input().split()))
array = list(map(int,input().split()))
print(count(array, m, n))