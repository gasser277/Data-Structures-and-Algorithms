class MaxHeap:
    def __init__(self, initial_find_size=10):
        self.cbt = [None for _ in range(initial_find_size)]
        self.next_index = 0

    def insert(self, data):
        if self.next_index == len(self.cbt):
            newArray = [None for _ in range(len(self.cbt)*2)]
            newArray[:len(self.cbt)] = self.cbt
            self.cbt = newArray
        self.cbt[self.next_index] = data
        self._up_heapify()
        self.next_index += 1

    def remove(self):
        if self.find_size() == 0:
            return None
        self.next_index -= 1

        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        self.cbt[0] = last_element

        self.cbt[self.next_index] = None
        self._down_heapify()

        return to_remove

    def _up_heapify(self):
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element < child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element
                child_index = parent_index
            else:
                break

    def _down_heapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent = self.cbt[parent_index]
            left_child = None
            right_child = None

            max_element = parent

            # check if left child exists
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            # compare with left child
            if left_child is not None:
                max_element = max(parent, left_child)

            # compare with right child
            if right_child is not None:
                max_element = max(right_child, max_element)

            # check if parent is rightly placed
            if max_element == parent:
                return

            if max_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = max_element
                parent = left_child_index

            elif max_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = max_element
                parent = right_child_index

    def find_size(self):
        return self.next_index

def rearrange_digits(arr):
    if len(arr) == 0:
        return None
    max_heap = MaxHeap()
    for input in arr:
        max_heap.insert(input)
    first_val = ""
    second_val = ""
    for i in range(max_heap.find_size()):
        if i % 2 == 1:
            first_val += str(max_heap.remove())
        else:
            second_val += str(max_heap.remove())
    return [int(first_val), int(second_val)]
def test_function(test):
    output = rearrange_digits(test[0])
    result = test[1]
    if sum(output) == sum(result):
        print("Pass")
    else:
        print("Fail")
# Test case 1
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])


# Test case 2
test_function([[9, 1, 8, 2, 7, 3, 9], [9831, 972]])

# Test case 3
test_function([[1, 1, 1, 1, 1], [111, 11]])
test_function([[1, 1, 2, 2, 3, 3, 4, 4], [4321, 4321]])
