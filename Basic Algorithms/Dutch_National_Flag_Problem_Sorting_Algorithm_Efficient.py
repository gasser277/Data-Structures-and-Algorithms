def sort_012(arr):
    i_current= 0
    i_0= 0
    i_2 = len(arr) - 1
    while(i_current) < i_2 + 1:
        current_val = arr[i_current]
        if current_val == 0:
            arr[i_current] = arr[i_0]
            arr[i_0] = current_val
            i_0+= 1
            i_current+= 1
        elif current_val == 1:
            i_current+= 1
        elif current_val == 2:
            arr[i_current] = arr[i_2]
            arr[i_2] = current_val
            i_2 -= 1
    return arr
def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

#Test case 1
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
#Test case 2
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
#Test case 3
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])