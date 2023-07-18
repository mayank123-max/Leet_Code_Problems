def solve(array):
    oc = 0
    for i in array:
        oc = 1 if i%2 else 0
    if oc == 0:
        return 0
    count = 0
    prefix_sum = [0]
    map = {}
    for i in array:
        prefix_sum.append(prefix_sum[-1]+i)
    for i in prefix_sum:
        for j in map:
            if j%2 == 0:
                count += map[j]
        map[i] = map.get(i,0)+1
    return count

array = list(map(int,input().split()))
print(solve(array))