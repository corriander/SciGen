#Copyright (C) 2014  A. Corrie                                         
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

class SciFun(object):
	"""Scilab function encapsulation.

	Encapsulates information sufficient for a top-level description of
	a single Scilab function skeleton including:

	  - Simple documentation block.
	  - List of parameters
	"""
	def __init__(self, name, credit=None):
		self._name = name
		self._credit = credit

	def __repr__(self):
		return "SciFun('%s')" % self.name

	def __str__(self):
		string = []
		string.append("SciFun Object: %s" % self.name)
		return "\n".join(string)
	
	@property
	def name(self):
		"""Name of Scilab function."""
		return self._name

	@property
	def credit(self):
		"""Credit string (frontmatter)."""
		return self._credit

class SciParam(object):
	"""Scilab Parameter encapsulation.

	Encapsulates information sufficient for a description of a single
	Scilab function parameter including:

	  - Variable name
	  - Variable
	
	"""
	def __init__(self, name, var):
		self._name = name
		self._var = var
	
	def __repr__(self):
		return "SciParam('%s', '%s')" % (self.name, self.var)

	def __str__(self):
		return "Parameter: %s, %s" % (self.name , self.var)

	@property 
	def name(self):
		"""Human-readable name of Scilab function parameter."""
		return self._name

	@property
	def var(self):
		"""Scilab function parameter name."""
		return self._var
