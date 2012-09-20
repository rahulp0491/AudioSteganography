#! /usr/bin/python

import os
import sys
import bit
import struct
import wave as W

class StegFile:
	"""Class for output file which contains the hidden message"""
	def __init__ (self, outFile, paramTuple):
		"""Opens/Creates output file and sets all the params as of the source file"""
		self.file = W.open (outFile, 'wb')
		self.file.setparams (paramTuple)
	
	def writeFile (self, numFrames, hid):
		"""Writes new message-hidden data into the output file"""
		for byte in range (0, 4*numFrames):
			pack = struct.pack ('h', hid [byte])
			self.file.writeframes (pack [:1])
	
	def closeStegFile (self):
		"""Closes the audio file"""
		self.file.close ()

class AudioFile:
	"""Class for source wave file"""
	def __init__ (self, inFile):
		"""Opens the source wave file"""
		self.file = W.open (inFile, 'rb')
	
	def getNumFrames (self):
		"""Gets the number of frames in the source wave file
		1 Frame = 4 Bytes"""
		return self.file.getnframes ()
	
	def getData (self):
		"""Gets non-readable data from the source wave file"""
		return self.file.readframes (self.getNumFrames())
	
	def getParamTuple (self):
		"""Returns all the wave parameters as a tuple (immutable)"""
		return self.file.getparams ()
	
	def closeAudioFile (self):
		"""Closes the audio file"""
		self.file.close ()

class StegMsg:
	"""Class for the text message"""
	def __init__ (self):
		"""Initializes the message"""
		self.msg = raw_input ("Enter Message: ")
	
	def msgLen (self):
		"""Gets the length of the message"""
		return len (self.msg)

def dataToOrd (data):
	"""Returns a list of integer ordinals of the data"""
	return [ord (byte) for byte in data]

def hideMsg (text, ordData):
	"""Sets the starting byte; 0-43 bytes are used for wave headers
	Writes new steganofied data and returns a list of bytes (integer ordinal form)"""
	startByte = 44
	bitLen = 8
	msgLen = text.msgLen ()
	byteNum = startByte
	ordText =  dataToOrd (text.msg)
	
	for byte in range (0, msgLen):
		for b in range (0, bitLen):
			ordData [byteNum] = bit.changeLSB (ordData [byteNum], bit.getbit (ordText [byte], b))
			byteNum = byteNum + 1
	
	return ordData

if __name__ == '__main__':
	"""Main routine"""
	fileName = sys.argv[1]
	if os.path.isfile (fileName):
		pass
	else:
		raise IOError ('File does not exists')
	
	inFile = AudioFile (fileName)
	inData = inFile.getData ()
	ordData =  dataToOrd (inData)
	text = StegMsg ()
	
	hidObj = hideMsg (text, ordData)
	
	outfilename = sys.argv[2]
	
	try:
		outFile = StegFile (outfilename, inFile.getParamTuple ())
	except:
		raise IOError ('File does not exists')
	
	outFile.writeFile (inFile.getNumFrames (), hidObj)

