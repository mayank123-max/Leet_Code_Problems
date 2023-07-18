# Brute Force Approach To Count The Subarrays Having XOR Value Equal To K.........

def xor(array , k):
    xor = 0
    n =len(array)
    if n == 1 and array[0] == k:
        return k
    xor = array[0]
    for i in range(1,n):
        xor = xor ^ array[i]
    return xor

def solve(array , k):
    subarray = []
    count = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)+1):
            subarray.append(array[i:j])
    for i in subarray:
        if xor(i , k) == k:
            count += 1
    return count

array = list(map(int,input().split()))
k = int(input())
print(solve(array , k))