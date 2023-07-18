import sys
def largest(arr):
    max = -sys.maxsize
    a = -1
    for i in arr:
        if i == 1:
            a = arr.index(i)
            for j in arr[a+1:]:
                if j == 1:
                    diff = arr.index(j) - arr.index(i) + 1
                    if diff > max:
                        max = diff
    return max
s=input()
srev=s[::-1]
dp=[[0 for j in range(len(srev)+1)] for i in range(len(s)+1)]
dp[0][0] = 1
for i in range(1,len(srev)+1):
    for j in range(1,len(s)+1):
        if srev[i-1] == s[j-1]:
            dp[i][j] = 1
# print(dp)
maximum = -sys.maxsize
for i in dp:
    # x = largest(i)
    # if x > maximum:
    #     maximum = x

    print(largest(i))
print(maximum)