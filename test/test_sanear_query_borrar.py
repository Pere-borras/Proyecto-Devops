from src.eliminar_documentos.sanear_query_borrar import sanear_query_borrar
import pytest

@pytest.mark.test_sanear_query_borrar_1
def test_sanear_query_borrar_1():
    query = ''
    prueba = sanear_query_borrar(query)
    assert prueba == None

@pytest.mark.test_sanear_query_borrar_2
def test_sanear_query_borrar_2():
    query = 'pack prueba x'
    prueba = sanear_query_borrar(query)
    assert prueba == {'Nombre pack': 'pack prueba x'}

@pytest.mark.test_sanear_query_borrar_3
def test_sanear_query_borrar_3():
    query = 'pack prueba'
    resultado = sanear_query_borrar(query)
    assert isinstance(resultado, dict)