import numpy as np
import matplotlib.pyplot as plt

mean = 0
std_dev = 1
num_samples = 1000

data = np.random.normal(mean, std_dev, num_samples)

plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title('Гистограмма нормального распределения')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.show()
