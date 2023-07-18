def rob(i, array, dp):
    if len(array) == 0:
        return 0
    if i >= len(array):
        return 0
    if dp[i] != -1:
        return dp[i]
    
    ans = max(array[i] + rob(i+2, array, dp), rob(i+1, array, dp))
    dp[i] = ans
    return ans

array = list(map(int,input().split()))
n = len(array)
dp = []
while n:
    dp.append(-1)
    n -= 1
print(dp)
print(rob(0, array, dp))