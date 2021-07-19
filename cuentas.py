import unittest

class TestCuentas(unittest.TestCase):

    def TestCuentaCreada(self):
        cuenta = 12345
        self.assertEqual(cuenta, 12345)
