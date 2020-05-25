# -*- enconding: utf-8 -*-

import c_parser 
class ideADK():
	def __init__(self,cod):
		self.data=cod
		
	def compilar(self):
		c_parser.VERBOSE = 0
		try:
			c_parser.parser.parse(self.data, tracking=True)
			print ('[ok]')
			return True

		except:
			print ('[error]')
			return False


	
