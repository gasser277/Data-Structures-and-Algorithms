import random
def get_min_max(arr):
    if len(arr) == 0:
        return None
    min = arr[0]
    max = arr[0]
    for i in arr:
        if i< min:
            min = i
        if i> max:
            max = i
    return (min, max)
#Test case 1
# assert(get_min_max([]) is None)
print ("Pass" if None == get_min_max([]) else "Fail")
# Test case 2
assert((0, 0) == get_min_max([0, 0, 0, 0, 0, 0, 0, 0]))
print ("Pass" if (0, 0) == get_min_max([0, 0, 0, 0, 0, 0, 0, 0]) else "Fail")
# Test case 3
l = [i for i in range(0, 10)]  
random.shuffle(l)
assert((0, 9) == get_min_max(l))
print ("Pass" if (0, 9)  == get_min_max(l) else "Fail")

