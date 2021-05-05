def rotated_array_search(arr, value):
    return rotated_array_search_recursive(arr,value,0,len(arr) - 1)
def rotated_array_search_recursive(arr, value, initial, final):
    if initial > final:
        return -1
    middle_index = (initial + final) // 2
    middle_element = arr[middle_index]
    if middle_element == value:
        return middle_index
    if arr[initial] <= middle_element:
        if middle_element > value and arr[initial] <= value:
            return rotated_array_search_recursive(arr,value,initial,middle_index - 1)
        return rotated_array_search_recursive(arr,value,middle_index + 1,final)
    if middle_element < value and arr[final] >= value:
        return rotated_array_search_recursive(arr,value,middle_index + 1,final)
    return rotated_array_search_recursive(arr,value,initial,middle_index - 1)
def linear_search(arr, value):
    for index, element in enumerate(arr):
        if element == value:
            return index
    return -1
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list,
                                                                 number):
        print("Pass")
    else:
        print("Fail")

# Test case 1
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Test case 2
test_function([[], 10])
test_function([[1], 1])
test_function([[1], 0])

# Test case 3
test_function([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 3])

