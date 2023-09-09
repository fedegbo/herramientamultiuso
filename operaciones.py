def operaciones():
    num = int(input('Ingrese un numero: '))
    num1 = int(input('Ingrese otro numero: '))
    eleccion = 0
    while eleccion != 7:
        eleccion = int(input("""Elige Entre las siguientes operaciones: \n 
                     1) suma
                     2) resta
                     3) multiplicación
                     4) división
                     5) potenciar
                     6) cambio de valores
                     7) salir
                     \n"""))
        if eleccion == 1:
            return f"{num} + {num1} = {num + num1}"
        elif eleccion == 2:
            return f"{num} - {num1} = {num - num1}"
        elif eleccion == 3:
            return f"{num} X {num1} = {num * num1}"
        elif eleccion == 4:
            return f"{num} / {num1} = {num / num1}"
        elif eleccion == 5:
            return num**num1
        elif eleccion == 6:
            num = int(input('Ingrese un numero: '))
            num1 = int(input('Ingrese otro numero: '))
        elif eleccion == 7:
            print('Gracias por usar nuestra calculadora :)')
    

