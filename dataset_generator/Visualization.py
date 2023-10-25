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
          '00:00', '08:00', '16:00'
          '00:00', '08:00', '16:00',
          '00:00', '08:00', '16:00', '00:00']

# csv reader
filepath = 'target/1/HERON1.csv'
df = pd.read_csv(filepath, sep=',')
print(df.shape)
print(df.columns)
print(df.head(5))
print(df.tail(5))


# 30 Days slicing
# n = round(day*31)
n = 24*31
df = df.iloc[:n]
print(df.tail(5))
#
# mains
df.iloc[:, 1].plot()

# device of interest - wm
df.iloc[:, 2].plot()

# device of interest -  dw
df.iloc[:, 3].plot()
#
# device of interest -  ac
df.iloc[:, 4].plot()
#
# device of interest -  dryer
df.iloc[:, 5].plot()
#
# device of interest -  fridge
df.iloc[:, 6].plot()
#
# device of interest -  iron
df.iloc[:, 7].plot()

# device of interest -  router
df.iloc[:, 10].plot()

labels = df.iloc[np.linspace(0, df.shape[0]-1, num=len(labels)), 0]
plt.xticks(ticks=np.linspace(0, df.shape[0]-1, num=len(labels)), labels=labels, rotation=90, fontsize=4.5)
# plt.legend(['mains', 'wm'], loc='best')
plt.legend(["mains", "wm", "dw", "ac", "dryer", "fridge", "iron", "router"], loc='best')
plt.title('SynD_all_appliances 30 Days')
plt.savefig('figures/SynD_all_appliances_30_days.pdf', format='pdf', bbox_inches='tight')
plt.savefig('figures/SynD_all_appliances_30_days.png', format='png', dpi=300, bbox_inches='tight')
plt.show()





