def solve(A,B):
    graph = {}
    for i in B:
        if graph.get(i[0]):
            graph[i[0]].append(i[1])
        else:
            graph[i[0]] = []
    return graph

A = int(input())
M = int(input())
B = []
while M:
    B.append(list(map(int,input().split())))
    M -= 1
print(solve(A,B))
