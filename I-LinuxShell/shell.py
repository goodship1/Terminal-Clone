""" imports"""
from __future__ import unicode_literals
from prompt_toolkit import prompt
from shellFuncutions import ShellOperations
import cmd
import os 


class InteractiveShell(cmd.Cmd,object):
	
	def __init__(self):
		self.interactive()


	def interactive(self):
		""" interactive shell"""
		variables = dict()
		self.op = ShellOperations()
		line = ""
		operators = ["+","-","*",'**','<',">"]
		returnShellMethods = {"tod":self.op.do_tod()}
		listofprintMethods = ["bll","h","cur","bdir","blue","bl","sh",'wc','get','cwl','cdir']
		while(True):#excute while True
			enter_commands = prompt(">>")
			if(enter_commands in returnShellMethods.keys()):
				print(returnShellMethods[enter_commands])
			if(enter_commands not in returnShellMethods.keys())and(enter_commands not in listofprintMethods):
				try:
					exec(enter_commands)
				except Exception as Err:
					print(Err)
			if(enter_commands == 'cl'):
				self.op.do_cl()
			if(enter_commands == "exit"):#if enter_commands equal to exit then exit interactive shell
				os.system("exit")
			if(len(enter_commands)>1)and(enter_commands[1] in operators):
				try:
					print(eval(enter_commands))
				except Exception as err:
					print(err)
			if(enter_commands in listofprintMethods)and(enter_commands == "bll"):
				self.op.do_bll()
			if(enter_commands == "h")and(enter_commands in listofprintMethods):
				self.op.do_h(line)
			if(enter_commands == "cur")and(enter_commands in listofprintMethods):
				self.op.do_cur(line)
			if(enter_commands =="bdir") and(enter_commands in listofprintMethods):
				self.op.do_bdir(line)
			if(enter_commands =='bl')and(enter_commands in listofprintMethods):
				self.op.do_bl(line)
			if(enter_commands  == "sh")and(enter_commands in listofprintMethods):
				File = raw_input("enter file name: ")
				self.op.do_show(File)
			if(enter_commands == "wc") and(enter_commands in listofprintMethods):
				File = raw_input("enter file name :")
				self.op.do_cw(File)
			if(enter_commands == 'get')and(enter_commands in listofprintMethods):
				File = raw_input("enter software to get: ")
				self.op.do_get(File)
			if(enter_commands =="cwl") and(enter_commands in listofprintMethods):
				File = raw_input("enter file name :")
				self.op.do_cwl(File)
			if(enter_commands == "cdir")and(enter_commands in listofprintMethods):
				File = raw_input("enter directory :")
				self.op.do_cdir(File)

interacive = InteractiveShell()
