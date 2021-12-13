from src.encontrar_documentos.query import sanear_query
import pytest


@pytest.mark.test_query_in_brackets_1
def test_query_in_brackets_1():
    request = "'hola': '1'"
    output = sanear_query(request)
    assert output[0] == '{'
    assert output[-1] == '}'


@pytest.mark.test_query_in_brackets_2
def test_query_in_brackets_2():
    request = "'hola': '2'}"
    output = sanear_query(request)
    assert output[0] == '{'
    assert output[-1] == '}'


@pytest.mark.test_query_in_brackets_3
def test_query_in_brackets_3():
    request = "{'hola': '3'"
    output = sanear_query(request)
    assert output[0] == '{'
    assert output[-1] == '}'


@pytest.mark.test_query_in_brackets_4
def test_query_in_brackets_4():
    request = "{'hola': '4'}"
    output = sanear_query(request)
    assert output[0] == '{'
    assert output[-1] == '}'


@pytest.mark.test_query_in_brackets_5
def test_query_in_brackets_5():
    request = ''
    output = sanear_query(request)
    assert '{' in output
    assert '}' in output
