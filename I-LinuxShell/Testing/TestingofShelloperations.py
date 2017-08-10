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

def testingdo_showErrorHandling():
	assert shell.do_show('adadada') == "not a file"

def testingofdo_cur():
	current = os.getcwd()
	assert current ==  shell.do_cur(line='')

def testingDo_h():
	assert shell.do_h(line="")==True

def testingdo_geterrorHandling(line = ""):
	#testing when line is empty
	assert shell.do_get(line) ==  "cannot take a empty line"

def testingdo_get(line = 'update'):
	#testing do_ get update
	assert shell.do_get(line)==True

def testingdo_get(line = "python"):
	#testing if we can find another package 
	assert shell.do_get(line)==True

def testingdo_bl():
	files = os.listdir(os.getcwd())
	assert files == shell.do_bl(line ="")

def testingdo_cdir(line = ""):
	#testing do_cdir with empty line 
	#should return error handling
	assert shell.do_cdir(line) ==  "cannot take a empty line"


