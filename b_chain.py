#defining the 'block' data structure
class Block:
	#each block has 7 attributes
	#1 number of the block
	#2 what data is stored in this block?
	#3 pointer to the next block
	#4 The hash of this block (serves as a unique ID and verifites its integrity)
	#5 A nonce is a number only used once
	#6 store the hash (ID) of the previous block in the chain
	#7 timestamp
	blockNo = 0
	data = None
	next = None
	hash = None
	nonce = 0
	previous_hash = 0x0
	timestamp = datetime.datetime.now()
	
	def __init__(self,data):
		self.data = data
	
	#function to calculate 'hash' of a block
	def hash(self):
		h = hashlib.sha256()
		h.update(
		str(self.nonce).encode('utf-8') +
		str(self.data).encode('utf-8') +
		str(self.previous_hash).encode('utf-8') +
		str(self.timestamp).encode('utf-8') +
		str(self.blockNo).encode('utf-8')
		
		)