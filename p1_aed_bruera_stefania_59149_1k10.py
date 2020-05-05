#Desarrolle un programa completo en Python, sin usar las funciones predefinidas
# min() y max(), que permita cargar los sueldos de tres vendedores.
# Informar el mayor sueldo. Adicionalmente calcule y muestre la bonificación
# obtenida por el vendedor que gana ese sueldo mayor, sabiendo que esta es del
# 20% sobre el monto del sueldo mayor.


print("Parcial 1 - AED - BRUERA, STEFANIA VERÓNICA - 59149 - 1K10")
print("=" * 80)
print("Ejercicio: Sueldo de tres vendedores")
print("=" * 80)

#Datos
sueldo1 = int(input("Sueldo del primer vendedor: "))
sueldo2 = int(input("Sueldo del segundo vendedor: "))
sueldo3 = int(input("Sueldo del tercer vendedor: "))

#Proceso...
if sueldo1 > sueldo2 and sueldo1 > sueldo3:
    mayor = sueldo1
    id = "Vendedor 1"
else:
    if sueldo2 > sueldo3:
        mayor = sueldo2
        id = "Vendedor 2"
    else:
        mayor = sueldo3
        id = "Vendedor 3"

adicional = round((mayor * 20) / 100, 2)
bonificacion = mayor + adicional

#Resultados
print("Mayor sueldo es:",mayor, "y pertenece a:",id)
print(id,"recibe una bonificación de:",bonificacion)

