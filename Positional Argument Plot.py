import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Set_1 = {
    'S[0]': [0, 1, 10, 11, 100, 101, 110, 111, 110, 11, 0, 11, 110, 1001, 1100, 1111],
    'S[1]': [1111, 1100, 1001, 110, 11, 0, 11, 110, 101, 0, 101, 100, 11, 10, 1, 0],
    'S[10]': [1111, 1011, 111, 11, 1, 101, 11, 1, 1, 11, 101, 1, 11, 111, 1011, 1111],
    'S[11]': [0, 1, 10, 11, 10, 101, 0, 101, 100, 11, 0, 11, 0, 101, 1010, 1111],
    'S[100]': [1111, 1010, 101, 0, 1, 0, 11, 100, 11, 0, 101, 10, 11, 10, 1, 0],
    'S[101]': [1111, 1001, 11, 11, 1, 101, 11, 1, 1, 11, 101, 1, 11, 11, 1001, 1111],
    'S[110]': [0, 1, 10, 11, 0, 101, 0, 11, 10, 11, 0, 1, 0, 1, 1000, 1111],
    'S[111]': [1111, 1000, 1, 0, 1, 101, 11, 10, 1, 0, 101, 0, 11, 10, 1, 1111]
}

df_1 = pd.DataFrame(Set_1)

Set_2 = {
    'S[1000]': [1111, 111, 1, 11, 1, 101, 11, 1, 1, 11, 101, 1, 11, 1, 111, 1111],
    'S[1001]': [0, 1, 0, 11, 0, 101, 0, 1, 0, 11, 0, 1, 0, 1, 110, 1111],
    'S[1010]': [1111, 110, 1, 0, 1, 0, 11, 0, 1, 0, 101, 0, 11, 0, 1, 0],
    'S[1011]': [1111, 101, 1, 11, 1, 101, 11, 1, 1, 11, 101, 1, 11, 1, 101, 1111],
    'S[1100]': [0, 1, 0, 11, 0, 101, 0, 1, 0, 11, 0, 1, 0, 1, 100, 1111],
    'S[1101]': [1111, 100, 1, 0, 1, 0, 11, 0, 1, 0, 101, 0, 11, 0, 1, 1111],
    'S[1110]': [1111, 11, 1, 11, 1, 101, 11, 1, 1, 11, 101, 1, 11, 1, 11, 1111],
    'S[1111]': [0, 1, 0, 11, 0, 101, 0, 1, 0, 11, 0, 1, 0, 1, 10, 1111]
}

df_2 = pd.DataFrame(Set_2)

import seaborn as sns

# Concatenate the values from both sets
x_values = np.concatenate(list(Set_1.values()))
y_values = np.concatenate(list(Set_2.values()))

# Create a DataFrame with the concatenated values
data = pd.DataFrame({'Set_1': x_values, 'Set_2': y_values})

# Count the occurrences of each pair of values
counts = data.groupby(['Set_1', 'Set_2']).size().reset_index(name='Count')

# Create a pivot table with the counts
pivot_table = counts.pivot(index='Set_2', columns='Set_1', values='Count')

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='g')
plt.title('Binary Values Heatmap')
plt.xlabel('Set_1')
plt.ylabel('Set_2')

# Invert the y-axis
plt.gca().invert_yaxis()

plt.show()

