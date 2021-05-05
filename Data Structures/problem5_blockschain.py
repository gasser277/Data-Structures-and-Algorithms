import hashlib
from datetime import datetime 
import pytz
utc = pytz.utc
class Block: #Class Block which stores timestamp,data, prev Hash , and calculates and stores Its Hash.
    def __init__(self,timestamp, data, previous_hash):
        self.timestamp=timestamp
        self.data=data
        self.previous_hash=previous_hash #Hash of the previous Block
        self.current_hash=None #Hash of the block
        self.next=None
    def calc_hash(self):#Method to find Hash of Block
      if self.data is None:
          return None
      sha = hashlib.sha256()
      hash_str = self.data.encode('utf-8')
      sha.update(hash_str)
      Block_Hash=sha.hexdigest
      return Block_Hash        #Hash of Block
    
    def insert_hash(self,hash_val): #Method To insert the Hash Value in the block
        self.current_hash=hash_val
        
      
class Blockchain: #BlockChain as Linked List which connects the Blocks
    def __init__(self):
        self.head=None
    def Insert_Block(self,timestamp, data, previous_hash): #Method to insert a Block in the end of Blockchain, it takes these data as input and stores them in a new block which will be inserted in the block chain
        Blockk=Block(timestamp,data,previous_hash)#Create a new Block with input data
        Blockk_Hash=Blockk.calc_hash() #After block is created , this method calculates its hash
        Blockk.insert_hash(Blockk_Hash) #After Hash is created , this method stores the hash in the block.
        
        if self.head is None: #This section is Transversing through the Blockchain to insert the Block at end of Blockchain
            self.head=Blockk
        else:
            iterator_block=self.head
            while iterator_block.next:
                iterator_block=iterator_block.next_hash
            iterator_block.next_hash=Blockk
        return Blockk

#Test Case 1(normal block)
first_time_stamp=datetime(2020,10,16,9,15,20,0,tzinfo=pytz.utc) #Defining First Block's timestamp
Blockchain=Blockchain()
Block1=Blockchain.Insert_Block(first_time_stamp,"500 dollars paid","Random Entry") #Inserting First Block
Block1_hash=Block1.calc_hash()
Block1.insert_hash(Block1_hash)
print(Block1.timestamp,Block1.data,Block1.current_hash)#expect the entry input
print("//////////////////")
#Test Case 2 (same timestamp block)
second_time_stamp=datetime(2020,10,16,9,15,20,0,tzinfo=pytz.utc) 
Block2=Blockchain.Insert_Block(second_time_stamp,"100 dollars paid",Block1.current_hash) 
Block2_hash=Block2.calc_hash()
Block2.insert_hash(Block2_hash)
print(Block2.timestamp,Block2.data,Block2.current_hash,Block2.previous_hash==Block1.current_hash ) #expect the entry input and True
print("//////////////////")
#Test Case 3(empty block)
Third_time_stamp=None 
Block3=Blockchain.Insert_Block(Third_time_stamp,None,Block2.current_hash) 
Block3_hash=Block3.calc_hash()
Block3.insert_hash(Block3_hash)
print(Block3.timestamp,Block2.data,Block3.current_hash,Block3.previous_hash==Block1.current_hash)#expect entry input and False
print("//////////////////")






  
    
        
        
        
        

