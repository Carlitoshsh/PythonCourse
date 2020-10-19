import unittest

def suma(num1, num2):
    return num1+num2

class CajaNegraTest(unittest.TestCase):
    def test_suma(self):
        num_1 = 12
        num_2 = 2

        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, 14)
        self.assertGreater(resultado, 13)

if __name__ == '__main__':
    unittest.main()