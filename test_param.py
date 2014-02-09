from function import SciParam, SciInput, SciOutput

class TestParam:
	
	param = SciParam(
			'String',
			's',
			'This is a parameter.',
			'string',
			(1, 1)
			)

	partial_param = SciParam(
			'String',
			's'
			)

	def test_param_name(self):
		assert self.param.name == 'String'

	def test_param_var(self):
		assert self.param.var == 's'

	def test_param_desc(self):
		assert self.param.description == "This is a parameter."

	def test_param_scitype(self):
		assert self.param.scitype == "string"

	def test_param_size(self):
		assert self.param.size == (1, 1)

	def test___repr__(self):
		assert repr(self.param) == "SciParam('String', 's', kwargs)"

	def test___str__(self):
		string = ["s - String"]
		string.append("Description : This is a parameter.")
		string.append("Type        : string")
		string.append("Size        : [1, 1]")
		string = "\n".join(string)
		assert str(self.param) == string
	
	def test_partial__str__(self):
		assert str(self.partial_param) == "s - String"

class TestInput:

	param = SciInput('Boolean', 'b')

	def test_name(self):
		assert self.param.name == 'Boolean'

	def test_var(self):
		assert self.param.var == 'b'

	def test__repr__(self):
		assert repr(self.param) == "SciInput('Boolean', 'b', kwargs)"

	def test__str__(self):
		assert str(self.param) == 'Input: Boolean, b'

class TestOutput:

	param = SciOutput('Number', 'n')

	def test_name(self):
		assert self.param.name == 'Number'

	def test_var(self):
		assert self.param.var == 'n'

	def test__repr__(self):
		assert repr(self.param) == "SciOutput('Number', 'n', kwargs)"

	def test__str__(self):
		assert str(self.param) == 'Output: Number, n'
