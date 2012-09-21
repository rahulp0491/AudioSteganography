#! /usr/bin/python

def getbit (integer, pos):
	"""This returns the bit at given position"""
#	Getting the bit given its position
	value = (integer & (1 << pos) != 0)
	if value == False:
		return 0
	else:
		return 1

def changeLSB (integer, bit):
	"""This replaces the LSB of integer with given bit"""
	return ((integer & ~1) | bit)

# >>Not currently in use 
def makeBin (byte): 
	"""This returns a 8-bit string of the bin representation of byte"""
	bitlen = 8;
	binpart = byte [2:]
	restlen = bitlen - len (binpart)
	for i in range (0, restlen):
		binpart = "0" + binpart
	return binpart

def dataToOrd (data):
	"""Returns a list of integer ordinals of the data"""
	return [ord (byte) for byte in data]

def hideMsg (text, ordData):
	"""Sets the starting byte; 0-43 bytes are used for wave headers
	Writes new steganofied data and returns a list of bytes (integer ordinal form)"""
	
#	First 44 bytes are wave headers
	startByte = 44
	bitLen = 8
	
#	Getting length of text msg
	msgLen = text.msgLen ()
	byteNum = startByte
	
#	Converting string into ord of data
	ordText =  dataToOrd (text.msg)
	
	for byte in range (0, msgLen):
		for b in range (0, bitLen):
#			Replacing LSB with desired bit
			ordData [byteNum] = changeLSB (ordData [byteNum], getbit (ordText [byte], b))
			byteNum = byteNum + 1
	
	return ordData
