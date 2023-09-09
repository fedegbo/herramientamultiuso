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
    elif ingreseMoneda == "chile":
        print(f"Elegiste {ingreseMoneda}")
        return f"Tieens {ingresar_cantidad * dolar_chile}$ en mano" 
    else:
        print("Error de programa")

