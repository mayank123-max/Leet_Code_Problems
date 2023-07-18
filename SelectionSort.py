def SelectionSort(array):
    for i in range(len(array)-1):
        curr_min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[curr_min]:
                curr_min = j
        array[i] , array[curr_min] = array[curr_min] , array[i]

array = list(map(int,input().split()))
SelectionSort(array)
print(array)