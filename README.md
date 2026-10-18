# PROYECTO1
ESTE ES EL PARCIAL NUMERO 3 DE LA MATERIA ESTRUCTURA DE DATOS 


Proyecto Parcial 3: Algoritmos de Búsqueda y Recuperación de Datos






Asignatura: Estructura de Datos








Docente: Daniel Alexis Nieto Mora






Institución Universitaria ITM









Equipo 3: David Esteban Urrutia Morales y Luis Andrés Llerena Arredondo



1. Descripción General del Proyecto
Este proyecto analiza, implementa y compara los algoritmos fundamentales de búsqueda y recuperación de información: Búsqueda Lineal, Búsqueda Binaria y Tablas Hash. Se evalúa su comportamiento teórico, su complejidad asintótica y su rendimiento práctico utilizando un script eficiente en Python puro, sin dependencias externas.


2. Marco Teórico y Matemático
2.1 Búsqueda Lineal (Secuencial)
Concepto: Recorre la estructura de datos elemento por elemento desde el inicio hasta encontrar el objetivo o llegar al final.
Requisitos: No requiere precondiciones sobre los datos (pueden estar desordenados).
Complejidad Temporal:
Mejor Caso ($\Omega(1)$): El elemento se encuentra en la primera posición.
Caso Promedio ($\Theta(n)$): El elemento se encuentra en el medio.
Peor Caso ($O(n)$): El elemento está al final o no existe.
Complejidad Espacial: $O(1)$ (operación in situ).
2.2 Búsqueda Binaria
Concepto: Algoritmo de "Divide y Vencerás" que divide repetidamente el espacio de búsqueda a la mitad.
Requisitos: El conjunto de datos debe estar estrictamente ordenado.
Invariantes y Terminación:
Invariante del ciclo: Si el elemento buscado existe en el arreglo, se encuentra obligatoriamente en el rango cerrado $[\text{izquierda}, \text{derecha}]$.
Condición de terminación: El ciclo finaliza cuando $\text{izquierda} > \text{derecha}$ o cuando se halla el elemento.
Complejidad Temporal:
Mejor Caso ($\Omega(1)$): El elemento está justo en el punto medio inicial.
Caso Promedio y Peor Caso ($O(\log n)$): Halvaciones sucesivas del espacio de búsqueda.
Complejidad Espacial: $O(1)$ en implementación iterativa.
2.3 Comparativa con Tablas Hash
Concepto: Las tablas hash transforman claves en índices mediante una función hash (implementadas mediante diccionarios en Python).
Complejidad de Búsqueda: $O(1)$ en el caso promedio, aunque puede degradarse a $O(n)$ en el peor caso debido a colisiones.


3. Dataset Utilizado
Nombre: Simulación de Catálogo Bibliográfico (Inspirado en Kaggle Open Book Library).
Descripción: Conjunto de 10,000 registros numéricos únicos generados aleatoriamente para evaluar con precisión el número de comparaciones y los tiempos en milisegundos.


4. Tecnologías Utilizadas
Lenguaje: Python 3.x (Puro)
Librerías Nativas:
random (Generación de muestras y datasets aleatorios)
time (Medición precisa de rendimiento en milisegundos)


5. Implementación en Python (main.py)
El script implementa desde cero la lógica algorítmica solicitada:

import random

import time

def busqueda_lineal(arr, objetivo):

    comparaciones = 0

    for i in range(len(arr)):

        comparaciones += 1

        if arr[i] == objetivo:

            return i, comparaciones

    return -1, comparaciones

def busqueda_binaria(arr, objetivo):

    izquierda = 0

    derecha = len(arr) - 1

    comparaciones = 0

    while izquierda <= derecha:

        comparaciones += 1

        medio = (izquierda + derecha) // 2

        if arr[medio] == objetivo:

            return medio, comparaciones

        elif arr[medio] < objetivo:

            izquierda = medio + 1

        else:

            derecha = medio - 1

    return -1, comparaciones

def busqueda_tabla_hash(tabla_hash, objetivo):

    inicio = time.time()

    if objetivo in tabla_hash:

        tiempo = (time.time() - inicio) * 1000

        return True, 1, tiempo

    return False, 1, 0.0

def ejecutar_proyecto():

    print("================================================================")

    print("      COMPARATIVA DE ALGORITMOS DE BÚSQUEDA (EQUIPO 3)        ")

    print("================================================================")

    total_registros = 10000

    print(f"Generando {total_registros:,} registros aleatorios...")

    datos_desordenados = random.sample(range(1, 1000000), total_registros)

    datos_ordenados = sorted(datos_desordenados)

    tabla_hash = {val: f"Libro_Item_{val}" for val in datos_desordenados}

    objetivo = datos_ordenados[int(total_registros * 0.85)]

    print(f"Elemento objetivo a buscar: {objetivo}\n")

    

    t_inicio = time.time()

    idx_lin, comp_lin = busqueda_lineal(datos_desordenados, objetivo)

    tiempo_lin = (time.time() - t_inicio) * 1000

    print(f"[1] Búsqueda Lineal -> Índice: {idx_lin}, Comparaciones: {comp_lin:,}, Tiempo: {tiempo_lin:.6f} ms")

    

    t_inicio = time.time()

    idx_bin, comp_bin = busqueda_binaria(datos_ordenados, objetivo)

    tiempo_bin = (time.time() - t_inicio) * 1000

    print(f"[2] Búsqueda Binaria -> Índice: {idx_bin}, Comparaciones: {comp_bin:,}, Tiempo: {tiempo_bin:.6f} ms")

    

    encontrado, comp_h, tiempo_hash = busqueda_tabla_hash(tabla_hash, objetivo)

    print(f"[3] Tabla Hash -> Encontrado: {encontrado}, Operaciones: {comp_h}, Tiempo: {tiempo_hash:.6f} ms")

    print("================================================================")

if __name__ == "__main__":

    ejecutar_proyecto()


6. Resultados y Conclusiones
La búsqueda lineal recorre un promedio considerable de elementos ($O(n)$), resultando ineficiente en catálogos grandes.
La búsqueda binaria reduce drásticamente el número de comparaciones a un orden logarítmico ($O(\log n)$), requiriendo precondiciones de ordenamiento.
Las tablas hash proporcionan un acceso casi instantáneo ($O(1)$) mediante funciones de dispersión internas, siendo altamente óptimas para sistemas de recuperación de información.


7. Autores
David Esteban Urrutia Morales
Luis Andrés Llerena Arredondo
Equipo 3 - Estructura de Datos (Grupo 190304018-1)
