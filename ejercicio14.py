print("Ingrese los valores.")

NUM = int( input("Tipo de Calculo: "))
V = int( input("Ingrese V: "))

Funcion = {
    1 : 100*V,
    2 : 100**V,
    3 : 100/V
}

VAL = Funcion.get(NUM, 0)


print(VAL)