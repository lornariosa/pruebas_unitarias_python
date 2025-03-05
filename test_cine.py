from cine import Pelicula
import pytest

#Compra de entradas con asientos suficientes.
def test_compra_exitosa():
    pelicula1 = Pelicula("Test Pelicula_1", 10, 10)
    resultado = pelicula1.vender_entradas(5)
    assert resultado == "Has comprado 5 entradas para Test Pelicula_1. Total: $50"
    assert pelicula1.asientos_disponibles == 5

#Compra de entradas con asientos insuficientes.
def test_compra_asientos_insuficientes():
    pelicula2 = Pelicula("Test Pelicula_2", 3, 10)
    resultado = pelicula2.vender_entradas(5)
    assert resultado == "No hay suficientes asientos disponibles. Solo quedan 3 asientos."
    assert pelicula2.asientos_disponibles == 3

#Compra de cero entradas.
def test_compra_cero_entradas():
    pelicula3 = Pelicula("Test Pelicula_3", 10, 10)
    resultado = pelicula3.vender_entradas(0)
    assert resultado == "Has comprado 0 entradas para Test Pelicula_3. Total: $0"
    assert pelicula3.asientos_disponibles == 10

if __name__ == "__main__":
    pytest.main()