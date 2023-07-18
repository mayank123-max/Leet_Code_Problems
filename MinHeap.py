from heapq import heapify, heappush, heappop, _heapify_max
array = list(map(int,input().split()))
k = int(input())
min_heap = []
max_heap = []
# heapify(min_heap)
heapify(max_heap)
for i in array:
    # heappush(min_heap, i)
    heappush(max_heap, -1*i)
# while k-1:
#     heappop(min_heap)
#     heappop(max_heap)
#     k -= 1
# print("Kth Smallest Element:-",heappop(min_heap))
# print("Kth Largest Element:-",heappop(max_heap))
max_heap = [-i for i in max_heap]
print(max_heap)