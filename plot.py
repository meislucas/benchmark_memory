import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
df = pd.read_csv('benchmark_results.csv')

# Convert memory usage to MB
df['read_mem'] = df['read_mem'] / 1024  # Assuming the values are in KB

# Create a bar plot
plt.figure(figsize=(12, 8))

# Get unique libraries and CSV files
libraries = df['library'].unique()
csv_files = df['csv_file'].unique()

# Set the width of the bars
bar_width = 0.2

# Set positions of the bars on the x-axis
r = np.arange(len(csv_files))

# Create bars for each library
for i, library in enumerate(libraries):
    subset = df[df['library'] == library]
    plt.bar(r + i * bar_width, subset['read_mem'], width=bar_width, edgecolor='grey', label=library)

# Add labels and title
plt.xlabel('CSV File')
plt.ylabel('Memory Usage (MB)')
plt.title('Memory Usage by Library and CSV File Size')
plt.xticks(r + bar_width * (len(libraries) - 1) / 2, csv_files, rotation=45)
plt.legend()

# Save the plot as an image file
plt.tight_layout()
plt.savefig('memory_usage_bar_plot.png')

# Show the plot
plt.show()