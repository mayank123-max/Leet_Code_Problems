def solve(a):
    c = 0
    minimum = len(a)
    d = {}
    for i in a:
        d[i] = []
    for i in range(len(a)):
        d[a[i]].append(i)
    print(d)
    for i in d:
        if len(d[i]) == 1:
            c += 1
    if c == len(d):
        return -1
    else:
        for i in d:
            if len(d[i]) > 1:
                diff = d[i][-1] - d[i][0]
                if diff < minimum:
                    minimum = diff
        return minimum
array = list(map(int,input().split()))
print(solve(array))