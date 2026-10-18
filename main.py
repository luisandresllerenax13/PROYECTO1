import random
import time
from collections.abc import Mapping, Sequence


class Busqueda:
    @staticmethod
    def _validar_entrada(arr: Sequence[int], objetivo: int) -> None:
        if not isinstance(arr, Sequence) or isinstance(arr, (str, bytes, bytearray)):
            raise TypeError("arr debe ser una secuencia de números enteros")
        if isinstance(objetivo, bool) or not isinstance(objetivo, int):
            raise TypeError("objetivo debe ser un número entero")

    @staticmethod
    def busqueda_lineal(arr: Sequence[int], objetivo: int) -> tuple[int, int]:
        Busqueda._validar_entrada(arr, objetivo)
        comparaciones = 0
        for i, valor in enumerate(arr):
            comparaciones += 1
            if valor == objetivo:
                return i, comparaciones
        return -1, comparaciones

    @staticmethod
    def busqueda_binaria(arr: Sequence[int], objetivo: int) -> tuple[int, int]:
        Busqueda._validar_entrada(arr, objetivo)
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

    @staticmethod
    def busqueda_tabla_hash(
        tabla_hash: Mapping[int, object], objetivo: int
    ) -> tuple[bool, int, float]:
        if not isinstance(tabla_hash, Mapping):
            raise TypeError("tabla_hash debe ser un mapeo, por ejemplo un diccionario")
        if isinstance(objetivo, bool) or not isinstance(objetivo, int):
            raise TypeError("objetivo debe ser un número entero")

        inicio = time.perf_counter()
        encontrado = objetivo in tabla_hash
        tiempo_ms = (time.perf_counter() - inicio) * 1000
        return encontrado, 1, tiempo_ms


def ejecutar_proyecto(total_registros: int = 100_000) -> None:
    if isinstance(total_registros, bool) or not isinstance(total_registros, int):
        raise TypeError("total_registros debe ser un número entero")
    if not 1 <= total_registros <= 999_999:
        raise ValueError("total_registros debe estar entre 1 y 999,999")

    print("================================================================")
    print("      COMPARATIVA DE ALGORITMOS DE BÚSQUEDA (EQUIPO 3)        ")
    print("================================================================")
    
    
    print(f"Generando {total_registros:,} registros aleatorios...")
    
    datos_desordenados = random.sample(range(1, 1000000), total_registros)
    datos_ordenados = sorted(datos_desordenados)
    tabla_hash = {val: f"Libro_Item_{val}" for val in datos_desordenados}
    
    
    objetivo = datos_ordenados[int(total_registros * 0.85)]
    print(f"Elemento objetivo a buscar: {objetivo}\n")
    
    
    t_inicio = time.perf_counter()
    idx_lin, comp_lin = Busqueda.busqueda_lineal(datos_desordenados, objetivo)
    tiempo_lin = (time.perf_counter() - t_inicio) * 1000
    print(f"[1] Búsqueda Lineal:")
    print(f"    - Índice encontrado: {idx_lin}")

t_inicio = time.perf_counter()
    idx_bin, comp_bin = Busqueda.busqueda_binaria(datos_ordenados, objetivo)
    tiempo_bin = (time.perf_counter() - t_inicio) * 1000
    print(f"[2] Búsqueda Binaria:")
    print(f"    - Índice encontrado: {idx_bin}")
    print(f"    - Comparaciones realizadas: {comp_bin:,}")
    print(f"    - Tiempo de ejecución: {tiempo_bin:.6f} ms\n")

    encontrado, comp_h, tiempo_hash = Busqueda.busqueda_tabla_hash(tabla_hash, objetivo)
    print(f"[3] Tabla Hash (Diccionario):")
    print(f"    - ¿Encontrado?: {encontrado}")
    print(f"    - Accesos / Operaciones: {comp_h}")
    print(f"    - Tiempo de ejecución: {tiempo_hash:.6f} ms\n")
    print("================================================================")


if __name__ == "__main__":
    try:
        ejecutar_proyecto()
    except (TypeError, ValueError) as error:
        print(f"Error al ejecutar el proyecto: {error}")
