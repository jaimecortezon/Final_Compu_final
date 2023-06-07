## Ejercicio 3:
#Este array representa un conjunto de datos donde cada fila es un registro y cada columna un campo específico. Los campos son: 'Day', 'Temperature', 'Year', 'Weather_Type', 'Humidity'.

import numpy as np

arr = np.array([
    [12, 25, 2022, 3, 43],
    [15, 28, 2022, 2, 54],
    [18, 29, 2022, 1, 56],
    [20, 30, 2022, 3, 51],
    [22, 31, 2022, 3, 28]
] * 200)


#Preguntas:

#¿Cuántos tipos de clima únicos hay en el DataFrame?
print(arr[:, 3].max())

#¿Cuál es la temperatura más alta que se registra en el DataFrame?
print(arr[:, 1].max())

#¿Cuántos registros se tienen del día 22?
print(arr[arr[:, 0] == 22].shape[0])

#¿Cuál es la temperatura mínima registrada en los días con tipo de clima 3?
print(arr[arr[:, 3] == 3][:, 1].min())

#¿Cuál es la humedad promedio registrada?
print(arr[:, 4].mean())