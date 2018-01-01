# code to copy file from another directory to present directory 

import shutil
import os

""" make sure input file already exist """
if os.path.isfile('test/sample.txt') is True:
	shutil.copy('test/sample.txt', os.getcwd())
else:
	print "Sorry! not able to copy file becuase file is not present in the provided path!"