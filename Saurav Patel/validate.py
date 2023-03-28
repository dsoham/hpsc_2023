import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Define the values of wnum and time
wnum = 1.00
time = np.arange(0, 1.25, 0.05)

# Calculate the values of np.cosh((wnum)*(time))
y = np.cosh((wnum)*(time))

# Plot the curve
plt.plot(time, y, 'r')

# Set the axis labels and title
plt.xlabel('Time (s)')
plt.ylabel('np.cosh((wnum)*(time))')
plt.title('Cosh Curve')


# Show the plot
#plt.show()

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('110.csv')

# Add 0.02 to each value in the 'avg(alpha.phase1)' column
df['avg(alpha.phase1)'] = df['avg(alpha.phase1)'] + 0.89


dk = pd.read_csv('Default Dataset.csv')
plt.plot(dk['a'],dk['b'],'g')


# Plot the modified data on a linear scale
plt.plot(df['Time'], df['avg(alpha.phase1)'])
plt.xlabel('Time')
plt.ylabel('Growth Rate')
plt.title('Comparison Plot')
plt.savefig('_plot1.png', dpi=600)
plt.show()

#plt.savefig('modified_plot.png', dpi=300)