from function import SciParamSet, SciParam, SciInput, SciOutput

param = SciParam('Parameter', 'p')
iparam_1 = SciInput('Dimension 1', 'x')
iparam_2 = SciInput('Dimension 2', 'y')
oparam = SciOutput('Length', 'l')

def test_init_empty():
	paramset = SciParamSet()
	assert not paramset # Pythonic, not explicit. Test boolean value.

def test_init_one_parameter_name():
	paramset = SciParamSet(param)
	assert paramset[0].name == 'Parameter'

def test_init_one_parameter_var():
	paramset = SciParamSet(param)
	assert paramset[0].var == 'p'

def test_init_multi_params():
	paramset = SciParamSet(iparam_1, iparam_2, oparam)
	assert paramset[0].name == 'Dimension 1'
	assert paramset[0].var == 'x'
	assert paramset[2].name == 'Length'
	assert paramset[2].var == 'l'



