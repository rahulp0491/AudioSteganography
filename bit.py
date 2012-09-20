#! /usr/bin/python

def getbit( integer, pos ):
	"""This returns the bit at given position"""
	value=(integer & (1 << pos) != 0)
	if value==False:
		return 0
	else:
		return 1

def changeLSB(integer, bit):
	"""This replaces the LSB of integer with given bit"""
	return ((integer & ~1) | bit)


def makeBin (byte): 
	"""This returns a 8-bit string of the bin representation of byte"""
	bitlen = 8;
	binpart = byte [2:]
	restlen = bitlen - len (binpart)
	for i in range (0, restlen):
		binpart = "0" + binpart
	return binpart
