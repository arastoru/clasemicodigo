# Código de que peliculas puedes ver en el cine
edad_str = input("Bienvenido al cine, ¿cuál es tu edad?: ")
edad = int(edad_str)

if edad < 0:
    print("Edad no válida. Por favor, ingresa un número positivo.")
elif edad >= 18:
    print("¡Puedes ver películas clasificadas R!")
elif edad >= 13:  # Python llega aquí solo si edad NO es >= 18 y NO es < 0
    print("Puedes ver películas clasificadas PG-13.")
else:  # Si no es < 0, ni >= 18, ni >= 13, entonces debe ser < 13 y >= 0
    print("Te recomendamos películas clasificadas G o P.")

print("\n")

# Código de la tabla de multiplicar
num_tabla = int(input("Ingresa un número para ver su tabla de multiplicar: "))
print(f"--- Tabla del {num_tabla} ---")

for i in range(1, 11):  # i tomará valores de 1 a 10
    resultado = num_tabla * i
    print(f"{num_tabla} x {i} = {resultado}")
#Código bucle for
numeroenteroposit = int(input("Ingresa un número entero positivo: "))
print(f"Contando hasta {numeroenteroposit} (sin incluirlo):")
for numero in range(numeroenteroposit): 
         # range(n) genera números desde 0 hasta n-1
    print(numero, end=" ")


#Codigo de refactorizacion (incluimos listas) rectangulo
def calcular_area_rectangulo(base, altura):
    return base * altura

rectangulos = []  #es una variable para almacenar los datos de los rectangulos
contador = 1   #es la variable para contar los rectangulos

while True:
    base = int(input("Ingrese la base del rectángulo: "))
    altura = int(input("Ingrese la altura del rectángulo: "))
    area = calcular_area_rectangulo(base, altura)
    rectangulos.append((contador, base, altura, area)) #el append te permite agregar elementos a la lista
    print(f"El área del rectángulo {contador} ({base}x{altura}) es: {area}")
    contador += 1

    continuar = input("¿Desea ingresar otro rectángulo? Presione Enter para continuar o 'n' para salir: ")
    if continuar.lower() == 'n':
        break

ver_datos = input("¿Desea ver los datos de los rectángulos guardados? Presione 1 para ver: ")
if ver_datos == '1':
    for rectangulo in rectangulos:
        numero, base, altura, area = rectangulo
        print(f"Rectángulo {numero}: Base = {base}, Altura = {altura}, Área = {area}")


#Codigo bucle while
contador = 0
numero = int(input("Introduce un número entero: "))
print("\nBucle while:")
while contador < numero:  # la condición depende del número ingresado
    print(f"Contador es: {contador}")
    contador = contador + 1  # Actualiza la variable de control(contador)
print("¡El bucle while ha terminado!")



#Codigo para lista actualizable de integrantes grupo Ingenidea
 # Primero creamos una lista vacía para los nombres de los estudiantes
lista_nombres_estudiantes = [] #  lista

print("¡Bienvenidos integrantes del grupo Ingenidea!")

# Bucle para añadir integrantes
while True:
    print("\nEscribe el nombre del nuevo integrante (o escribe 'salir' para terminar):")
    nombre_nuevo = input("Ingresa el nombre: ").strip()

    # Aqui finalizamos si el usuario desea terminar de registrar nombres
    if nombre_nuevo.lower() in ["salir", "fin"]:
        print("\nFinalizando el registro de integrantes...")
        break

    # Guardar el nombre del integrante anterior (si existe)
    # Se actualizó el nombre de la lista
    nombre_anterior = lista_nombres_estudiantes[-1] if lista_nombres_estudiantes else None

    # Añadir el nuevo nombre a la lista
    # Se actualizó el nombre de la lista
    lista_nombres_estudiantes.append(nombre_nuevo)

    # Mensaje de bienvenida
    print(f"¡Bienvenid@ {nombre_nuevo} al grupo Ingenidea!")

    # Mostrar detallitos
    print("\n--- Detalles de incorporación ---")
    print(f"Último integrante añadido: {nombre_nuevo}")
    if nombre_anterior:
        print(f"Integrante anterior: {nombre_anterior}")
    else:
        print("Este es el primer integrante añadido.")

    # Mostramos la lista actualizada
    print("\n--- Lista actualizada de integrantes ---")
    # Se actualizó el nombre de la lista
    for nombre in lista_nombres_estudiantes:
        print(nombre)

# Cuando terminen de ingresar los nombres damos print a la lista final
print("\n--- Lista final de integrantes del grupo Ingenidea ---")
# Se actualizó el nombre de la lista
for nombre in lista_nombres_estudiantes:
    print(nombre)

print("\n¡Estos son todos los miembros!")


# Código del juego adivina el número secreto
# El número secreto ahora es fijo: 6 pero puede ser cambiado por cualquier otro número entero.
numero_secreto = 6

print("¡Bienvenido al juego Adivina el Número Secreto!")
print("Estoy pensando en el...")

# Iniciamos la variable adivinanza con un valor diferente al número secreto para que el bucle WHILE se ejecute al menos una vez.
adivinanza = 0 

# Bucle que continua mientras la adivinanza no sea correcta
while adivinanza != numero_secreto:
    try:
        # Pide al usuario que adivine el número.
        adivinanza = int(input("Ingresa el número que crees que es el secreto: "))

        # Aqui le damos una pista si el número no es correcto
        if adivinanza > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.")
        elif adivinanza < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.")

    except ValueError:
        # Maneja el error si el usuario no ingresa un número entero (int)
        print("Ingresa un número entero.")

# Mensaje (print)que aparece cuando el número fue adivinado
print(f"¡Correcto! El número era {numero_secreto}. ¡Felicidades, adivinaste!")



#Codigo lista de comidas bolivianas favoritas
 # Crea una lista llamada comidas_favoritas con los nombres (strings) de tus 3 comidas bolivianas favoritas.
comidas_favoritas = ["Pollo Frito", "Pique Macho", "Milanesa"]

# Imprimimos la lista completa para verificar que se creó bien.
print("Mi lista de comidas favoritas es:")
print(comidas_favoritas)

# Imprime un mensaje que diga: "Mi segunda comida favorita es: [el nombre de la segunda comida]".
print(f"\nMi segunda comida favorita es: {comidas_favoritas[1]}")

# Usamos len() al imprimir un mensaje 
# len() nos dara la cantidad de elementos en la lista.
print(f"Mi lista de comidas favoritas tiene {len(comidas_favoritas)} elementos.")



#Codigo para calcular el promedio de notas
# Creamos una lista llamada lista_mis_notas con las notas.
lista_mis_notas = [60.5, 74, 80.5, 90.5,]
# Creamos una variable suma_total inicializada en 0.
suma_total = 0

# Usamos un bucle for para recorrer lista_mis_notas.
# En cada iteración, añade la nota actual a suma_total.
for nota in lista_mis_notas:
    suma_total = suma_total + nota 

# Calcula el promedio: promedio = suma_total / len(lista_mis_notas).
# len(lista_mis_notas) nos da la cantidad de elementos en la lista.
promedio = suma_total / len(lista_mis_notas)

# Imprime(print) la suma total y el promedio.
print(f"Mis notas son: {lista_mis_notas}")
print(f"La suma total de las notas es: {suma_total:.2f}") 
print(f"El promedio de las notas es: {promedio:.2f}") # :.2f para mostrar dos decimales


# acumulador sumar elementos
def sumar_elementos(lista_numeros):
    acumulador_suma = 0
    for numero in lista_numeros:
        acumulador_suma += numero  
    return acumulador_suma
mis_numeros = [10, 5, 20, 15, 8, 25]
resultado_suma = sumar_elementos(mis_numeros)

print(f"La lista de números es: {mis_numeros}")
print(f"La suma total es: {resultado_suma}")



#Codigo encontrar mayor o numero mas grande en lista
lista_numeros_grande = [45, 12, 78, 33, 90, 67, 21]
if not lista_numeros_grande:
    print("La lista está vacía, no se puede encontrar el número más grande.")
else:
    mayor_temporal = lista_numeros_grande[0]
    for i in range(1, len(lista_numeros_grande)):
        elemento_actual = lista_numeros_grande[i]
        if elemento_actual > mayor_temporal:
            mayor_temporal = elemento_actual
    print(f"\nLa lista de números es: {lista_numeros_grande}")
    print(f"El número más grande en la lista es: {mayor_temporal}")



#Codigo de Invertir lista con range, append
def invertir_lista(lista_original):
    lista_invertida = []
    for i in range(len(lista_original) - 1, -1, -1):
        lista_invertida.append(lista_original[i])
    return lista_invertida