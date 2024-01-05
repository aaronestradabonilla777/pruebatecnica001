import unittest
from src import module2

class TestModule2(unittest.TestCase):

    def test_function_in_module2(self):
        # Aquí puedes llamar a una función en module2 y verificar si el resultado es el esperado
        result = module2.some_function()
        self.assertEqual(result, 'expected result')

if __name__ == '__main__':
    unittest.main()