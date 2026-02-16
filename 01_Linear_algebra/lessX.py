import numpy as np
from numpy.linalg import norm

a = np.array([6, 4, 9, 8])
b = np.array([8, 4, 10, 12])

q = -3 * a + 2.5 * b

print(norm(q))

s = np.array([5, 3.1, 8, 7, 0])
w = np.array([13, 2.6, 4, 9, 7])

#  cos_X = np.dot(s, w) / (norm(s) * norm(w))  # (то же самое)
cos_X = s @ w / (norm(s) * norm(w))
angle = np.rad2deg(np.arccos(cos_X))
print("Косинус угла между s и w:", cos_X)
print("Сам угол:", angle)

print("Задача 8")

A = (-4, 8)
B = (-15, 15)
C = (-10, -7)
D = (3, -4)

DA = np.array([A[0] - D[0], A[1] - D[1]])
DC = np.array([C[0] - D[0], C[1] - D[1]])
# print(DA, DC)
cos_angle = DA @ DC / (norm(DA) * norm(DC))
angle = np.arccos(cos_angle)  # допишите код для вычисления в радианах здесь
print("Косинус угла:", cos_angle)  # допишите код здесь
print("Сам угол:", np.rad2deg(angle))  # допишите код здесь