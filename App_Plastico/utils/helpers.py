import datetime

def generate_recommendations(cursor, user_id):
    cursor.execute('SELECT fecha, cantidad, descripcion FROM consumo WHERE user_id = %s', (user_id, ))
    consumos = cursor.fetchall()

    if not consumos:
        return ["No se encontraron datos de consumo para generar recomendaciones."]

    recommendations = []
    for consumo in consumos:
        fecha, cantidad, descripcion = consumo
        recommendations.append(f"Considera reducir tu consumo de {descripcion} si es mayor a {cantidad}.")

    # Guardar las recomendaciones en la base de datos
    today = datetime.date.today()
    for rec in recommendations:
        cursor.execute('INSERT INTO sugerencias (user_id, recomendacion, fecha) VALUES (%s, %s, %s)',
                        (user_id, rec, today))
    return recommendations
