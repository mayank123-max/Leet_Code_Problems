def solve(array):
    d = {}
    subarray = []
    for i in range(len(array)):
        for j in range(i+1,len(array)+1):
            subarray.append(array[i:j])
    for i in subarray:
        if len(str(i)) == 1:
            d[int(i)] = d.get(int(i),0)+1
        else:
            l=list(i)
            prod = 1
            for i in l:
                prod *= i
            d[prod] = d.get(prod,0)+1
    for i in d:
        if d[i] != 1:
            return 0
    return 1
num = int(input())
print(solve(list(map(int,str(num)))))