from shellOperationTesting import ShellOperations

class TestForShellOperations(object):
	def __init__(self):
		self.shell =  ShellOperations()
		self.line = ""
		self.line_test = "abc"
		self.empty = [""]
		
	def do_CurTest(self):
		assert os.getcwd()==self.shell.do_cur(self.line)
		return True
	
	def testForEmptyLine(self):
		assert self.empty[0] == self.shell.checkiflineisEmpty(self.line)
		return True
	
	def testForlineNotEmpty(self):
		assert self.shell.checkiflineisEmpty(self.line)!=self.empty[0]
		return True
	
		


T = TestForShellOperations()
print(T.testForlineNotEmpty())
print(T.testForEmptyLine())
