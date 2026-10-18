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
