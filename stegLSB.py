#! /usr/bin/python

import struct
import wave as W

class StegFile:
	"""Class for output file which contains the hidden message"""
	def __init__ (self, outFile, paramTuple):
		"""Opens/Creates output file and sets all the params as of the source file"""
		self.file = W.open (outFile, 'wb')
		
#		Setting file parameters
		self.file.setparams (paramTuple)
	
	def writeFile (self, numFrames, hid):
		"""Writes new message-hidden data into the output file"""
		for byte in range (0, 4*numFrames):
#			1 frame = 4 bytes; pack ord data to hex and write byte by byte
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






