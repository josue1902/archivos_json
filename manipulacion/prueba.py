import json

# Supongamos que tienes una lista llamada "lista_json" que contiene objetos JSON
lista_json = [
    {"nombre": "Juan", "edad": 30},
    {"nombre": "María", "edad": 25},
    {"nombre": "Pedro", "edad": 35}
]

# Supongamos que quieres eliminar el diccionario con nombre "María"
nombre_a_eliminar = "María"

# Itera sobre la lista y elimina el diccionario con el nombre especificado
for item in lista_json:
    if item.get("nombre") == nombre_a_eliminar:
        lista_json.remove(item)

# Imprime la lista actualizada
print(lista_json)
