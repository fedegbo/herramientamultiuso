import operaciones as calc
import conversordemonedas as contmone
while True:
    menu = input('''Bienvenido a la herramienta multiuso para todas las necesidades que necesites satisfacer.
                    Por favor elige entre las siguientes opciones
                    1) calculadora
                    2) conversión de monedas
                    aprieta x para salir
                    proximamente mas 
                    ''')

    if menu.lower() == "x":
        break
    elif menu == "1":
      print(calc.operaciones())
    elif menu == "2":
        print(contmone.monedas("Chile",200))
print("¡Hasta luego!")





