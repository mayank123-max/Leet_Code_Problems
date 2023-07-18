from copy import copy,deepcopy
array = [1,2,3,4,5]
array2 = copy(array)
array3 = deepcopy(array)
array4 = array
array4.append(10)
# array.append(6)
# array2.append(6)
array3.append(6)
print(array, array2, array3)