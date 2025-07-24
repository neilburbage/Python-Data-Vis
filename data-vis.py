import numpy as np
import matplotlib.pyplot as plt

# Data Visualization Libraries

# Line Plot

x = [1, 2, 3, 4, 5]
y = [10, 12, 5, 8, 7]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot Example')
plt.show()

# Scatter Plot

plt.scatter(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Example')
plt.show()

categories = ['A', 'B', 'C', 'D']
values = [25, 30, 15, 20]

plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot Example')
plt.show()

age = [15, 20, 25, 30, 35, 40, 45, 50]

plt.boxplot(age)
plt.xlabel('Box Plot')
plt.title('Box Plot Example')
plt.show()