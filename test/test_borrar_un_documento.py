from src.eliminar_documentos.borrar_un_documento import borrar_un_documento
from src.mongo_archivos.conectar_con_mongo import conectar_con_mongo
import pytest

pack_prueba = {
    "Nombre pack": "Pack de prueba para test",
    "calidad": "Premium",
    "precio": "52€",
    "stock": "23",
    "dimensiones": {
        "altura": "5 cm ",
        "ancho": "10 cm"
    },
    "contenidos": {
        "Gorro de fiesta volador": {
            "caracteristicas": {
                "Precio": "8",
                "Calidad": "49",
                "Material": "indestructible",
                "Cantidad": "1",
                "Stock": "23",
                "Demanda": "99"
            }
        },
        "Balón anti-gravedad": {
            "caracteristicas": {
                "Precio": "7",
                "Calidad": "50",
                "Material": "normal",
                "Cantidad": "1",
                "Stock": "100",
                "Demanda": "61"
            }
        },
        "Inyección de felicidad": {
            "caracteristicas": {
                "Precio": "30",
                "Calidad": "100",
                "Material": "consumible",
                "Cantidad": "1",
                "Stock": "200",
                "Demanda": "100"
            }
        },
        "Poción del amor": {
            "caracteristicas": {
                "Precio": "7",
                "Calidad": "42",
                "Material": "consumible",
                "Cantidad": "1",
                "Stock": "100",
                "Demanda": "61"
            }
        }
    }
}

@pytest.mark.test_borrar_un_documento
def test_borrar_un_documento():

    colleccion = conectar_con_mongo()
    colleccion.insert_one(pack_prueba)

    query = {"Nombre pack": "Pack de prueba para test"}
    
    borrar_un_documento(query)

    assert colleccion.find_one(pack_prueba) == None