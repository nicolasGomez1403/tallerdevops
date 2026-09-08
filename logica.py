def calculate_indicadores_rendimento(notas):
    if not notas:
        return {
            "total_evaluaciones": 0,
            "promedio": 0.0,
            "aprobados": 0,
            "reprobados": 0,
            "tasa_aprobacion": 0.0,
            "rango_calificaciones": 0.0
        }
    
    total = len(notas)
    promedio = sum(notas) / total
    aprobados = sum(1 for nota in notas if nota >= 60)
    reprobados = total - aprobados
    tasa_aprobacion = (aprobados / total) * 100
    rango = max(notas) - min(notas)
    
    return {
        "total_evaluaciones": total,
        "promedio": promedio,
        "aprobados": aprobados,
        "reprobados": reprobados,
        "tasa_aprobacion": tasa_aprobacion,
        "rango_calificaciones": rango
    }
