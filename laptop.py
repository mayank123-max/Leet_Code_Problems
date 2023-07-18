def solve(N, array, Q, query):
    maximum = 0
    l = []
    ans = []
    for i in query:
        maximum_budget = i[1]
        for j in array:
            if j[0] <= maximum_budget:
                l.append(array.index(j))
        for k in l:
            if array[k][1] > maximum:
                maximum = array[k][1]
        ans.append(maximum)
    return ans

N = int(input())
array = []
query = []
while N:
    array.append(list(map(int,input().split())))
    N -= 1
Q = int(input())
while Q:
    query.append(list(map(int,input().split())))
    Q -= 1
ans = solve(N, array, Q, query)
for i in ans:
    print(i)