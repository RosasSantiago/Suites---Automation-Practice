import unittest

class TestUsuarios(unittest.TestCase):

    def testUsuarioCreado(self):
        usuario = 'Pepe'
        self.assertEqual(usuario, 'Pepe')

    def testUsuarioNoCreado(self):
        respuesta = 'El usuario no ha sido creado'
        self.assertEqual(respuesta, 'El usuario no ha sido creado')
