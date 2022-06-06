#%%
#CARBOHYDRATE CALCULATOR

import numpy as np
import pandas as pd

#table = np.genfromtxt(fname='tabla_nutricional.csv', delimiter=',')
table = pd.read_csv(r'C:\Users\juand\Design in Biomedical Engineering\Diabetes App\tabla_nutricional.csv')

#print("¿Que vas a comer el dia de hoy?")
comida = input('¿Desayuno, almuerzo o cena?')
escoger = input("Presiona 1 si quieres calcular nueva comida, presiona 2 si quieres escoger una comida guardada")
if escoger == "1":
    alimento1 = input(" Escribe tu primer alimento")
    peso1 = float(input('¿Cuanto pesa tu alimento en gramos?'))
    filter1= table.loc[(table['Alimento'] == alimento1)]
    valor1= filter1['B']
    valor1= float(valor1.to_numpy())
    alimento2 = input(" Escribe tu segundo alimento")
    peso2 = float(input('¿Cuanto pesa tu alimento en gramos?'))
    filter2 = table.loc[(table['Alimento'] == alimento2)]
    valor2= filter2['B']
    valor2 = float(valor2.to_numpy())
    adicional = input(" Alimento adicional? (yes/no)") 
    if adicional == 'yes':
        alimento3 = input(" Escribe tu tercer alimento")
        peso3 = float(input('¿Cuanto pesa tu alimento?'))
        filter3 = table.loc[(table['Alimento'] == alimento3)]
        valor3= filter3['B'] 
        valor3= float(valor3.to_numpy())
    elif adicional == 'no':
        alimento3 = 0
        peso3 = 0
        valor3 = 0


peso_total1 = valor1 * peso1
peso_total2 = valor2 * peso2
peso_total3 = valor3 * peso3
peso_definitivo = round(peso_total1 + peso_total2 + peso_total3)


print('Tu ' + comida + ' contiene aproximadamente {:} gramos de carbohidratos'.format(peso_definitivo))