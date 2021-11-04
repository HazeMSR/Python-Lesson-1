import pytest
from src.poo import Pantalla

def test_one():
	assert True

def test_two():
	raise Exception

@pytest.mark.parametrize('arg1', [
	'ana',
	'anitalavalatina',
	'ojo',
	'appa',
	'yohagoyogahoy',
	'tunalatuna',
	'tigretono',
	'keymonkey',
	'loquesea',
	'mana'
])
def test_with_parameter(arg1):
	for i in range( int(len(arg1) / 2) ):
		print(i)
		if arg1[i] != arg1[ len(arg1) - 1 - i]: #arg1[3] , arg[2]
			raise Exception

	assert True


def test_pantalla():
	tv_samsung = Pantalla(999.99, 3000, 500, 1980)
	assert tv_samsung.get_voltaje() == 500