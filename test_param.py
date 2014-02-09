from function import SciParam, SciInput, SciOutput

description = "This is a parameter."
param = SciParam('String', 's', description)

def test_param_name():
	assert param.name == 'String'

def test_param_var():
	assert param.var == 's'

def test_param_desc():
	assert param.description == "This is a parameter."

def test___repr__():
	assert repr(param) == "SciParam('String', 's')"

def test___str__():
	string = ["s - String"]
	string.append("Description : This is a parameter.")
	string = "\n".join(string)
	assert str(param) == string

iparam = SciInput('Boolean', 'b')

def test_iparam_name():
	assert iparam.name == 'Boolean'

def test_iparam_var():
	assert iparam.var == 'b'

def test_i__repr__():
	assert repr(iparam) == "SciInput('Boolean', 'b')"

def test_i__str__():
	assert str(iparam) == 'Input: Boolean, b'

oparam = SciOutput('Number', 'n')

def test_oparam_name():
	assert oparam.name == 'Number'

def test_oparam_var():
	assert oparam.var == 'n'

def test_o__repr__():
	assert repr(oparam) == "SciOutput('Number', 'n')"

def test_o__str__():
	assert str(oparam) == 'Output: Number, n'
