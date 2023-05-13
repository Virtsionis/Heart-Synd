import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

df = pd.read_csv('/home/nikolaos/Desktop/HeartSynD/HeartSynD-main/HeartSynD-main/dataset_generator/target/67/15.csv', sep ='\t')
df.columns = ['Datetime', 'power']
timestamps = df['Datetime'].tolist()

# str to datetime oneliner
list_of_converted_datetimes = [datetime.strptime(t, '%Y-%m-%d %H:%M:%S') - relativedelta(days=219) for t in timestamps]
df['Datetime'] = list_of_converted_datetimes

#csv export to path
df.to_csv('/home/nikolaos/Desktop/HeartSynD/HeartSynD-main/HeartSynD-main/dataset_generator/target/67/15.csv', index=False)

