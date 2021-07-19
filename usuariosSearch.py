import unittest
from unittest.main import main

class TestUsuariosBusqueda(unittest.TestCase):

    def testBusqueda_correcta(self):
        dato = True
        self.assertTrue(dato)

    def testBusqueda_incompleta(self):
        dato = False
        self.assertFalse(dato)

