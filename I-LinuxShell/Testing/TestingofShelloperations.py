from shellOperationTesting import ShellOperations
import os
class TestForShellOperations(object):
	def __init__(self):
		self.shell =  ShellOperations()
		self.line = ""
		self.line_test = "abc"
		self.empty = [""]
		self.current_format = self.shell.formattingCurrentWorkingDirectory()
		
		
	def do_CurTest(self):
		assert os.getcwd()==self.shell.do_cur(self.line)
		return True
	
	def testForEmptyLine(self):
		return self.empty[0] == self.shell.checkiflineisEmpty(self.line)
	
	def testForlineNotEmpty(self):
		assert self.shell.checkiflineisEmpty(self.line)!=self.empty[0]
		return True
	
	def testingCurrentdirectioryfileFormatting(self):
		Files = os.getcwd()
		Files = Files.split('/')
		Files.remove(Files[0])
		assert Files == self.shell.formattingCurrentWorkingDirectory()
		return True
	
	def testingErrorhandlingofEmptylinedoCdirMethod(self):
		return self.shell.do_cdir(self.line)== "cannot take a empty line"
	
	
	def testingchangeDirectorydirectory(self):
		pass
	
	def testingdo_bdir(self):
		back = os.chdir(os.path.pardir)
		assert back  == self.shell.do_bdir(self.line)
		return True
	
	def testingCheckIfFileisTrue(self):
		result = os.path.isfile('test.txt')
		assert result == self.shell.checkIfFile('test.txt')
		return True
	
	def testingCheckIfFilesIsFalse(self,files):
		result = os.path.isfile(files)
		assert result == self.shell.checkIfFile(files)
	

	
		
		

	
		


T = TestForShellOperations()
T.testingCheckIfFilesIsFalse('test.txt')
