def solve(array):
    missing = 0
    repeated = 0
    temp = [0 for i in range(len(array)+1)]
    for i in array:
        temp[i] += 1
    print(temp[1:])
    for i in range(1,len(temp)):
        if temp[i] == 0:
            missing = i
        else:
            if temp[i] > 1:
                repeated = i
    return missing, repeated

array = list(map(int,input().split()))
print(solve(array))