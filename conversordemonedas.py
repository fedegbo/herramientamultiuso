# todas las conversiones seran a dolares del día 28/7/23
# def monedas(ingreseMoneda):
#     ingreseMoneda.lower()
#     print("Solo puedes cambiar Euros,Pesos Argentinos y Chilenos")
#     ingresar_cantidad = int(input("ingrese la cantidad que quiere cambiar a dolares: ")) 
#     dolar_euro = 1.10
#     dolar_Argento = 546
#     dolar_chile = 827
    
#     if ingreseMoneda == "dolar":
#          ingreseMoneda.lower()
#          print(f"Elegiste {ingreseMoneda}")
#          return ingresar_cantidad / dolar_euro
#     elif ingreseMoneda == "argentina":
#          ingreseMoneda.lower()
#          print(f"Elegiste {ingreseMoneda}")
#          return ingreseMoneda / dolar_Argento
#     elif ingreseMoneda == "chile":
#         ingreseMoneda.lower()
#         print(f"Elegiste {ingreseMoneda}")
#         return ingreseMoneda / dolar_chile
#     else:
#         print("error de programa")
# resultado = monedas("chile")
# print(resultado)

def monedas(ingreseMoneda,ingresar_cantidad):
    ingreseMoneda = ingreseMoneda.lower()
    print("Solo puedes cambiar Euros, Pesos Argentinos y Chilenos")
    dolar_euro = 1.10
    dolar_Argento = 546
    dolar_chile = 827
    
    if ingreseMoneda == "euros":
        print(f"Elegiste {ingreseMoneda}")
        return f"Tieens {ingresar_cantidad * dolar_euro}$ en mano"
    elif ingreseMoneda == "argentina":
        print(f"Elegiste {ingreseMoneda}")
        return f"Tienes {ingresar_cantidad * dolar_Argento}$ en mano"
        return 
    elif ingreseMoneda == "chile":
        print(f"Elegiste {ingreseMoneda}")
        return f"Tieens {ingresar_cantidad * dolar_chile}$ en mano" 
    else:
        print("Error de programa")

