## Ejercicio 2:

#Muestra cuántos registros hay por cada clase de pasaje (Pclass) y encuentra el pasajero con la edad más alta.

#Realiza una matriz de covarianza con todas las columnas numéricas.

#Para cada clase de pasaje (Pclass), filtra el DataFrame para incluir solo a los pasajeros de esa clase.

#Usa Matplotlib para hacer un histograma de las tarifas ('Fare') de los pasajeros de cada clase.

#Asegúrate de que cada histograma tenga un título que indique la clase de pasajero y que todos los histogramas estén en la misma figura.




#Importamos las librerias necesarias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Cargamos el dataset
df = pd.read_csv('titanic.csv')

#Mostramos cuantos registros hay por cada clase de pasaje (Pclass)
print(df['Pclass'].value_counts())

#Encontramos el pasajero con la edad mas alta
print(df[df['Age'] == df['Age'].max()])
print(df[df['Age'] == df['Age'].max()][['Name', 'Age']])
print(df[df['Age'] == df['Age'].max()][['Name', 'Age']].values)

#Realizamos una matriz de covarianza con todas las columnas numericas
print(df.cov())

#Para cada clase de pasaje (Pclass), filtramos el DataFrame para incluir solo a los pasajeros de esa clase.
print(df[df['Pclass'] == 1])
print(df[df['Pclass'] == 2])
print(df[df['Pclass'] == 3])

#Usamos Matplotlib para hacer un histograma de las tarifas ('Fare') de los pasajeros de cada clase. 
#Asegurate de que cada histograma tenga un titulo que indique la clase de pasajero y que todos los histogramas esten en la misma figura.
plt.hist(df[df['Pclass'] == 1]['Fare'], label = 'Clase 1')
plt.hist(df[df['Pclass'] == 2]['Fare'], label = 'Clase 2')
plt.hist(df[df['Pclass'] == 3]['Fare'], label = 'Clase 3')
plt.legend()
plt.show()
