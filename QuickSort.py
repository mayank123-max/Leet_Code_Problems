def partition(nums, l, r):
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr

def quicksort(nums, l, r):
    if len(nums) == 1:
        return nums
    if l < r:
        pi = partition(nums, l, r)
        quicksort(nums, l, pi-1)
        quicksort(nums, pi+1, r)
    return nums

array = list(map(int,input().split()))
print(quicksort(array, 0, len(array)-1))