def solve(array, k):
    count = 0
    prefix_Sum=[0]
    map = {}
    for i in array:
        prefix_Sum.append(prefix_Sum[-1]+i)
    
    for i in prefix_Sum:
        tmp = i -k
        if map.get(tmp):
            count += map[tmp]
        map[i] = map.get(i,0)+1
    return count

array = list(map(int,input().split()))
k = int(input())
print(solve(array, k))