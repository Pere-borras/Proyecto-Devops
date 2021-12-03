import pytest
from src.mongo_find import mongo_find
from src.conectar_con_mongo import conectar_con_mongo

@pytest.mark.test_calidad_basic
def test_calidad_basic():
    Basic = mongo_find({'calidad':'Basic'})
    for element in Basic:
        assert element['calidad'] == 'Basic'

@pytest.mark.test_calidad_standard
def test_calidad_basic():
    Basic = mongo_find({'calidad':'Standard'})
    for element in Basic:
        assert element['calidad'] == 'Standard'

@pytest.mark.test_calidad_premium
def test_calidad_basic():
    Basic = mongo_find({'calidad':'Premium'})
    for element in Basic:
        assert element['calidad'] == 'Premium'

