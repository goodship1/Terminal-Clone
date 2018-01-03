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


def testingdo_show():
	assert shell.do_show('test.txt') == True


def testingofdo_cur():
	current = os.getcwd()
	assert current ==  shell.do_cur(line='')

def testingDo_h():
	assert shell.do_h(line="")==True



def testingdo_get(line = 'update'):
	#testing do_ get update
	assert shell.do_get(line)==True

def testingdo_get(line = "python"):
	#testing if we can find another package 
	assert shell.do_get(line)==True

def testingdo_bl():
	files = os.listdir(os.getcwd())
	assert files == shell.do_bl(line ="")




