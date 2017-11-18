
import os
import cmd
import time
import datetime
import subprocess
from errorHandling import Errors
from  subprocess import check_output

class ShellOperations(cmd.Cmd ,object):
	
	def __init__(self):
		self._e = Errors()#instance of errors
			
	
	def do_cur(self,line):
		"""current returns current working directory"""
		print os.getcwd()#prints the current working directory 
		
	def do_tod(self):
		""" tod return current time and date"""
		unix_time = time.time()#gets unix time stamp
		date_conversion = '%Y-%m-%d %H:%M:%S'#converting unix time stamp
		return datetime.datetime.fromtimestamp(unix_time).strftime(date_conversion)#printing date and time in format of '%Y-%m-%d %H:%M:%S'
	
	def _checkiflineisEmpty(self,line):
		empty = ['']
		return line == empty[0]
	
	def _formattingCurrentWorkingDirectory(self):
		files = self._current_return()
		files = files.split('/')
		files.remove(files[0])
		return files
		
	def do_cdir(self,line):
		""" cdir changes the file directory"""
		files = self._formattingCurrentWorkingDirectory()
		count = len(files)-1
		if(self._checkiflineisEmpty(line)):
			try:
				raise Exception(self._e.empty_line())
			except Exception as err:
				print(self._e.empty_line())
		elif(line in  files):
			while(True):
				self.do_bdir(line)
				count-=1
				find  = files.index(line)
				if(find == count):
					break
		elif(line not in files):
			try:
				os.chdir(line)
			except Exception as err:
				print(self._e.no_directory_found())
	
			
	def get_home(self):
		""" funcution to check if in home directory"""
		return os.getcwd()=="home"	
	
	def _checkIfFile(self,line):
		return os.path.isfile(line)
		
	def _current_return(self):
		""" returns current directory
		function used to get back to home"""
		return os.getcwd()
	
	
	
	def _commandsTxtStorage(self):
		File = open("Commands.txt",'r')
		commands = []
		new_list = []
		for information in File:
			commands.append(information.split(':'))
		for commands_information in commands:
			for commands_Information in commands_information:
				new_list.append(commands_Information)
		return  new_list
	
	
	
	
	def do_help(self,line):
		File = open("Commands.txt","r")
		commands = self._commandsTxtStorage()
		find = int 
		if(line == "all"):
			for information in File:
				print(information.strip())
		elif(line != "all"):
			try:
				find = commands.index(line)
				print(commands[find+1])
			except Exception as err:
				print(self._e.no_command())
	
	def do_cat(self,line):
		cats = []
		exec("x = 1")
		if(line == ""):
			while(True):
				user_cat = raw_input(">>")
				if(user_cat == 'b'):
					break
		if(">" in line):
			try:
			 line[2] = cats
			 while(True):
				 user_cat = raw_input(">>")
				 line[2].append(user_cat)
				 if(user_cat == "b"):
					 break
			except Exception as err:
				print(self._e.not_catable())
		
		
	
	
	def do_h(self,line):
		""" h gets to home directory"""
		files = self._formattingCurrentWorkingDirectory()
		find  = files.index('home')#find the index value of home
		counter = len(files)
		while(True):#while true
			self.do_bdir(line)#calls the bdir method 
			counter-=1#decerement count by one each time
			if(counter==find):
				break
		self.do_cdir('home')#changes the directory
	
	def do_get(self,line):
		""" get packages"""
		if(self._checkiflineisEmpty(line)):#if line is empty 
			try:
				raise Exception(self._e.empty_line())
			except Exception as err:
				print self._e.empty_line()
		if(self._checkiflineisEmpty(line)==False):#if true
			try:
				connection = check_output("ping -c 1 www.google.com",shell=True)
				if(line  == "update"):#checks if line is update then update
					os.system("sudo apt-get update")
				else:# else try install line 
					os.system("sudo apt-get install %s"%line)
			except subprocess.CalledProcessError as  err:
				print err
		
	def do_cwl(self,line):
		if(self._checkIfFile(line)):#checks if line is a file
			File = open(line).read()#opens file for read
			File = File.splitlines()#splits files at new lines
			count  = len(File)#counts len of file
			print count
		else:
			#error handling if line is not a file
			try:
				raise Exception(self._e.not_file())
			except Exception as Err:
				print Err
			
	
	def do_cl(self): 
		""" cl clears the terminal screen"""
		os.system('clear')#clears the terminal screen 
		
	def do_bl(self,line):
		"""bl lists files which are in the current working directory"""
		files = os.listdir(os.getcwd())#stores current directory and list of files in working direcotry 
		print(files)#lists the directory
			
	def do_bll(self):
		"""bll lists access of files and files of the current working directory"""
		files = os.listdir(os.getcwd())#gets the list of directorys in current
		for x in range(len(files)):
			#refactor
			if(os.access(files[x],os.R_OK == True)and(os.access(files[x],os.W_OK)==True) and(os.access(files[x],os.X_OK)==True)):
				print files[x] +"R_W_X"
			elif(os.access(files[x],os.R_OK)==False)and(os.access(files[x],os.W_OK)==False)and(os.access(files[x],os.X_OK)==True):
				print files[x]+"no access"
			elif(os.access(files[x],os.R_OK)==True)and(os.access(files[x],os.W_OK)==False)and(os.access(files[x],os.X_OK)==False):
				print files[x]+"R"
			elif(os.access(files[x],os.R_OK)==False)and(os.access(files[x],os.W_OK)==True)and(os.access(files[x],os.X_OK)==True):
				print files[x]+"R"
			elif(os.access(files[x],os.R_OK)==False)and(os.access(files[x],os.W_OK)==False)and(os.access(files[x],os.X_OK)==True):
				print files[x] + "X"
			elif(os.access(files[x],os.R_OK)==True)and(os.access(files[x],os.W_OK)==True)and(os.access(files[x],os.X_OK)==False):
				print files[x]+" " + "R_W"
			elif(os.access(files[x],os.R_OK)==False)and(os.access(files[x],os.W_OK)==True)and(os.access(files[x],os.X_OK)==True):
				print files[x]+ +" "+"X_W"
			elif(os.access(files[x],os.R_OK)==True)and(os.access(files[x],os.W_OK)==True)and(os.access(files[x],os.X_OK)==False):
				print files[x]+"R_W"
			elif(os.access(files[x],os.R_OK)==False)and(os.access(files[x],os.W_OK)==True)and(os.access(files[x],os.X_Ok)==False):
				print files[x]+"W"
	
			
	def do_show(self,line):
		""" show files to user press Q to leave"""
		if(self._checkIfFile(line)):#checks if line is a file
			File = open(line).read()#opens and reads files 
			os.system('less %s'%line)#calls the less linux command
		else:#else throw error 
			try:
				raise Exception(self._e.not_file())
			except Exception as err:
				print self._e.not_file() 
				
	def do_process(self,line):
		print(os.system("-ps"))
		
				
	def do_cw(self,line):
		""" cw counts words of a file"""
		count = 0#count variable
		if(self._checkIfFile(line)):#checks if line is a file
			files = open(line).read()#opens line file for read
			for x in files.split():#splits at whitespaces
				count+=1#increments count by each iteration
			print count #prints count
		else:
			try:
				raise Exception(self._e.not_file())#raise not file exception 
			except Exception as err:#catch error
				print self._e.not_file()#prints error in terminal

			
	def do_bdir(self,line):
		"""bdir moves back one directory"""
		os.chdir(os.path.pardir)#moves back one directory in linux system 



