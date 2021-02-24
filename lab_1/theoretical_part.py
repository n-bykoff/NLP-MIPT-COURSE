import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def a(b):
    return 0.75 - 0.25 * b


def c(b):
    return 1.5 - b


def d(b):
    return 2 - 4 * b


def solve_system(sigma=0.5):
	M = np.array([[1, 1, 1, 1], [-(1 + sigma), sigma, -1, 1], 
	             [(sigma - 2) ** 2, sigma ** 2, 1, 1], [(sigma - 2) ** 3, sigma ** 3, -1, 1]])
	V = np.array([1, -sigma, sigma ** 2, -sigma ** 3])

	solve = np.linalg.solve(M, V)

	print('Система:')
	print(M, V, '\n')

	print(f'Решение: {solve}')


def plot_graph(type='1st'):
	mpl.style.use('seaborn')

	x = np.linspace(-10, 10, 1000, endpoint=True)
	x_s = [0, 0, 1/2]
	y_s = [0, 3/4, 0]

	x_l = [1/3]
	y_l = [2/3]

	x_3rd = [0.5]
	y_3rd = [1]

	x_fr_2nd = [0.583]
	y_fr_2nd = [0.917]


	y_1 = a(x)
	y_2 = d(x)
	y_3 = c(x)

	plt.figure(figsize=(15, 12))

	plt.vlines(0, -0.05, 1.2, 'darkblue', linewidth=3)
	plt.hlines(0, -0.05, 1, 'darkblue', linewidth=3)
	plt.plot(x, y_1, 'darkblue', x, y_2, 'darkblue', linewidth=3)
	
	if type == '2nd':
	    plt.plot(x, y_3, 'orchid', linewidth=3)
	elif type == '3rd':
	    plt.plot(x, y_3, 'orchid', linewidth=3)
	    plt.scatter(x_s, y_s, s=200, color='crimson', zorder=3)
	    plt.scatter(x_l, y_l, s=200, color='crimson', zorder=3)
	    plt.scatter(x_3rd, y_3rd, color='brown', s=200, zorder=3, label='Схема 3-го порядка аппроксимации')
	    plt.legend()
	elif type == 'full': 
	    plt.plot(x, y_3, 'orchid', linewidth=3)
	    plt.scatter(x_s, y_s, color='crimson', s=200, zorder=3)
	    plt.scatter(x_l, y_l, color='cyan', s=200, zorder=3, 
	                label='Наиболее точная схема с минимальной аппроксимационной вязкостью на множестве Фридрихса')
	    plt.scatter(x_3rd, y_3rd, color='brown', s=200, zorder=3, label='Схема 3-го порядка аппроксимации')
	    plt.scatter(x_fr_2nd, y_fr_2nd, color='black', s=200, zorder=3, label='Самая близкая к Фридрихсу схема 2го порядка')
	    plt.legend()
	    
	plt.fill_between(x, y_1, where=((x <= 1 / 3)), color='beige')
	plt.fill_between(x, y_2, where=((y_2 >= 0) & (y_2 < 0.75)), color='beige')

	plt.xlim([0, 1])
	plt.ylim([-0.05, 1.2])

	plt.show()
