import datetime
import hashlib
#defining the 'block' data structure
#defining the 'block' data structure
class Block:
    #each block has 7 attributes 
  
    #1 number of the block
    blockNo = 0
    #2 what data is stored in this block?
    data = None
    #3 pointer to the next block
    next = None
    #4 The hash of this block (serves as a unique ID and verifies its integrity)
    #A hash is a function that converts data into a number within a certain range. 
    hash = None
    #5 A nonce is a number only used once  
    nonce = 0
    #6 store the hash (ID) of the previous block in the chain
    previous_hash = 0x0
    #7 timestamp 
    timestamp = datetime.datetime.now()

    #We initialize a block by storing some data in it
    def __init__(self, data):
        self.data = data

    #Function to compute 'hash' of a block
    #a hash acts as both a unique identifier
    #& verifies its integrity
    #if someone changes the hash of a block
    #every block that comes after it is changed 
    #this helps make a blockchain immutable
    def hash(self):
        #SHA-256 is a hashing algorithm that
        # generates an almost-unique 256-bit signature that represents
        # some piece of text
        h = hashlib.sha256()
        #the input to the SHA-256 algorithm
        #will be a concatenated string
        #consisting of 5 block attributes
        #the nonce, data, previous hash, timestamp, & block #
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.data).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        #returns a hexademical string
        return h.hexdigest()
      
        ## SHOW DEMO 2, change data 

    def __str__(self):
        #print out the value of a block
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"
		
		
		#creating the blockchain now
	class Blockchain:
			
			diff = 20
			maxNonce = 2**32
			target = 2**(256-diff)
			
			block = Block("Genesis")
			
			head = block
			
			def add(self,block):
				block.previous_hash = self.block.hash()
				block.blockNo = self.block.blockNo + 1
				self.block.next = block
				self.block = self.block.next
			
			def mine(self,block):
				for n in range(self.maxNonce):
					if int(block.hash(),16) <= self.target:
						self.add(block)
						print(block)
						break
					else:
						block.nonce = block.nonce + 1

blockchain = Blockchain()

for n in range(10):
	blockchain.mine(block("Block " + str(n+1)))

while blockchain.head ! = None:
	print(blockchain.head)
	blockchain.head = blockchain.head.next

