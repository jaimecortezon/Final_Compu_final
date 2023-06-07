## Ejercicio 1:

#Carga el dataset Titanic.csv. Muestra las primeras 10 filas, las últimas 5 filas y una muestra aleatoria de 5 filas. Finalmente, renombra las columnas a términos equivalentes en español según tu criterio.

#Verifica los tipos de datos de todas las columnas y calcula los estadísticos descriptivos para todas las columnas numéricas.

#Crea una función que reciba como argumentos una columna de un DataFrame, un valor umbral y una dirección (mayor o menor). Esta función debe devolver la media de los valores en la columna que son mayores o menores que el valor umbral, según la dirección proporcionada.

#Utiliza esta función para calcular la tarifa media ('Fare') de los pasajeros cuya edad ('Age') es mayor y menor que 30. Del mismo modo, calcula la edad media de los pasajeros que pagaron una tarifa que es mayor y menor que el promedio de todas las tarifas.


#Importamos las librerias necesarias
import pandas as pd


#Cargamos el dataset
df = pd.read_csv('titanic.csv')

#Mostramos las primeras 10 filas
print(df.head(10))

#Mostramos las ultimas 5 filas
print(df.tail(5))

#Mostramos una muestra aleatoria de 5 filas
print(df.sample(5))

#Renombramos las columnas a terminos equivalentes en español segun nuestro criterio
#df.columns = ['Id_Pasajero', 'Sobrevivio', 'Clase', 'Nombre', 'Sexo', 'Edad', 'Hermanos_Esposos', 'Padres_Hijos', 'Ticket', 'Tarifa', 'Cabina', 'Embarque']


#Verificamos los tipos de datos de todas las columnas
print(df.dtypes)

#Calculamos los estadisticos descriptivos para todas las columnas numericas
print(df.describe())

#Creamos la funcion que recibe como argumentos una columna de un DataFrame, un valor umbral y una direccion (mayor o menor). Esta funcion debe devolver la media de los valores en la columna que son mayores o menores que el valor umbral, segun la direccion proporcionada.
def media(df, columna, valor, direccion):
    if direccion == 'mayor':
        return df[df[columna] > valor][columna].mean()
    elif direccion == 'menor':
        return df[df[columna] < valor][columna].mean()
    else:
        return 'Error'
    
#Utilizamos esta funcion para calcular la tarifa media ('Fare') de los pasajeros cuya edad ('Age') es mayor y menor que 30. Del mismo modo, calculamos la edad media de los pasajeros que pagaron una tarifa que es mayor y menor que el promedio de todas las tarifas.
print(media(df, 'Age', 30, 'mayor'))
print(media(df, 'Age', 30, 'menor'))
print(media(df, 'Fare', df['Fare'].mean(), 'mayor'))
print(media(df, 'Fare', df['Fare'].mean(), 'menor'))
