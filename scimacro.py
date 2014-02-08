#Copyright (C) 2013  A. Corrie                                         
#                                                                      
#This program is free software: you can redistribute it and/or modify  
#it under the terms of the GNU General Public License as published by  
#the Free Software Foundation, either version 3 of the License, or     
#(at your option) any later version.                                   
#                                                                      
#This program is distributed in the hope that it will be useful,       
#but WITHOUT ANY WARRANTY; without even the implied warranty of        
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         
#GNU General Public License for more details.                          
#                                                                      
#You should have received a copy of the GNU General Public License     
#along with this program.  If not, see [http://www.gnu.org/licenses/]

class SciMacro(object):
	"""Scilab Macro encapsulation.

	Encapsulates information sufficient for a top-level description of
	a single-file Scilab macro skeleton including:

	  - Licence
	  - Credits
	  - Functions

	"""
	def __init__(self, name):
		self._name = name
	
	@property
	def name(self):
		"""Name of Scilab macro.

		This is also the default filename.

		"""
		return self._name
