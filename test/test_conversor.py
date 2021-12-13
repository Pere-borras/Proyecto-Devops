from src.encontrar_documentos.conversor import conversor
import pytest
import os


@pytest.mark.test_archivo_existe
def test_archivo_existe():
    output = [1, 2, 'hola']
    conversor(output)
    print(os.getcwd)
    assert os.path.join(os.getcwd(), 'hugo','content','Packs', '1.md')
    os.remove(os.path.join(os.getcwd(), 'hugo','content','Packs', '1.md'))


@pytest.mark.test_archivo_borrado
def test_archivo_borrado():
    path = os.path.join(os.getcwd(), 'hugo','content','Packs', '1.md')
    assert os.path.isfile(path) == False
