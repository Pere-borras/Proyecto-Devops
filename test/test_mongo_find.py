import pytest
from src.mongo_archivos.mongo_find import mongo_find

@pytest.mark.test_calidad_basic
def test_calidad_basic():
    Basic = mongo_find({'calidad':'Basic'})
    for element in Basic:
        assert element['calidad'] == 'Basic'

@pytest.mark.test_calidad_standard
def test_calidad_standard():
    Basic = mongo_find({'calidad':'Standard'})
    for element in Basic:
        assert element['calidad'] == 'Standard'

@pytest.mark.test_calidad_premium
def test_calidad_premium():
    Basic = mongo_find({'calidad':'Premium'})
    for element in Basic:
        assert element['calidad'] == 'Premium'

