import pytest
from biblioteca import Libro, Biblioteca

# Pruebas para la clase Libro
def test_atributos_libro():
    libro = Libro("Asesinato para principiantes", "Holly Jackson", 2014)
    assert libro.titulo == "Asesinato para principiantes"
    assert libro.autor == "Holly Jackson"
    assert libro.anio == 2014
    assert libro.prestado is False

def test_libro_estado():
    libro = Libro("Asesinato para principiantes", "Holly Jackson", 2014)
    assert "disponible" in str(libro)
    libro.prestado = True
    assert "prestado" in str(libro)


# Pruebas para la clase Biblioteca
def test_agregar_libro():
    biblioteca = Biblioteca()
    libro = Libro("Asesinato para principiantes", "Holly Jackson", 2014)
    biblioteca.agregar_libro(libro)
    assert len(biblioteca.libros) == 1
    assert biblioteca.libros[0] == libro


def test_eliminar_libro():
    biblioteca = Biblioteca()
    libro = Libro("Asesinato para principiantes", "Holly Jackson", 2014)
    biblioteca.agregar_libro(libro)
    biblioteca.eliminar_libro("Asesinato para principiantes")
    assert len(biblioteca.libros) == 0


def test_eliminar_libro_no_existente():
    biblioteca = Biblioteca()
    libro = Libro("Asesinato para principiantes", "Holly Jackson", 2014)
    biblioteca.agregar_libro(libro)
    biblioteca.eliminar_libro("Desaparición para expertos")
    assert len(biblioteca.libros) == 1


def test_buscar_libro():
    biblioteca = Biblioteca()
    libro = Libro("Asesinato para principiantes", "Holly Jackson", 2014)
    biblioteca.agregar_libro(libro)
    assert biblioteca.buscar_libro("Asesinato para principiantes") == libro

def test_buscar_libro_no_existente():
    biblioteca = Biblioteca()
    assert biblioteca.buscar_libro("Asesinato para principiantes") is None


def test_listar_libros():
    biblioteca = Biblioteca()
    libro1 = Libro("Asesinato para principiantes", "Holly Jackson", 2014)
    libro2 = Libro("Desaparición para expertos", "Holly Jackson", 2021)
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    lista = biblioteca.listar_libros()
    assert len(lista) == 2
    assert "Asesinato para principiantes de Holly Jackson (2014) - disponible" in lista
    assert "Desaparición para expertos de Holly Jackson (2021) - disponible" in lista


def test_prestar_libro():
    biblioteca = Biblioteca()
    libro = Libro("Asesinato para principiantes", "Holly Jackson", 2014)
    biblioteca.agregar_libro(libro)
    mensaje = biblioteca.prestar_libro("Asesinato para principiantes")
    assert libro.prestado is True
    assert mensaje == "Has pedido prestado el libro 'Asesinato para principiantes'."

def test_prestar_libro_prestado():
    biblioteca = Biblioteca()
    libro = Libro("Asesinato para principiantes", "Holly Jackson", 2014)
    biblioteca.agregar_libro(libro)
    biblioteca.prestar_libro("Asesinato para principiantes")
    mensaje = biblioteca.prestar_libro("Asesinato para principiantes")
    assert mensaje == "El libro 'Asesinato para principiantes' ya está prestado."

def test_prestar_libro_no_existente():
    biblioteca = Biblioteca()
    mensaje = biblioteca.prestar_libro("Asesinato para principiantes")
    assert mensaje == "El libro 'Asesinato para principiantes' no se encuentra en la biblioteca."


def test_devolver_libro():
    biblioteca = Biblioteca()
    libro = Libro("Asesinato para principiantes", "Holly Jackson", 2014)
    biblioteca.agregar_libro(libro)
    biblioteca.prestar_libro("Asesinato para principiantes")
    mensaje = biblioteca.devolver_libro("Asesinato para principiantes")
    assert libro.prestado is False
    assert mensaje == "Has devuelto el libro 'Asesinato para principiantes'."

def test_devolver_libro_no_prestado():
    biblioteca = Biblioteca()
    libro = Libro("Asesinato para principiantes", "Holly Jackson", 2014)
    biblioteca.agregar_libro(libro)
    mensaje = biblioteca.devolver_libro("Asesinato para principiantes")
    assert mensaje == "El libro 'Asesinato para principiantes' no estaba prestado."

def test_devolver_libro_no_existente():
    biblioteca = Biblioteca()
    mensaje = biblioteca.devolver_libro("Asesinato para principiantes")
    assert mensaje == "El libro 'Asesinato para principiantes' no se encuentra en la biblioteca."

if __name__ == "__main__":
    pytest.main()
