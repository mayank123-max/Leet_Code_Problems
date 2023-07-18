def solve(nums , target):
    hash = {}
    for i in range(len(nums)):
        hash[nums[i]] = i
    for i in range(len(nums)):
        if hash.get(target-nums[i]) and i != hash.get(target-nums[i]):
            return [i,hash[target-nums[i]]]

arr = list(map(int,input().split()))
target = int(input())
print(solve(arr,target))