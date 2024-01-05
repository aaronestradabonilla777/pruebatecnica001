import unittest
from src import module1

class TestModule1(unittest.TestCase):

    def test_function1(self):
        # Supongamos que function1 es una función en module1 que toma dos números y devuelve su suma
        result = module1.function1(1, 2)
        self.assertEqual(result, 3)

    def test_function2(self):
        # Supongamos que function2 es otra función en module1 que toma una cadena y la devuelve en mayúsculas
        result = module1.function2('test')
        self.assertEqual(result, 'TEST')

if __name__ == '__main__':
    unittest.main()