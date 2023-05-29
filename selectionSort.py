def selectionSort(array, size):
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
        
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j

        (array[ind], array[min_index]) = (array[min_index], array[ind])

arr_size = int(input("Enter size of array: "))
arr = []

for i in range(arr_size):
    user_input = int(input("Enter the value:- "))
    arr.append(user_input)

print("\nUnsorted Array:- {}".format(arr))
size = len(arr)

selectionSort(arr, size)
print("\nSorted Array:- {}".format(arr))