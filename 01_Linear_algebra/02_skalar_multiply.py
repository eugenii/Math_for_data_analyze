import numpy as np

# Стоимость проекта
k = np.array([500, 2000, 5000, 4500])
client_list = np.array([20, 0.5, 3, 60])

result = k @ client_list

result_2 = k.dot(client_list)

print(result)

assert result == result_2, "error in dot product"