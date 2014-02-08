from function import SciParam

param = SciParam('String', 's')

def test_param_name():
	assert param.name == 'String'

def test_param_var():
	assert param.var == 's'

def test___repr__():
	assert repr(param) == "SciParam('String', 's')"

def test___str__():
	assert str(param) == 'Parameter: String, s'
