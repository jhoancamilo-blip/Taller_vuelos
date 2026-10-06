print("Sistema de gestión de vuelos")





























def verificar_ocupacion(pasajeros):

    if pasajeros < 50:
        return "Baja ocupación"
    else:
        return "Ocupación normal"

    resultados = []

for codigo, datos in vuelos.items():

    pasajeros = datos["pasajeros"]
    precio = datos["precio"]

    precio_final, ingreso = calcular_ingreso(
        pasajeros,
        precio
    )

    ocupacion = verificar_ocupacion(pasajeros)

    resultados.append({
        "codigo": codigo,
        "pasajeros": pasajeros,
        "precio_original": precio,
        "precio_final": precio_final,
        "ingreso": ingreso,
        "ocupacion": ocupacion
    })

    resultados.sort(
    key=lambda vuelo: vuelo["ingreso"],
    reverse=True
)
    ingreso_global = sum(
    vuelo["ingreso"]
    for vuelo in resultados
)
    print("\n===== REPORTE DE VUELOS =====")

for vuelo in resultados:

    print(f"\nVuelo: {vuelo['codigo']}")
    print(f"Pasajeros: {vuelo['pasajeros']}")
    print(f"Precio original: ${vuelo['precio_original']:.2f}")
    print(f"Precio final: ${vuelo['precio_final']:.2f}")
    print(f"Ingreso generado: ${vuelo['ingreso']:.2f}")
    print(f"Ocupación: {vuelo['ocupacion']}")

print(
    f"\nIngreso global de la aerolínea: "
    f"${ingreso_global:.2f}"
)
