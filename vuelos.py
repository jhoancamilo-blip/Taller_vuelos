print("Sistema de gestión de vuelos")
vuelos = {
    "AV101": {
        "pasajeros": 80,
        "precio": 450
    },
    "AV202": {
        "pasajeros": 45,
        "precio": 600
    },
    "AV303": {
        "pasajeros": 120,
        "precio": 750
    },
    "AV404": {
        "pasajeros": 35,
        "precio": 500
    }
}

def calcular_ingreso(pasajeros, precio):

    if precio > 500:
        precio_final = precio * 0.85
    else:
        precio_final = precio

    ingreso = pasajeros * precio_final

    return precio_final, ingreso