def solve(array, B):
    count = 0
    subarray = []
    for i in range(len(array)):
        for j in range(i+1,len(array)+1):
            subarray.append(array[i:j])
    for i in subarray:
        lc = 0
        for j in i:
            if j%2 != 0:
                lc += 1
        if lc == B:
            count += 1
    return count

array = list(map(int,input().split()))
B = int(input())
print(solve(array, B))