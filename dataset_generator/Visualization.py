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


##############################################################
# concatenate several househoulds that are the one after the other chronologically in one household


# Read the CSV file
filepath = 'target/9/HERON9.csv'
df2 = pd.read_csv(filepath, sep=',')
print(df2.head(2))
print(df2.tail(2))
print(df2.shape)
#
# Read the CSV file
filepath = 'target/10/HERON10.csv'
df3 = pd.read_csv(filepath, sep=',')
print(df3.head(2))
print(df3.tail(2))
print(df3.shape)
#
# # Read the CSV file
# filepath = 'target/4/HERON4.csv'
# df4 = pd.read_csv(filepath, sep=',')
# print(df4.head(2))
# print(df4.tail(2))
# print(df4.shape)
#
# # Read the CSV file
# filepath = 'target/5/HERON5.csv'
# df5 = pd.read_csv(filepath, sep=',')
# print(df5.head(2))
# print(df5.tail(2))
# print(df5.shape)
#
# # Read the CSV file
# filepath = 'target/6/HERON6.csv'
# df6 = pd.read_csv(filepath, sep=',')
# print(df6.head(2))
# print(df6.tail(2))
# print(df6.shape)
#
# filepath = 'target/7/HERON7.csv'
# df7 = pd.read_csv(filepath, sep=',')
# print(df7.head(2))
# print(df7.tail(2))
# print(df7.shape)
#
# List of file paths
filepaths = [
    'target/9/HERON9.csv',
    'target/10/HERON10.csv'
]

# Create an empty list to store dataframes
dfs = []

# Read each CSV file and store the dataframes in the list
for filepath in filepaths:
    df = pd.read_csv(filepath, sep=',')
    dfs.append(df)

# Concatenate the dataframes
merged_df = pd.concat(dfs, ignore_index=True)

print(merged_df.head(2))
print(merged_df.tail(2))
print(merged_df.shape)
print(f"Total Columns: {len(merged_df.columns)}")
# # csv export
# merged_df.to_csv(f'target/1/HERON1.csv', index=False)


############################################################


# # Read the CSV file
# filepath = 'target/2/HERON2.csv'
# df = pd.read_csv(filepath, sep=',')
# print(df.head(2))
# print(df.tail(2))
# print(df.shape)
#
# # Calculate the sum of the 'main' column
# main_column_sum = df['mains'].sum()
# print(f"kwh per day: {main_column_sum:.3f}")
#
# # Set the figure size
# plt.figure(figsize=(12, 6))
#
# # Plot the mains data
# df.iloc[:, 1].plot(label="mains")
#
# # Plot the other devices of interest
# device_columns = [2, 3, 4, 5, 6, 7, 10]
# device_labels = ["wm", "dw", "ac", "dryer", "fridge", "iron", "router"]
#
# for i, col in enumerate(device_columns):
#     df.iloc[:, col].plot(label=device_labels[i])
#
# # Set x-ticks for each hour of the day
# num_hours = 24
# tick_positions = range(0, df.shape[0], int(df.shape[0] / num_hours))
# tick_labels = [f"{hour:02}:00" for hour in range(num_hours)]
#
# plt.xticks(tick_positions, tick_labels, rotation=90)
#
# # Set labels, legend, and title
# plt.legend(loc='best')
# plt.title('1 Day of SynD')
# plt.ylabel("kwh")
# plt.xlabel("Hours (h)")
#
# # # Save and show the plot
# # plt.savefig('figures/1 Day of SynD.pdf', format='pdf', bbox_inches='tight')
# # plt.savefig('figures/1 Day of SynD.png', format='png', dpi=300, bbox_inches='tight')
# plt.show()





