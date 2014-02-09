from function import *

iparam_1 = SciInput('Dimension 1', 'x')                                
iparam_2 = SciInput('Dimension 2', 'y')                                
oparam = SciOutput('Length', 'l')
paramset = SciParamSet(iparam_1, iparam_2, oparam)
test_summary = "This is a function"
test_description = "This function does things.\n\nAnd Stuff."
test_credit = "Copyright (C) 2013 A. Person"
test_body = "l = sqrt(x^2 + y^2)"
test_fun = SciFun(
		'test_function',
		paramset,
		test_summary,
		test_description,
		test_credit,
		test_body
		)

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

def test_summary():
	assert test_fun.summary == "This is a function" 

def test_description():
	assert test_fun.description == "This function does things.\n\nAnd Stuff."

def test_usage():
	string = "[l] = test_function(x, y)"
	assert test_fun.usage == string

def test_parameters():
	assert isinstance(test_fun.parameters, SciParamSet)

def test_declaration():
	string = "function [l] = test_function(x, y)"
	assert test_fun.declaration == string

def test_body():
	assert test_fun.body == 'l = sqrt(x^2 + y^2)'
