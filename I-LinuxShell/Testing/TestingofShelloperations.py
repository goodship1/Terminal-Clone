import pytest
from shellOperationTesting import ShellOperations
import os 

shell  = ShellOperations()

def testingchecklineisEmpty():
	line = " "
	shell.checkiflineisEmpty(line)==True

	
def testingformatCurrentWorkingDirectory():
	Files = os.getcwd()
	Files = Files.split('/')
	Files.remove(Files[0])
	assert Files ==  shell.formattingCurrentWorkingDirectory()
	
