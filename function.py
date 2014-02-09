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
	def __init__(self, name, var, description=None, scitype=None):
		self._name = name
		self._var = var
		self._description = description
		self._scitype = scitype
	
	def __repr__(self):
		return "%s('%s', '%s', kwargs)" % (
				self.__class__.__name__,
				self.name,
				self.var
				)

	def __str__(self):
		text = ["%s - %s" % (self.var, self.name)]
		text.append("Description : %s" % self.description)
		text.append("Type        : %s" % self.scitype)
		return "\n".join(text)

	@property 
	def name(self):
		"""Human-readable name of Scilab function parameter."""
		return self._name

	@property
	def var(self):
		"""Scilab function parameter name."""
		return self._var

	@property
	def description(self):
		"""Scilab function parameter description."""
		return self._description

	@property
	def scitype(self):
		"""Scilab data type as reported by Scilab's `typeof()`"""
		return self._scitype

class SciInput(SciParam):
	"""Scilab function input parameter encapsulation."""
	def __init__(self, name, var):
		SciParam.__init__(self, name, var)
	
	def __str__(self):
		return "Input: %s, %s" % (self.name, self.var)

class SciOutput(SciParam):
	"""Scilab function output parameter encapsulation."""
	def __init__(self, name, var):
		SciParam.__init__(self, name, var)
	
	def __str__(self):
		return "Output: %s, %s" %(self.name, self.var)


