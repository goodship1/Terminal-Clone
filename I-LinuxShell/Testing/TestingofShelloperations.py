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

def testingcheckifFile():
	assert shell.checkIfFile('test.txt')==True

def testingreturnofdo_cw():
	assert shell.do_cw('test.txt') == 3

def testingErrorhandlingofdo_cw():
	assert shell.do_cw('wgwgfwgg')=="not a file"

def testingdo_show():
	assert shell.do_show('test.txt') == True
