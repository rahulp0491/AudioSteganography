import os
import sys
import stegLSB
import bit

def Main ():
	"""Main routine"""
#	Get source file path
	fileName = sys.argv[1]
	if os.path.isfile (fileName):
		pass
	else:
		raise IOError ('File does not exists')
	
#	Initializing source audio file
	inFile = stegLSB.AudioFile (fileName)
	
#	Getting data from source audio file as a string of bytes
	inData = inFile.getData ()
	
#	Converting data into list of readable integer ordinal format
	ordData =  bit.dataToOrd (inData)
	
#	Initializing text message to be embedded
	text = stegLSB.StegMsg ()
	
#	Hiding text message into the list ord data 
	hidObj = bit.hideMsg (text, ordData)
	
#	Getting output file path
	outfilename = sys.argv[2]
	try:
		outFile = stegLSB.StegFile (outfilename, inFile.getParamTuple ())
	except:
		raise IOError ('File does not exists')
	
#	Writing new embedded data into a new file (filename given earlier)
	outFile.writeFile (inFile.getNumFrames (), hidObj)

if __name__ == '__main__':
	"""Calling Main ()"""
	Main ()
