import datetime

# Modo de uso de software
Operation_type = input("¿Que tipo de operacion quiere realizar?")

match Operation_type:
    case 'consulta':
        time_interval = input("Tipo de bolsa de carbon: ")
    case 'ingreso':
        time_interval = input("Tipo de bolsa de carbon: ")
    case _:
        print("Operacion incorrecta")

# Solicitar al usuario que ingrese datos
bag_type = input("Tipo de bolsa de carbon: ")
carbon_type = input("Tipo de carbon: ")
volume = input("Ingrese el volumen ingresado: ")

# Obtener la fecha y hora actual y formatearla hasta los segundos
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Imprimir los datos ingresados
print("\nDatos ingresados:")
print("Tipo de bolsa:", bag_type)
print("Tipo de carbon:", carbon_type)
print("Volumen ingresado:", volume)
print("Fecha de ingreso:", timestamp)
