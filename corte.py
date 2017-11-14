import matplotlib as mpl
import pandas as pd 
mpl.use('Agg')
import matplotlib.pyplot as plt

DATA    = pd.read_csv('Delito_Hurto_Celulares.csv', parse_dates= True, index_col= 'FECHA')

# scatter graph
DATA['days'] = DATA.index.day
DATA.plot.scatter('days', 'EDAD')
FIG     = plt.gcf()
FIG.savefig('scatter.png')

# histograma
DATA['month'] = DATA.index.month
DATA['month'].hist() 
FIG     = plt.gcf()
FIG.savefig('histograma.png')

# box
DATA.EDAD.plot.box()
FIG     = plt.gcf()
FIG.savefig('box.png')

# otro 1 pie
victimas_a_pie = DATA['MOVIL VICTIMA'] == "A PIE" 
victimas_a_pie = DATA[victimas_a_pie]
victimas_a_pie['MOVIL AGRESOR'].value_counts().plot.pie()
FIG     = plt.gcf()
FIG.savefig('pie.png')

# otro 2 bar
DATA['MARCA'].value_counts().plot.bar()
FIG     = plt.gcf()
FIG.savefig('bar.png')