import unittest
import usuarios
import usuariosSearch
import cuentas


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(usuarios))
suite.addTests(loader.loadTestsFromModule(usuariosSearch))
suite.addTest(cuentas.TestCuentas("testCuentaCreada"))
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)