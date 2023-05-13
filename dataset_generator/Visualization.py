import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

##########################################################################################
# Heron visualization 30 days

hour = round(14400/24)
day = 14400


#visualizations
labels = ['00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00', '00:00']

# house 1
dft1 = pd.read_csv('/home/nikolaos/Desktop/Heart/HeartSynD-main-v2/dataset_generator/target/33/1.csv', sep='\t')
print(dft1.head())


# 30 Days slicing
n = round(day*31)
dft1 = dft1.iloc[:n]
print(dft1.tail(5))

dft1.iloc[:, 1].plot()
labels = dft1.iloc[np.linspace(0, dft1.shape[0]-1, num=len(labels)), 0]
plt.xticks(ticks=np.linspace(0, dft1.shape[0]-1, num=len(labels)), labels=labels, rotation=90, fontsize=6)
plt.legend(['mains'], loc='best')
plt.title('SynD_all_appliances 30 Days')
plt.savefig('/home/nikolaos/Desktop/Heart/Heart_data/SynD_Heron/SynD_all_appliances_30_days.png')
plt.show()





