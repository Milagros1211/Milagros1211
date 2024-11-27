import datetime

# Solicitar al usuario que ingrese datos
bag_type = input("Tipo de bolsa de carbon: ")
carbon_type = input("Tipo de carbon: ")
volume = input("Ingrese el volumen ingresado: ")
timestamp = datetime.datetime.now()

# Imprimir los datos ingresados
print("\nDatos ingresados:")
print("Tipo de bolsa:", bag_type)
print("Tipo de carbon:", carbon_type)
print("Volumen ingresado:", volume)
print("Fecha de ingreso:", timestamp)
