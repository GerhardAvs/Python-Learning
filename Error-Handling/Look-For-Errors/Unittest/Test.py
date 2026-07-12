import unittest          # Importa el módulo para crear pruebas unitarias.
import Mi_Function       # Importa el archivo donde está la función a probar.

# Clase de prueba. Debe heredar de unittest.TestCase.
class Test_cambiar_texto(unittest.TestCase):

    # Cada método que empiece con "test_" será ejecutado automáticamente.
    def test_todo_mayusculas(self):

        # Comprueba que la función Todo_Mayusculas("hola")
        # devuelva exactamente "HOLA".
        self.assertEqual(
            Mi_Function.Todo_Mayusculas("hola"),
            "HOLA"
        )

# Este bloque solo se ejecuta si este archivo se ejecuta directamente.
if __name__ == '__main__':

    # Ejecuta todas las pruebas de la clase.
    unittest.main()