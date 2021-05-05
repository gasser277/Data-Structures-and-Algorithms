def sqrt(value):
    if not isinstance(value, int):
        print("Invalid Input")
        return
    if value == 0 or value == 1:
        return value
    i = 1
    last_value = value
    while i <= last_value:
        mid = (i + last_value) // 2
        mid_squared = mid * mid
        if mid_squared == value:
            return mid
        elif mid_squared < value:
            i = mid + 1
            result = mid
        else:
            last_value = mid - 1
    return result
# Test case 1
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
# Test case 2
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
# Test case 3
print("Pass" if (sqrt(None) is None) else "Fail")
# Test case 4
print("Pass" if (9999 == sqrt(99999999)) else "Fail")

