class Errors(Exception):
	def not_file(self):
		return "not a file"
	
	def directory_not_found(self):
		return "directory not found"
	
	def no_directory_found(self):
		return "can't find directory"
	
	def end_of_directory(self):
		return "end of the file directory"
	
	def colour_not_found(self):
		return "colour not found"
	
	def empty_line(self):
		return "cannot take a empty line"
	
	def no_internet_connection(self):
		return "no internet connection"
	
	def no_package(self):
		return "no package of the name"
	
