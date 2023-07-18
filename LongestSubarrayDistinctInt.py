def solve(array):
    l=[]
    maximum = 0
    for i in array:
        if i not in l:
            l.append(i)
        else:
            maximum = max(len(l), maximum)
            l=[i]
    return maximum

array = input().split()
print(solve(array))