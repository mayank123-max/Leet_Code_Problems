def solve(array, ans=[], l=[]):
    if len(array) == 0:
        ans.append(l)
        return
    for i in range(len(array)):
        l.append(array[i])
        solve(array[i+1:], ans, l)
    l.pop(-1)
    return ans

array = [1,2,3]
print(solve(array))