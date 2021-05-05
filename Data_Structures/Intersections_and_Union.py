class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    Union_Set=set()
    current_node=llist_1.head
    while current_node:
        Union_Set.add(current_node.value)
        current_node=current_node.next
    current_node=llist_2.head
    while  current_node:
        Union_Set.add(current_node.value)
        current_node=current_node.next
    return Union_Set

def intersection(llist_1, llist_2):
    Set1=set()
    Set2=set()
    current_node=llist_1.head
    while current_node:
        Set1.add(current_node.value)
        current_node=current_node.next
    current_node=llist_2.head
    while current_node:
        Set2.add(current_node.value)
        current_node=current_node.next
    intersection_set=Set1.intersection(Set2)
    return intersection_set
    


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
print("////////////")
# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_3 = []
element_4 = [1,7,8,9,11,21,1]

for i in element_3:
    linked_list_3.append(i)

for i in element_4:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))#returns element 4 without repotion because no element in element3
print (intersection(linked_list_3,linked_list_4))#empty set (no intersection)
print("////////////")
# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_5 = []
element_6 = []

for i in element_5:
    linked_list_5.append(i)

for i in element_6:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))#returns empty
print (intersection(linked_list_5,linked_list_6))#returns empty
print("////////////")
