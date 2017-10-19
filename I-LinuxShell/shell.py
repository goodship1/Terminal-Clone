""" imports"""
from __future__ import unicode_literals
import cmd
from prompt_toolkit import prompt
from shellFuncutions import ShellOperations
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.contrib.completers import WordCompleter
from keys import KeyBindings
from toolbar import ToolBar



class InteractiveShell(cmd.Cmd,object):
	
	def __init__(self):
		self.interactive()
	
	def get_title(self):
		return "i-linux"


	def interactive(self):
		""" interactive shell"""
		variables = dict()
		self.op = ShellOperations()
		self.bindings = KeyBindings() 
		line = ""
		self.toolBar = ToolBar()
		input_History = InMemoryHistory()
		operators = ["+","-","*",'**','<',">"]
		returnShellMethods = {"tod":self.op.do_tod()}
		listofprintMethods = ["bll","h","cur","bdir","bl","sh",'wc','get','cwl','cdir','man']
		linux_Commands = WordCompleter(listofprintMethods)
		
		
		while(True):#excute while True
			enter_commands = prompt(">>",history=input_History,key_bindings_registry=self.bindings.register,completer=linux_Commands,mouse_support = True,get_title = self.get_title,get_bottom_toolbar_tokens = self.toolBar.get_bottom_toolbar_tokens,style = self.toolBar.toolBarStyle)
			store = enter_commands
			store = store.split(" ")
			if(enter_commands in returnShellMethods.keys()):
				print(returnShellMethods[enter_commands])
			if(enter_commands not in returnShellMethods.keys())and(enter_commands not in listofprintMethods)and(store[0] not in listofprintMethods):
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
			if(store[0]  == "sh")and(store[0] in listofprintMethods):
				try:
					self.op.do_show(store[1])
				except Exception as err:
					self.op.do_show("")	
			if(store[0] == "wc") and(store[0] in listofprintMethods):
				try:
					self.op.do_cw(store[1])
				except Exception as err:
					self.op.do_cw("")
			if(store[0] == 'get')and(store[0] in listofprintMethods):
				try:
					self.op.do_get(store[1])
				except Exception as err:
					self.op.do_get("")

			if(store[0] =="cwl") and(store[0] in listofprintMethods):
				try:
					self.op.do_cwl(store[1])
				except Exception as err:
					self.op.do_cwl("")
			if(store[0] == "cdir")and(store[0] in listofprintMethods):
				try:
					self.op.do_cdir(store[1])
				except Exception as err:
					self.op.do_cdir("")
