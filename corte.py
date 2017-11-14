import pandas as pd 
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

datos = pd.read_csv('./Delito_Hurto_Celulares.csv')
print(datos.head(50))
#print(datos.describre())

#datosResumidos = datos[['Header1', 'Header2', 'Header3']]
print(datos.corr())

fig = plt.gcf()
datos.plot.scatter('DIA', 'HORA')
fig.savefig('out.png')