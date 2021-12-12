from src.encontrar_documentos.recopilador_datos import recopilador_datos
import pytest


@pytest.mark.test_datos_correctos
def test_datos_correctos():
    json_arr = {"Nombre pack": "Pack Squanchy Style", "calidad": "Basic", "precio": "7", "stock": "25", "dimensiones": {"altura": "3 cm", "ancho": "6 cm"}, "contenidos": {"Rifle de pulso": {"caracteristicas": {"Precio": "5", "Calidad": "30",
                                                                                                                                                                                                                  "Material": "normal", "Cantidad": "1", "Stock": "25", "Demanda": "10"}}, "Poción del arcoiris": {"caracteristicas": {"Precio": "2", "Calidad": "20", "Material": "consumible", "Cantidad": "1", "Stock": "50", "Demanda": "63"}}}}
    output = recopilador_datos(json_arr)
    assert output == ['---', 'title: "Pack Squanchy Style"', 'draft: true', 'tags: ["Basic"]', '---', '## Pack Squanchy Style', '#### Calidad: Basic.', '#### Precio: 7.', '#### Stock: 25.', '#### Dimensiones', '**Altura**: 3 cm.', '','**Ancho**: 6 cm.', '## Contenidos', '- Rifle de pulso', '    - Caracteristicas', '        - Precio: 5', '        - Calidad: 30', '        - Material: normal', '        - Cantidad: 1', '        - Stock: 25', '        - Demanda: 10', '- Poción del arcoiris', '    - Caracteristicas', '        - Precio: 2', '        - Calidad: 20', '        - Material: consumible', '        - Cantidad: 1', '        - Stock: 50', '        - Demanda: 63' ]
