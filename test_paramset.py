from function import SciParamSet, SciParam, SciInput, SciOutput

param = SciParam('Parameter', 'p')
iparam_1 = SciInput('Dimension 1', 'x')
iparam_2 = SciInput('Dimension 2', 'y')
oparam = SciOutput('Length', 'l')

class TestEmpty:
	
	paramset = SciParamSet()

	def test_init_empty(self):
		assert not self.paramset # Pythonic, not explicit. Test boolean value.
	
class TestOneParam:
	
	paramset = SciParamSet(param)

	def test_name(self):
		assert self.paramset[0].name == 'Parameter'

	def test_var(self):
		assert self.paramset[0].var == 'p'
	
	def test___getitem__(self):
		assert self.paramset['p'] == param

class TestMultiParam:

	paramset = SciParamSet(iparam_1, iparam_2, oparam)

	def test_names(self):
		assert self.paramset[0].name == 'Dimension 1'
		assert self.paramset[2].name == 'Length'

	def test_vars(self):
		assert self.paramset[0].var == 'x'
		assert self.paramset[2].var == 'l'

	def test_composition(self):
		assert self.paramset.stat() == {
				'SciInput' : ['x', 'y'],
				'SciOutput' : ['l']
				}