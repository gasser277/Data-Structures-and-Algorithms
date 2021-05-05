
class Node(object):
    def __init__(self,key,value):
            self.key=key
            self.value=value
            self.next=None
            self.prev=None            
    pass
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.capacity=capacity
        self.length=0
        self.hash={}

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.hash or self.length>self.capacity:
            print(-1)
            return -1
        
        else: 
            current_node=self.hash[key]
            current_node.prev.next=current_node.next
            current_node.next=current_node.prev
            self.tail.next=current_node
            current_node.prev=self.tail
            self.tail=current_node
            print(current_node.value)    
            return current_node.value

            
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.hash:
            current_node=self.hash[key]
            current_node.value=value
            self.tail.next=current_node
            current_node.prev=self.tail
            self.tail=current_node  ##
            self.length+=1
            if self.length>self.capacity:
                current_node=self.head.next
                self.head.next=self.head.next.next
                self.head.next.next.prev=self.head
                # self.tail.next=current_node
                # current_node.prev=self.tail
                # self.tail=current_node
                
        else: 
            current_node=Node(key,value)
            self.hash[key]=current_node
            self.tail.next=current_node
            current_node.prev=self.tail
            self.tail=current_node
            self.length+=1
            if self.length>self.capacity:
                current_node=self.head.next
                self.head.next=self.head.next.next
                self.head.next.prev=self.head
                # self.tail.next=current_node
                # current_node.prev=self.tail
                # self.tail=current_node
                

# Test Case 1:
our_cache = LRU_Cache(5)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache
our_cache.set(5, 5) 
our_cache.set(6, 6)
our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print("///////////////////////////////////////////////////////////////////////")
# Test Case 2:
our_cache = LRU_Cache(1000)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache
our_cache.set(5, 5) 
our_cache.set(6, 6)
our_cache.get(3)    # returns 3 now because cache hasnt reached its capacity
print("///////////////////////////////////////////////////////////////////////")
# Test Case 3:
our_cache = LRU_Cache(0)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
our_cache.get(1)       # returns -1
our_cache.get(2)       # returns -1
our_cache.get(9)      # returns -1  
our_cache.set(5, 5) 
our_cache.set(6, 6)
our_cache.get(3)    # returns -1 because its zero size     
print("///////////////////////////////////////////////////////////////////////")

