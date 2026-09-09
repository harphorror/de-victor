# ============================================================
# CLASE: U4 - Clase 1: Introducción a Funciones
# Colegio Arriarán Barros — Pensamiento Computacional y Programación
# ============================================================
# Estudiante: Víctor Valentín Moreira Segovia
# Curso: 3°MB
# Inicio: 09-09-2026, 8:29:37 a. m.
# Guardado: 09-09-2026, 8:30:26 a. m.
# Tiempo transcurrido: 0 min 47 seg
# ============================================================

# ============================================================
# EJERCICIOS DE CÓDIGO
# (Ver la Materia completa en la página — no se incluye aquí porque
#  es contenido de referencia, no algo que el estudiante responde)
# ============================================================

# ------------------------------------------------------------
# EJERCICIO 1: Modelo: función de bienvenida
# Enunciado: Código ya resuelto. Ejecútalo y observa que la función no hace nada hasta que se llama explícitamente.
# Estado última ejecución: no ejecutado
# ------------------------------------------------------------

def bienvenida():
    print("Bienvenido al curso de Python")
    print("Hoy empezamos Funciones")

bienvenida()
bienvenida()

# --- Salida obtenida al ejecutar (referencial) ---
# (no se ejecutó este ejercicio)


# ------------------------------------------------------------
# EJERCICIO 2: Práctica guiada: función de despedida
# Enunciado: Completa el código: define una función llamada 'despedida' que imprima dos líneas de mensaje de despedida, y llámala dos veces.
# Estado última ejecución: no ejecutado
# ------------------------------------------------------------

# Escribe aquí la definición de la función
def despedida():
    print("bye bye")
    print("chao")

despedida()
despedida()

# Escribe aquí las 2 llamadas a la función

# --- Salida obtenida al ejecutar (referencial) ---
# (no se ejecutó este ejercicio)


# ------------------------------------------------------------
# EJERCICIO 3: Independiente: función de reglas del curso
# Enunciado: Crea una función llamada 'reglas' que imprima 3 reglas del curso (a tu elección). Llámala una vez.
# Estado última ejecución: no ejecutado
# ------------------------------------------------------------

# Escribe tu solución completa aquí
def reglas():
    print("1: Jugar la batalla contra sans")
    print("2: No jugar minecraft en clase")
    print("3: apostar en umamusume")

reglas()

# --- Salida obtenida al ejecutar (referencial) ---
# (no se ejecutó este ejercicio)


# ------------------------------------------------------------
# EJERCICIO 4: Modelo: saludo personalizado
# Enunciado: Código ya resuelto. Ejecútalo y observa cómo el mismo saludo cambia según el parámetro que le pasas.
# Estado última ejecución: no ejecutado
# ------------------------------------------------------------

def saludar(nombre):
    print(f"¡Hola, {nombre}! Bienvenido a Python")

saludar("Ana")
saludar("Beto")
saludar("Carolina")

# --- Salida obtenida al ejecutar (referencial) ---
# (no se ejecutó este ejercicio)


# ------------------------------------------------------------
# EJERCICIO 5: Práctica guiada: presentación con 2 parámetros
# Enunciado: Completa el código: define una función 'presentar' que reciba nombre y curso, y muestre un mensaje combinando ambos.
# Estado última ejecución: no ejecutado
# ------------------------------------------------------------

# Escribe aquí la función con 2 parámetros: nombre y curso
def presentar(nombre, curso):
    print(f"Bienvenid@ {nombre} estas en {curso}")


presentar("Ana", "3ºA")
presentar("Beto", "3ºB")

# --- Salida obtenida al ejecutar (referencial) ---
# (no se ejecutó este ejercicio)


# ------------------------------------------------------------
# EJERCICIO 6: Independiente: calculadora de descuento
# Enunciado: Crea una función 'mostrar_descuento' que reciba dos parámetros: precio y porcentaje. La función debe imprimir el precio, el porcentaje, y el monto del descuento (precio * porcentaje / 100). Llámala con al menos 2 combinaciones distintas de valores.
# Estado última ejecución: no ejecutado
# ------------------------------------------------------------

# Escribe tu solución completa aquí
def m_d(precio, porcentaje):
    descuento = precio * porcentaje / 100
    print(f"Vale {precio}, con {porcentaje}% de descuento, monto final es {descuento}")
m_d(1000, 5)
m_d(25000, 2)

# --- Salida obtenida al ejecutar (referencial) ---
# (no se ejecutó este ejercicio)


# ------------------------------------------------------------
# EJERCICIO 7: Modelo: sumar con return
# Enunciado: Código ya resuelto. Ejecútalo y observa cómo el resultado de la función se guarda en una variable y se puede seguir usando.
# Estado última ejecución: no ejecutado
# ------------------------------------------------------------

def sumar(a, b):
    return a + b

resultado = sumar(3, 4)
print(resultado)
print(resultado * 2)

# --- Salida obtenida al ejecutar (referencial) ---
# (no se ejecutó este ejercicio)


# ------------------------------------------------------------
# EJERCICIO 8: Práctica guiada: calcular el doble
# Enunciado: Completa el código: la función 'doble' debe usar return (no print) para devolver el doble del número recibido. Luego usa el resultado guardado en una variable.
# Estado última ejecución: no ejecutado
# ------------------------------------------------------------

def doble(numero):
    # Escribe aquí: usa return para devolver numero * 2
     return numero * 2

resultado = doble(5)
print(f"El doble de 5 es {resultado}")

# --- Salida obtenida al ejecutar (referencial) ---
# (no se ejecutó este ejercicio)


# ------------------------------------------------------------
# EJERCICIO 9: Independiente: función de promedio
# Enunciado: Crea una función 'promedio' que reciba dos notas y use return para devolver el promedio de ambas (sin usar print dentro de la función). Guarda el resultado en una variable y muéstralo con print() fuera de la función.
# Estado última ejecución: no ejecutado
# ------------------------------------------------------------

# Escribe tu solución completa aquí
def media(n1, n2):
    return (n1 + n2) / 2


resultado = media(6.4,  7.0)
print(f"la media es {resultado}")

# --- Salida obtenida al ejecutar (referencial) ---
# (no se ejecutó este ejercicio)


# ------------------------------------------------------------
# EJERCICIO 10: Desafío: calculadora de notas del curso
# Enunciado: Crea una función 'calcular_promedio' que reciba una lista de notas (parámetro) y use return para devolver el promedio (usa sum() y len()). Luego, pide al usuario 4 notas, guárdalas en una lista, y usa tu función para calcular y mostrar el promedio del curso.
# Estado última ejecución: no ejecutado
# ------------------------------------------------------------

def calcular_promedio(notas):
    # Escribe aquí: usa return para devolver el promedio
     return sum(notas) / len(notas)


notas_curso = []
for i in range(4):
    nota = float(input(f"Nota {i + 1}: "))
    notas_curso.append(nota)

promedio_final = calcular_promedio(notas_curso)
print(f"El promedio del curso es {promedio_final}")

# --- Salida obtenida al ejecutar (referencial) ---
# (no se ejecutó este ejercicio)


# ============================================================
# BITÁCORA DE LA CLASE
# ============================================================

# ¿Qué es una función?: Explica con tus palabras qué es una función y por qué es útil usarlas en vez de repetir código.
# Respuesta:
#   La función es un bloque de código que nos permite escribir lo que queramos sin tener la necesidad de repetir lo que queramos escribir

# return vs print(): ¿Cuál es la diferencia entre usar return y usar print() dentro de una función? Da un ejemplo de cuándo usarías cada uno.
# Respuesta:
#   return devuelve un valor, en cambio print solo muestra lo que va a estar escrito. print es útil para enviar mensajes, crear mensajes. Return es util cuando se quiere hacer operaciones de manera continua como para sacar promedios.

# Etapa más difícil: De las 3 etapas (Modelo, Guiado, Independiente), ¿en cuál tuviste que pensar más? ¿Por qué crees que fue esa?
# Respuesta:
#   En el guiado, porque trataba de comprender mientras lo hacía, en el independiente ya sabía cómo hacerlo.

# Un ejemplo de mi código: Copia una línea de código que TÚ hayas escrito hoy que te haya costado entender al principio, y explica qué hace.
# Respuesta:
#   return sum(notas) / len(notas)
#   esto sirve para cada valor que tengan las notas se sumen, y luego se dividan por la cantidad de notas

# Preguntas pendientes: ¿Qué duda te queda de la clase de hoy? (si no tienes ninguna, escribe 'ninguna')
# Respuesta:
#   ninguna

# ============================================================
# FIN
# ============================================================
