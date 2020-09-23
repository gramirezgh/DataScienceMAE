import numpy as np
import pandas as pd
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
import statsmodels.api as sm
from math import pi

pob = pd.read_csv('data/poblacion.csv ') # carga de datos poblacionales 1952 - 2007

print(pob.head()) #Mostrando las cabeceras de los datos poblacionales
print('#############################')
print ('Cantidad de filas y columnas ', pob.shape)
print('#############################')
print ('Nombre de las columnas', pob.columns)

pob.describe() #Descripción general de los datos minimo, maximo, etc

pob_Bob = pob[pob["country"] == 'Bolivia'] # Filtrando a Bolivia de la lista de datos poblacionales
print(pob_Bob.head()) #Viendo las primeras 3 lineas
pob_Bob.drop(['country'],axis=1)['population'].plot(kind='bar') #quitando la cabecera 'country' elegiendo el eje 1 y dibujando
                                                                #el crecimiento de poblacion segun cada 2 años
#Filtrando a los paises a ser comparados con Bolivia en los ultimos 55 años
pob_Pe = pob[pob["country"] == 'Peru']
pob_Ar = pob[(pob["country"] == 'Argentina')]
pob_Br = pob[(pob["country"] == 'Brazil')]
pob_Ve = pob[(pob["country"] == 'Venezuela')]

anios = pob_Bob['year'].unique()  # los años van en el eje x
pop_ar = pob_Ar['population'].values  # Valores poblacionales de Argentina
pop_bo = pob_Bob['population'].values  # Valores poblacionales de Bolivia
pop_pe = pob_Pe['population'].values  # Valores poblacionales de Peru
pop_bra = pob_Br['population'].values  # Valores poblacionales de Brasil
pop_ve = pob_Ve['population'].values  # Valores poblacionales de Venezuela

df_plot = pd.DataFrame({'Argentina': pop_ar, 'Bolivia': pop_bo, 'Peru': pop_pe, 'Brazil': pop_bra, 'Venezuela': pop_ve}, index=anios)
df_plot.plot(kind='bar')  # Grafica de paises y su crecimiento en millones entre 1952 - 2007 ==> '55 años'

# Analizando la mayor concentración de población, mediante outliers
pob = pd.read_csv('data/poblacion.csv ')['population']
population_unique, counts = np.unique(pob, return_counts=True)

sizes = counts * 100
colors = ['blue'] * len(population_unique)
colors[-1] = 'red'

plt.axhline(1, color='k', linestyle='--')
plt.scatter(population_unique, np.ones(len(population_unique)), s=sizes, color=colors)
plt.yticks([])
plt.show()

