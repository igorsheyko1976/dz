import numpy as np
import matplotlib.pyplot as plt

data1 = np.random.rand(5)
data2 = np.random.rand(5)

plt.scatter(data1, data2, color='skyblue')
plt.title('Диаграмма рассеяния двух наборов случайных данных')
plt.xlabel('Набор данных 1')
plt.ylabel('Набор данных 2')
plt.show()
