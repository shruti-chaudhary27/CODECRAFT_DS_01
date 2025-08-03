import matplotlib.pyplot as plt
import numpy as np

# Generate random age data
np.random.seed(42)
ages = np.random.randint(15, 60, size=100)

# Create a histogram
plt.figure(figsize=(10, 6))
plt.hist(ages, bins=10, color='skyblue', edgecolor='black')
plt.title('Age Distribution in a Population')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()

# Save the chart
plt.savefig('age_distribution_histogram.png')
plt.show()
