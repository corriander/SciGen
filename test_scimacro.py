from scimacro import SciMacro

test_macro = SciMacro('test_macro')

def test_name():
	assert test_macro.name == 'test_macro'

def test___str__():
	str_out = []
	str_out.append("SciMacro Object: test_macro")
	test_str = "\n".join(str_out)
	assert str(test_macro) == test_str

def test___repr__():
	assert repr(test_macro) == "SciMacro('test_macro')"
