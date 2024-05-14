from funciones import *



print("""
1. Mostrar usuarios
2. Buscar usuario
3. Agregar usuario
4. Eliminar usuario
5. Actualizar usuario
6. Salir
        """
    )



while True:
    opcion = int(input("Ingresa una opcion: "))
    if opcion == 1:
        mostrar_usuarios()
    elif opcion == 2:
        buscar_usuarios()
    elif opcion == 3:
        agregar_usuario()
    elif opcion == 4:
        eliminar_usuario()
    elif opcion == 5:
        actualizar_usuario()
    elif opcion == 6:
        break
    else:
        print("Has ingresado una opcion incorrecta")








"""
mostrar usuarios
buscar un usuario
agregar usuario
eliminar

"""