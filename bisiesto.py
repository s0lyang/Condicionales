print("año bisiesto")

año = int( input("Ingrese año: "))

if (año % 400 == 0) or (año % 4 == 0) and (año % 100 != 0):
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")