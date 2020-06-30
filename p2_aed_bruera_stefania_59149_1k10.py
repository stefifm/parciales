# Consignas

# Se pide desarrollar un programa en Python que permita cargar por teclado
# un texto completo en una variable de tipo cadena de caracteres.  El texto
# finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar
# el final del texto, y que cada palabra de ese texto está separada de las
# demás por un espacio en blanco. El programa debe incluir al menos una
# función simple con parámetros y retorno de resultado, debe procesar el
# texto caracter a caracter (a razón de uno por vuelta de ciclo), y debe
# hacer lo siguiente sin usar un menú de opciones:


# 1) Determinar la cantadad de palabras que tenían más vocales que consonantes
# pero al mismo tiempo tenían al menos una vez la letra "u". Por ejemplo,
# el texto: “La muela me duele mucho.” tiene 2 palabras que cumplen:  (
# "muela" y "duele").

# 2) Determinar el promedio de letras por palabra entre las que tenían una con
# "t" en la segunda posición. Por ejemplo, en el texto:  “Atenas atacó con
# valentía.” hay 2 palabras que cumplen la condición ("Atenas" y "atacó")  y
# suman un total de 11 letras, por lo que el promedio pedido es de 5.5
# letras  por palabra.

# 3) Determinar la longitud de la palabra más larga de  todo el texto. Por
#  ejemplo, en el texto: “Las últimas directivas fueron de quedarse en
#  casa.”  La palabra más larga tiene 10 letras ("directiva").

# 4) Determinar cuántas palabras contenían la expresión "as",  pero no
# contenían una "e". Por ejemplo, en el texto:  "Pasamos pero no aspiramos a
# asestar otro golpe.", hay dos palabras que cumple la  condición ("Pasamos"
# y "aspiramos"). La palabra "asestar" tiene la expresión "as",  pero no
# cuenta porque tiene también una "e".
# Criterios generales de evaluación:
#
# Desarrollo del programa completo, incluyendo al menos una función  con
# parámetros y retorno de resultado: [máximo: 20% del puntaje]
# Desarrollo correcto del ítem 1: [máximo: 20% del puntaje]
# Desarrollo correcto del ítem 2: [máximo: 20% del puntaje]
# Desarrollo correcto del ítem 3: [máximo: 20% del puntaje]
# Desarrollo correcto del ítem 4: [máximo: 20% del puntaje]
# Para aprobar el parcial, el alumno debe llegar a un total acumulado de al
# menos 55% del puntaje, pero obligatoriamente debe estar desarrollado el
# programa, funcionando y operativo.

print("Parcial 2 Algoritmo y Estructura de Datos - Stefania Bruera - 59149 - 1K10")

# Funciones

def es_vocal(c):
    vocal = "aeiouáéíóú"
    if c in vocal:
        return True
    return False

def es_letra(c):
    if c >= "a" and c <= "z":
        return True
    return False

def es_consonante(c):
    if es_letra(c) and es_vocal(c) == False:
        return True
    return False

def promedio(suma, total):
    if total > 0:
        prom = round(suma / total, 2)
    else:
        prom = 0
    return prom


# Contadores y banderas

# Contadores generales
cont_letras = 0
palabras = 0

# Contadores del punto 1
cont_vocales = 0  # Contador de vocales para cuando la función es_vocal de True
cont_consonantes = 0 # Contador de consonantes para cuando la función
                     # es_consonantes de True
cont_u = 0 # Contador para saber la cantidad de "u" y luego usarla para ver
            # si al menos hay 1
pal_masvocal_u = 0 # Contador de palabras con más vocal que consonante y al
                    # menos una "u".

# Punto 2:
flag_seg_t = False # bandera para detectar si hay una "t" en la segunda posicón.
acu_letras_segt = 0 # Acumuladores para sumar la cantidad de letras entre
                    # las palabras que hay "t" en la segunda posición
palabras_t = 0 # Contador de palabras con "t" en la segunda posición

# Punto 4
flag_a = flag_as = False # Banderas para formar "as"
flag_e = False # Bandera para ver si hay una letra "e"
pal_as_sin_e = 0 # Contador de palabras con 'as' pero sin "e"


# Carga de texto
texto = input("Cargue un texto. Termina en punto: ")
texto = texto.lower()


# Resolución de los puntos
for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1
        # Punto 1
        # Usé las funciones es_vocal y es_consonante para luego contarlos
        # respectivamente.
        if es_vocal(caracter):
            cont_vocales += 1
        if es_consonante(caracter):
            cont_consonantes += 1
        # Contador de letra "u" para ver cuántas hay
        if caracter == "u":
            cont_u += 1

        # Punto 2
        # Ver si hay una "t" en la segunda posición
        if cont_letras == 2 and caracter == "t":
            flag_seg_t = True

        # Punto 3
        # Bandera para ver si hay "as" y luego otra para ver si hay letra "e"
        if caracter == "a":
            flag_a = True
        else:
            if flag_a and caracter == "s":
                flag_as = True
            flag_a = False
        if caracter == "e":
            flag_e = True
    else:
        if cont_letras == 0:
            continue
        palabras += 1

        # Punto 1
        # Si cont_vocales es mayor al cont_consonantes
        # Y si hay 1 o más "u"
        if cont_vocales > cont_consonantes and cont_u >= 1:
            pal_masvocal_u += 1

        # Punto 2
        # Bandera de "t" en segunda posicón en True
        # Luego se cuentan las palabras con "t" en segunda posición y
        # después se acumulan las letras cuas palabras cumplan con la condición
        if flag_seg_t == True:
            palabras_t += 1
            acu_letras_segt += cont_letras

        # Punto 3: Para ver la longitud de la palabra más larga del texto
        if palabras == 1 or cont_letras > mayor:
            mayor = cont_letras

        # Punto 4
        # Bandera de "e" en Falso para ver si hay "as" pero no "e"
        if flag_as and flag_e == False:
            pal_as_sin_e += 1
        palabras += 1

        # Reinicio de contadores y banderas
        cont_letras = 0
        cont_vocales = 0
        cont_consonantes = 0
        flag_seg_t = False
        flag_a = flag_as = flag_e = False


# Cálculos
prom_seg_t = promedio(acu_letras_segt, palabras_t)

# Resultados
print()
print("==================== RESULTADOS ======================")
print()

print("Punto 1 =========>")
print("Cantidad de palabras que tenían más vocales que consonantes y tienen "
      "al menos una 'u':",pal_masvocal_u)
print()

print("Punto 2 =========>")
print("Promedio de letras por palabras entre las que tenían una 't' en la "
      "segunda posición:",prom_seg_t)
print()

print("Punto 3 =========>")
print("Longitud de la palabra más larga del texto:",mayor)
print()

print("Punto 4 =========>")
print("Cantidad de palabras que tenían la experesión 'as' pero no tienen "
      "letra 'e':",pal_as_sin_e)
print()
