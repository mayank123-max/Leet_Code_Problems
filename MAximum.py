def solve(array):
    s = 0
    maximum = array[0]
    minimum = array[0]
    for i in array:
        s += i
        if s>maximum:
            maximum = s
        if s<0:
            s =0
    for i in array:
        s += i
        if s<minimum:
            minimum = s
        if s>0:
            s=0
    return max(s,maximum, abs(minimum))

array = list(map(int,input().split()))
print(solve(array))