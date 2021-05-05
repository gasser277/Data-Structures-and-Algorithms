import sys
import heapq

class Heap_node:
    def __init__(self, char, freqval):
        self.char = char
        self.freqval = freqval
        self.left = None
        self.right = None

    def __gt__(self, other):
        if not other:
            return -1
        if not isinstance(other, Heap_node):
            return -1
        return self.freqval > other.freqval

class Huffman_Coding:

    def huffman_encoding(self, text):
        if text == "":
            return "", None
        freqvaluency_dict = self.make_freqvaluency_dict(text)
        min_heap = self.min_heapify_dict(freqvaluency_dict)
        merged_heap = self.merge_nodes(min_heap)
        tree = heapq.heappop(merged_heap)
        codes = self.codes(tree)
        huffman_encodingd_text = self.get_huffman_encoding_text(text, codes)
        return huffman_encodingd_text, tree

    def decode(self, huffman_encodingd_text, tree):
        decoded_string = ""

        if huffman_encodingd_text == "":
            return decoded_string

        current_node = tree

        for char in huffman_encodingd_text:
            if char == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right
            if current_node.char is not None:
                decoded_string += current_node.char
                current_node = tree
        return decoded_string  

    def make_freqvaluency_dict(self, text):
        freqvaluency = {}
        for char in text:
            if not char in freqvaluency:
                freqvaluency[char] = 0
            freqvaluency[char] += 1
        return freqvaluency

    def min_heapify_dict(self, freqvaluency):
        heap = []
        for key in freqvaluency:
            node = Heap_node(key, freqvaluency[key])
            heapq.heappush(heap, node)
        return heap

    def merge_nodes(self, heap):
        if len(heap) == 1:
            node = heapq.heappop(heap)
            new_node = Heap_node(None, node.freqval)
            new_node.left = node
            heapq.heappush(heap, new_node)
        while len(heap) > 1:
            first_min_node = heapq.heappop(heap)
            second_min_node = heapq.heappop(heap)

            new_node = Heap_node(None, first_min_node.freqval + second_min_node.freqval)
            new_node.left = first_min_node
            new_node.right = second_min_node

            heapq.heappush(heap, new_node)
        return heap

    def codes(self, tree):
        if tree.left is None and tree.right is None:
            return {tree.char:'0'}
        return self.codes_recursive(tree, "")
    def codes_recursive(self, root, current_code):
        codes = {}
        if root is None:
            return {}
        if root.char is not None:
            codes[root.char] = current_code
        
        codes.update(self.codes_recursive(root.left, current_code + "0"))
        codes.update(self.codes_recursive(root.right, current_code + "1"))
        return codes

    def get_huffman_encoding_text(self, text, codes):
        huffman_encodingd_text = ""
        for char in text:
            huffman_encodingd_text += codes[char]
        return huffman_encodingd_text

if __name__ == "__main__":
    huffman_coding = Huffman_Coding()

    #Test Case 1
    test_sentence = "aaAAbbBB"
    print ("The size of the data is: {}\n".format(sys.getsizeof(test_sentence)))
    print ("The content of the data is: {}\n".format(test_sentence))
    huffman_encoding_data, tree = huffman_coding.huffman_encoding(test_sentence)
    print ("The size of the huffman_encodingd data is: {}\n".format(sys.getsizeof(int( huffman_encoding_data, base=2))))
    print ("The content of the huffman_encodingd data is: {}\n".format( huffman_encoding_data))
    decoded_data = huffman_coding.decode( huffman_encoding_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the huffman_encodingd data is: {}\n".format(decoded_data))
    print ("The size of the data is: {}\n".format(sys.getsizeof(test_sentence)))
    print ("The content of the data is: {}\n".format(test_sentence))
    huffman_encoding_data, tree = huffman_coding.huffman_encoding(test_sentence)
    decoded_data = huffman_coding.decode( huffman_encoding_data, tree)
    
    #Test Case 2
    test_sentence = "a"
    print ("The size of the data is: {}\n".format(sys.getsizeof(test_sentence)))
    print ("The content of the data is: {}\n".format(test_sentence))
    huffman_encoding_data, tree = huffman_coding.huffman_encoding(test_sentence)
    print ("The size of the huffman_encodingd data is: {}\n".format(sys.getsizeof(int( huffman_encoding_data, base=2))))
    print ("The content of the huffman_encodingd data is: {}\n".format( huffman_encoding_data))
    decoded_data = huffman_coding.decode( huffman_encoding_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the huffman_encodingd data is: {}\n".format(decoded_data))
    
    #Test Case 3
    test_sentence = "aaaaaaa"
    print ("The size of the data is: {}\n".format(sys.getsizeof(test_sentence)))
    print ("The content of the data is: {}\n".format(test_sentence))
    huffman_encoding_data, tree = huffman_coding.huffman_encoding(test_sentence)
    print ("The size of the huffman_encodingd data is: {}\n".format(sys.getsizeof(int( huffman_encoding_data, base=2))))
    print ("The content of the huffman_encodingd data is: {}\n".format( huffman_encoding_data))
    decoded_data = huffman_coding.decode( huffman_encoding_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the huffman_encodingd data is: {}\n".format(decoded_data))
    
    #Test Case 4 #different case letters
    test_sentence = "aaAAbbBB"

    print ("The size of the data is: {}\n".format(sys.getsizeof(test_sentence)))
    print ("The content of the data is: {}\n".format(test_sentence))
    huffman_encoding_data, tree = huffman_coding.huffman_encoding(test_sentence)
    print ("The size of the huffman_encodingd data is: {}\n".format(sys.getsizeof(int( huffman_encoding_data, base=2))))
    print ("The content of the huffman_encodingd data is: {}\n".format( huffman_encoding_data))
    decoded_data = huffman_coding.decode( huffman_encoding_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the huffman_encodingd data is: {}\n".format(decoded_data))
    
    #Test case 5
    test_sentence = " "
    print ("The size of the data is: {}\n".format(sys.getsizeof(test_sentence)))
    print ("The content of the data is: {}\n".format(test_sentence))
    huffman_encoding_data, tree = huffman_coding.huffman_encoding(test_sentence)
    print ("The size of the huffman_encodingd data is: {}\n".format(sys.getsizeof(int( huffman_encoding_data, base=2))))
    print ("The content of the huffman_encodingd data is: {}\n".format( huffman_encoding_data))
    decoded_data = huffman_coding.decode( huffman_encoding_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the huffman_encodingd data is: {}\n".format(decoded_data))



