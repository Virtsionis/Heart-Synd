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

# Read the CSV file
filepath = 'target/1/HERON1.csv'
df = pd.read_csv(filepath, sep=',')

# Calculate the sum of the 'main' column
main_column_sum = df['mains'].sum()
print(f"kwh per day: {main_column_sum:.3f}")

# Set the figure size
plt.figure(figsize=(12, 6))

# Plot the mains data
df.iloc[:, 1].plot(label="mains")

# # Plot the other devices of interest
# device_columns = [2, 3, 4, 5, 6, 7, 10]
# device_labels = ["wm", "dw", "ac", "dryer", "fridge", "iron", "router"]

# for i, col in enumerate(device_columns):
#     df.iloc[:, col].plot(label=device_labels[i])

# Set x-ticks for each hour of the day
num_hours = 24
tick_positions = range(0, df.shape[0], int(df.shape[0] / num_hours))
tick_labels = [f"{hour:02}:00" for hour in range(num_hours)]

plt.xticks(tick_positions, tick_labels, rotation=90)

# Set labels, legend, and title
plt.legend(loc='best')
plt.title('1 Day of SynD')
plt.ylabel("kwh")
plt.xlabel("Hours (h)")

# # Save and show the plot
# plt.savefig('figures/1 Day of SynD.pdf', format='pdf', bbox_inches='tight')
# plt.savefig('figures/1 Day of SynD.png', format='png', dpi=300, bbox_inches='tight')
plt.show()





