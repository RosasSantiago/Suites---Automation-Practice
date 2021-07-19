# LIBRERÍAS
import unittest
import HtmlTestRunner

# ARCHIVOS DONDE SE ENCUENTRAN LOS TEST
import usuarios
import usuariosSearch
import cuentas

#Loader is suite

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(usuarios))
suite.addTests(loader.loadTestsFromModule(usuariosSearch))

#runner = unittest.TextTestRunner(verbosity=3)
#result = runner.run(suite)


HtmlTestRunner.HTMLTestRunner(combine_reports=True,
                                  report_name="Reporte santi",
                                  add_timestamp=False).run(suite)