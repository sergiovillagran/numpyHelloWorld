import numpy as np
import matplotlib as mpl
mpl.use('Agg');
import matplotlib.pyplot as plt
anlos = np.loadtxt('anlos.txt', delimiter = ';')
print(len(anlos))
poblaciones = np.loadtxt('poblaciones.txt', delimiter = ';')
print(len(poblaciones))
#plt(anlos, poblaciones)
plt.scatter(anlos, poblaciones)
plt.xlabel('Anio')
plt.ylabel('poblaciones')
plt.savefig('scatterPop.png')

#estaturas 		= [1.70 , 1.55, 1.70, 1.80]
# pesos			= [90, 50, 85, 84]
# num_estaturas 	= np.array(estaturas)
# num_pesos		= np.array(pesos)

# plt.scatter(num_estaturas, num_pesos)
# plt.xlabel('estaturas')
# plt.ylabel('pesos')
# plt.savefig('scatterPop_test.png')
#print(type (poblaciones))
#matriz = np.loadtxt('matriz.txt', delimeter = ',', skiprows = 1, usecols = (0,2))
#print(matriz);