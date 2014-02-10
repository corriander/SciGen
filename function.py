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
	def __init__(self,
 			name,
 			parameters,
 			summary,
 			description=None,
 			credit=None,
			body=None
			):
		self._name = name
		self._parameters = parameters
		self._summary = summary
		self._description = description
		self._credit = credit
		self._body = body
		# generate declaration
		self.declaration = self._generate_declaration()

	def __repr__(self):
		return "SciFun('%s')" % self.name

	def __str__(self):
		doctxt = [self.summary]
		doctxt.append('')
		if self.usage:
			doctxt.append('Usage')
			doctxt.append('')
			doctxt.append(self.usage)
			doctxt.append('')
			doctxt.append('')
		doctxt.append(self.parameters)
		if self.description:
			doctxt.append('Description')
			doctxt.append('----------')
			doctxt.append(self.description)
			doctxt.append('')
			doctxt.append('')
		if self.credit:
			doctxt.append('Credits')
			doctxt.append('-------')
			doctxt.append('')
			doctxt.append(self.credit)
			doctxt.append('')
			doctxt.append('')
		doctxt = ["// %s" % line for line in doctxt]
		
		string = [self.declaration]
		string.extend(doctxt)
		string.append(self.body)
		string.append('')
		string.append('endfunction')
		return "\n".join(string)

	def _generate_declaration(self):
		"""Generate function declaration syntax."""
		components = ["function "]
		pstat = self.parameters.stat()
		components.append(str(pstat['SciOutput']).replace("'",""))
		components.append(" = ")
		components.append(self.name)
		components.append(str(tuple(pstat['SciInput'])).replace("'",""))
		return "".join(components)
	
	@property
	def name(self):
		"""Name of Scilab function.
		
		This is a mandatory attribute.
		
		"""
		# At some point, some sort of (configurable) naming rules
		# could be enforced.
		return self._name

	@property
	def parameters(self):
		"""Parameter set.
		
		This is a mandatory attribute and should be SciParamSet, even
		if it's empty.
		
		"""
		return self._parameters


	@property
	def summary(self):
		"""Summary of function.
		
		This is a mandatory component of the comment block.
		
		"""
		return self._summary
	
	@property
	def description(self):
		"""Detailed description of function."""
		return self._description

	@property
	def usage(self):
		"""Usage documentation."""
		# This is obviously currently dumb.
		return self.declaration.lstrip('function ')

	@property
	def credit(self):
		"""Credit string (frontmatter)."""
		return self._credit

	@property
	def body(self):
		"""Function body."""
		return self._body

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

	def __str__(self):
		stat = self.stat()
		string = []
		if stat['SciParam']:
			string.append('Modified Parameters')                           
			string.append('-------------------')                           
			string.append('These are returned to previous scope.')         
			self._add_text(string, stat['SciParam'])
		if stat['SciOutput']:
			string.append('Outputs')
			string.append('-------')
			self._add_text(string, stat['SciOutput'])
		if stat['SciInput']:
			string.append('Inputs')
			string.append('------')
			self._add_text(string, stat['SciInput'])
		return "\n".join(string)

	def _add_text(self, lsof_str, keys):
		# Used by __str__ to take some repetition out. Takes a list of
		# keys and adds the string representation to the lsof_str
		# parameter.
		lsof_str.append('')
		for o in keys:
			lsof_str.append(str(self[o]))
			lsof_str.append('')
		lsof_str.append('')
		return lsof_str
	
	def stat(self):
		"""Return variables in different classes of parameter."""
		dd = defaultdict(list)
		for item in self:
			dd[item.__class__.__name__].append(item.var)
		return dd

class SciParam(object):
	"""Scilab Parameter encapsulation.

	Encapsulates information sufficient for a description of a single
	Scilab function parameter including:

	  - Variable name
	  - Variable
	  - Description
	  - (Scilab) Type
	  - Size
	
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
		if self.description:
			text.append("Description : %s" % self.description)
		if self.scitype:
			text.append("Type        : %s" % self.scitype)
		if self.size:
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
	
class SciOutput(SciParam):
	"""Scilab function output parameter encapsulation."""
	def __init__(self, name, var):
		SciParam.__init__(self, name, var)
