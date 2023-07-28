# calculadora con las operaciones matemáticas básicas 
def operaciones():
    opcion = int(input('''Que quiere calcular
                    1) suma
                    2) resta
                    3) multiplicación
                    4) división 
                    '''))
    if opcion == 1:
        a = int(input("Ingrese un número: "))
        b = int(input("Ingrese otro número: "))
        resultado = a + b
        return f"El resultado es {resultado}"
    elif opcion == 2:
        a = int(input("Ingrese un número: "))
        b = int(input("Ingrese otro número: "))
        resultado = a - b
        return f"El resultado es {resultado}"
    elif opcion == 3:
        a = int(input("Ingrese un número: "))
        b = int(input("Ingrese otro número: "))
        resultado = a * b
        return f"El resultado es {resultado}"
    elif opcion == 3:
        a = int(input("Ingrese un número: "))
        b = int(input("Ingrese otro número: "))
        resultado = a * b
        return f"El resultado es {resultado}"


