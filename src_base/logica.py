def calcular_indicadores_rendimiento(notas):
    """
    Calcula indicadores de rendimiento académico sobre una lista de calificaciones.

    TODO: Completa la lógica de esta función para que pasen las pruebas unitarias.

    Requerimientos:
    1. Si 'notas' está vacía ([]), retornar exactamente el siguiente diccionario:
       {
           "total_evaluaciones": 0,
           "promedio": 0.0,
           "aprobados": 0,
           "reprobados": 0,
           "tasa_aprobacion": 0.0,
           "rango_calificaciones": 0.0
       }

    2. Si 'notas' contiene calificaciones (números flotantes o enteros):
       - 'total_evaluaciones': Cantidad de notas en la lista.
       - 'promedio': Promedio aritmético redondeado a 2 decimales usando round(suma / total, 2).
       - 'aprobados': Cantidad de notas mayores o iguales a 3.0 (nota >= 3.0).
       - 'reprobados': Cantidad de notas menores a 3.0 (nota < 3.0).
       - 'tasa_aprobacion': Porcentaje de notas aprobadas frente al total de evaluaciones,
                            redondeado a 2 decimales: round((aprobados / total_evaluaciones) * 100, 2).
       - 'rango_calificaciones': Diferencia entre la nota más alta y la más baja de la lista,
                                 redondeada a 2 decimales: round(max(notas) - min(notas), 2).

    3. Retornar el diccionario con las 6 claves calculadas.
    """
    # --- ESCRIBE TU CÓDIGO AQUÍ ---
    pass
