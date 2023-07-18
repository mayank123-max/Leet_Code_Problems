def solve(array, k):
    for i in range(len(array)):
        array[i] = 1 if array[i]%2 else 0
    count = 0
    map = {}
    prefix_Sum = [array[0]]
    for i in array:
        prefix_Sum.append(prefix_Sum[-1]+i)
    for i in prefix_Sum:
        tmp = i-k
        if map.get(tmp):
            count += map[tmp]
        map[i] = map.get(i,0)+1
    return count

array = list(map(int,input().split()))
k =int(input())
print(solve(array, k))