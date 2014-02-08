from function import SciFun

test_credit = "Copyright (C) 2013 A. Person"
test_fun = SciFun('test_function', test_credit)

def test_name():
	assert test_fun.name == 'test_function'

def test___str__():
	str_out = []
	str_out.append("SciFun Object: test_function")
	test_str = "\n".join(str_out)
	assert str(test_fun) == test_str

def test___repr__():
	assert repr(test_fun) == "SciFun('test_function')"

def test_credit():
	assert test_fun.credit == "Copyright (C) 2013 A. Person"
