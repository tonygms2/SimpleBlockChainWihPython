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
	