while True:
    try:
        select = int(input(
            '  Elige una opcion \n Agregar Datos presiona 1 \n Visualizar datos presiona 2 \n Volver al menu principal presiona 3 :  '))
    except ValueError:
        print("Por favor, ingresa un número válido.")
