import pytest
from  ErrorHandling import Errors
from shellOperationTesting import ShellOperations

"""global variables"""
shell = ShellOperations()
error  = Errors()
empty_line = " "
package = "python"
no_package = "wjgwjn"
File = "not_a_file"


# testing of the error handling for shellOperationTesting

def not_file():
	#testing of the handling of do_cw and and not file
	assert shell.do_cw('wgwgfwgg')== error.not_file()


def empty_line_test():
	#empty line test of do_cdir funcution and empty_line  error handling
	assert shell.do_cdir(empty_line) == error.empty_line()
	

def directory_not_found_testing():
	assert shell.do_cdir("not_a_file") == error.directory_not_found()



def no_internet_connection_testing():
	#testing of do_get with the error handling of no_internet_connection
	#for this test to pass internet had to disconnected
	assert shell.do_get(package) == error.no_internet_connection()

def empty_line_test_two():
	#testing of empty_line error handling for do_get funcution
	assert shell.do_get(line) == error.empty_line()

def no_package_test():
	#testing of  no_package error handling for do_get
	assert shell.do_get(no_package) == error.no_package()

def not_file_testing():
	#testing of the error handling for do_show with no the file 
	assert shell.do_show(File) == error.not_file()



