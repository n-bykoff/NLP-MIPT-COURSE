import numpy as np
import matplotlib.pyplot as plt


def a(x):
    return 0.75 - 0.25 * x


def c(x):
    return 1.5 - x


def d(x):
    return 2 - 4 * x


def solve_system(sigma=0.5):
	M = np.array([[1, 1, 1, 1], [-(1 + sigma), sigma, -1, 1], 
	             [(sigma - 2) ** 2, sigma ** 2, 1, 1], [(sigma - 2) ** 3, sigma ** 3, -1, 1]])
	V = np.array([1, -sigma, sigma ** 2, -sigma ** 3])

	solve = np.linalg.solve(M, V)

	print('Система:')
	print(M, V, '\n')

	print(f'Решение: {solve}')


def plot_graph(type='1st'):
	x = np.linspace(-10, 10, 1000, endpoint=True)

	y_1 = a(x)
	y_2 = d(x)
	y_3 = c(x)

	plt.figure(figsize=(20, 15))

	plt.plot(x, y_1, 'red', x, y_2, 'red', linewidth=3)
	
	if type == '2nd':
		plt.plot(x, y_3, 'orange', linewidth=3)

	plt.fill_between(x, y_1, where=((x <= 1 / 3)), color='green')
	plt.fill_between(x, y_2, where=((y_2 < 0.75)), color='green')

	plt.xlim([0, 1])
	plt.ylim([0, 1.2])
	plt.grid()

	plt.show()
