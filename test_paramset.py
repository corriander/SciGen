from function import SciParamSet, SciParam, SciInput, SciOutput

param = SciParam('Parameter', 'p')
iparam_1 = SciInput('Dimension 1', 'x')
iparam_2 = SciInput('Dimension 2', 'y')
oparam = SciOutput('Length', 'l')

def test_init_empty():
	paramset = SciParamSet()
	assert not paramset # Pythonic, not explicit. Test boolean value.

class TestOneParam:
	
	paramset = SciParamSet(param)

	def test_name(self):
		assert self.paramset[0].name == 'Parameter'

	def test_var(self):
		assert self.paramset[0].var == 'p'

class TestMultiParam:

	paramset = SciParamSet(iparam_1, iparam_2, oparam)

	def test_names(self):
		assert self.paramset[0].name == 'Dimension 1'
		assert self.paramset[2].name == 'Length'

	def test_vars(self):
		assert self.paramset[0].var == 'x'
		assert self.paramset[2].var == 'l'
