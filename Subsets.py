def solve(subset, ind, array, ans =[]):
    if ind == len(array):
        # print(subset)
        ans.append(subset)
        return ans
    solve(subset, ind+1, array, ans)
    subset.append(array[ind])
    solve(subset, ind+1, array, ans)
    subset.pop()

array = list(map(int,input().split()))
print(solve([], 0, array))