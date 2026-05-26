# ==========================================
# Programa: Clasificación de compromiso
# Autor: Jamir Alejandro Cruz Arana
# ==========================================

# Matriz con datos de clientes
# Formato:
# [ID Cliente, Duración en segundos, Eventos Clics]

sesiones = [
    ["C001", 240, 10],
    ["C002", 45, 2],
    ["C003", 120, 5],
    ["C004", 300, 15],
    ["C005", 70, 1]
]

# Función para clasificar el compromiso
def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"


# Mostrar informe final
print("===================================")
print(" INFORME DE COMPROMISO DE SESIONES ")
print("===================================")

# Recorrer la matriz
for sesion in sesiones:

    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    clasificacion = clasificar_compromiso(duracion, clics)

    print(f"Cliente: {id_cliente} -> Compromiso: {clasificacion}")