import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


X = 2

n_x = 201
h = 0.01

n_t = 101
tau = 0.5 * h

xs = np.linspace(0, X, n_x)
step = 100


def a_2(b, c):
	return 3 / 5 - 1 / 5 * b - 4 / 5 * c


def d_2(b, c):
	return 2 / 5 - 4 / 5 * b - 1 / 5 * c


def u_init(x):
    if 0.4 <= x <= 0.6:
        return 1
    return 0


def solve(scheme):
    arr = scheme[1]
    u = np.zeros((n_t, n_x))
    
    for i in range(n_x):
        u[0][i] = u_init(xs[i])
        u[1][i] = u_init(xs[i] - tau)

    for j in range(1, n_t - 1):
        for i in range(1, n_x - 1):
            u[j + 1][i] = arr[0] * u[j - 1][i - 2] + arr[1] * u[j - 1][i] + \
                          arr[2] * u[j][i - 1] + arr[3] * u[j][i + 1]
    
    _plot(scheme[0], u[step])


def solve_hybrid(scheme):
    arr1 = scheme[1][0]
    arr2 = scheme[1][1]
    arr3 = scheme[1][2]

    u = np.zeros((n_t, n_x))
    for i in range(n_x):
        u[0][i] = u_init(xs[i])
        u[1][i] = u_init(xs[i] - tau)

    for j in range(1, n_t - 1):
        for i in range(1, n_x - 1):
            u[j + 1][i] = arr1[0] * u[j - 1][i - 2] + arr1[1] * u[j - 1][i] + arr1[2] * u[j][i - 1] + arr1[3] * u[j][i + 1]

            if not min(u[j][i - 1], u[j - 1][i]) <= u[j + 1][i] <= max(u[j][i - 1], u[j - 1][i]):
                u[j + 1][i] = arr2[0] * u[j - 1][i - 2] + arr2[1] * u[j - 1][i] + arr2[2] * u[j][i - 1] + arr2[3] * u[j][i + 1]

                if not min(u[j][i - 1], u[j - 1][i]) <= u[j + 1][i] <= max(u[j][i - 1], u[j - 1][i]):
                    if arr3:
                        u[j + 1][i] = arr3[0] * u[j - 1][i - 2] + arr3[1] * u[j - 1][i] + arr3[2] * u[j][i - 1] + arr3[3] * u[j][i + 1]

                    if not min(u[j][i - 1], u[j - 1][i]) <= u[j + 1][i] <= max(u[j][i - 1], u[j - 1][i]):
                        if u[j + 1][i] >= max(np.array([u[j][i - 1], u[j - 1][i]])):
                            u[j + 1][i] = max(np.array([u[j][i - 1], u[j - 1][i]]))
                        else:
                            u[j + 1][i] = min(np.array([u[j][i - 1], u[j - 1][i]]))

    _plot(scheme[0], u[step])


def _plot(name, u):
    fig = plt.figure(figsize=(15, 12))
    fig.suptitle(name, fontsize=10)
    plt.plot(xs, [u_init(x - step * tau) for x in xs], label='analytic')
    plt.plot(xs, u, label=f'step={step}')
    plt.legend()
    plt.show()