import json

with open("personas.json", "r") as archivo:
    datos = json.load(archivo)
    personas = datos["personas"]



def mostrar_usuarios():
    for persona in personas:
        print(persona["nombre"])
    

def buscar_usuarios():    
    nomb_buscar = input("Ingresa el nombre a buscar: ")
    apelli_buscar = input(f"hola {nomb_buscar} ingresa tu apellido: ")
    for persona in personas:
        if persona["nombre"] == nomb_buscar and persona["apellido"] == apelli_buscar:
            #print("Estas inscripto en nuestra plataforma")
            print(persona["nombre"], persona["apellido"])
            break
    else:
        print("No se ha encontrado el usuario, llena tus datos para inscribirte")




def agregar_usuario():
    with open("personas.json", "r") as archivo:
        datos = json.load(archivo)
    nombre_nuevo = input("Ingresa el nombre: ")
    apellido_nuevo = input("Ingresa el apellido: ")
    dni_nuevo = int(input("Ingresa el dni: "))
    if len(str(dni_nuevo)) == 8:
        dni_repetido = False
        for persona in datos["personas"]:
            if persona["dni"] == dni_nuevo:
                dni_repetido = True
                break
        
        if not dni_repetido:
            id_nuevo = len(datos['personas']) + 1 
            nuevos_datos = {"id": id_nuevo, "nombre": nombre_nuevo, "apellido": apellido_nuevo, "dni": dni_nuevo}
            datos["personas"].append(nuevos_datos)
            
            print("Se agrego correctamente el usuario")
        else:
            print("El dni es incorrecto")

        with open("personas.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)

def eliminar_usuario():
    with open("personas.json", "r") as archivo:
        datos = json.load(archivo)
        #print("datos antes de eliminar", datos)
    nuevo_nombre = input("Ingresa el nombre: ")
    dni_nuevo = int(input("Ingresa el dni: "))
    for persona in datos["personas"]:
        if persona["nombre"] == nuevo_nombre and persona["dni"] == dni_nuevo:
            datos["personas"].remove(persona)
            print("El usuario ha sido eliminado")
            break
    else:
        print("No se ha encontrado un usuario con el nombre y dni dado")
    #print("datos despues de eliminar", datos)

    with open("personas.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)


def actualizar_usuario():
    with open("personas.json", "r") as archivo:
        datos = json.load(archivo)
    dni = int(input("Ingresa tu DNI para actulizar los datos: "))
    for persona in datos["personas"]:
        if persona["dni"] == dni:
            nombre_nuevo = input("Nombre: ")
            apellido_nuevo = input("Apellido: ")
            dni_nuevo = int(input("DNI: "))
    persona["nombre"] = nombre_nuevo
    persona["apellido"] = apellido_nuevo
    persona["dni"] = dni_nuevo

    with open("personas.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)




#mostrar_usuarios()
#agregar_usuario()

