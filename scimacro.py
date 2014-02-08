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
	def __init__(self, name, credit=None, license=None):
		self._name = name
		self._credit = credit
		self._license = license

	def __repr__(self):
		return "SciMacro('%s')" % self.name

	def __str__(self):
		string = []
		string.append("SciMacro Object: %s" % self.name)
		return "\n".join(string)
	
	@property
	def name(self):
		"""Name of Scilab macro.

		This is also the default filename.

		"""
		return self._name

	@property
	def credit(self):
		"""Credit string (frontmatter)."""
		return self._credit

	@property
	def license(self):
		"""License string (frontmatter)."""
		return self._license
