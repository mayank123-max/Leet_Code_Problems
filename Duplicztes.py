# def solve(array):
#     for i in range(len(array)):
#         if array[abs(array[i])] > 0:
#             array[abs(array[i])-1] = -array[abs(array[i])-1]
#         else:
#             return True
#     return False

# array = list(map(int,input().split()))
# solve(array)


d1={1:2,2:3}
d2={2:3,1:2}
print(d1==d2)