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

from collections import defaultdict

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

class SciParamSet(list):
	"""Set of Scilab function parameters.
	
	Paradoxically, Scilab functions don't actually *need* parameters.
	Although this might be considered an abuse of the language there
	are valid reasons to use parameterless functions (especially when
	trying to emulate OOP principles). It therefore makes sense for an
	empty set of parameters to be possible.
	
	"""
	def __init__(self, *args):
		for item in args:
			self.append(item)
	
	def __getitem__(self, key):
		if isinstance(key, int):
			return tuple(self)[key]
		for item in self:
			if item.var is key:
				return item
		raise KeyError, "Variable '%s' not in set." % key
	
	def stat(self):
		"""Return variables in different classes of parameter."""
		dd = defaultdict(list)
		for item in self:
			dd[item.__class__.__name__].append(item.var)
		return dict(dd)

class SciParam(object):
	"""Scilab Parameter encapsulation.

	Encapsulates information sufficient for a description of a single
	Scilab function parameter including:

	  - Variable name
	  - Variable
	
	"""
	def __init__(self, name, var, 
			description=None,
			scitype=None,
			size=None
			):
		self._name = name
		self._var = var
		self._description = description
		self._scitype = scitype
		self._size = size
	
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
		text.append("Size        : %s" % list(self.size))
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

	@property
	def size(self):
		"""Size of variable as reported by Scilab's `size()`"""
		return self._size

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
