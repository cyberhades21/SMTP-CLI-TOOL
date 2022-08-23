class Argument:
	def __init__(self,args):
		self.commands = []
		self.options = []
		self.optionvalues = { }
		self.args = args

		for arg in self.args:
			if '-' in arg:
				#Option OR Option With Values
				if '=' in arg:
					pair=arg.split('=')
					self.optionvalues[pair[0]] = pair[1] #appending the key value pairs to a dictionary
					self.options.append(pair[0])
					#it is option with values
					
				else:
					#its an option
					self.options.append(arg)
			else:
				#its a command
				self.commands.append(arg)
				
	def has_options(self,options):
		userOptions = set(self.options)
		reqired = set(options)
		return list(reqired & userOptions)
	

		
	