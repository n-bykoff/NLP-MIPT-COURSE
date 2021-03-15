import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

X = 1

n_x = 201
h = 2 * X / (n_x - 1)

n_t = 101
tau = 0.5 * h

xs = np.linspace(-1, X, n_x)
step = 100

u_l = 1.0
u_r = 0.0
p_l = 5.0
p_r = 2.0
rho = 0.25
c = 2.0


def u_0(x):
    return u_l if x <= 0 else u_r


def p_0(x):
    return p_l if x <= 0 else p_r


def u_t(x, t):
    if x < -c * t:
        return u_l
    elif x > c * t:
        return u_r
    return (u_l + u_r) / 2 - (p_r - p_l) / (2 * rho * c)


def p_t(x, t):
    if x < -c * t:
        return p_l
    elif x > c * t:
        return p_r
    return - rho * c * (u_r - u_l) / 2 + (p_l + p_r) / 2


def solve(scheme):
    arr = scheme[1]
    Y = np.zeros((n_t, n_x))
    Z = np.zeros((n_t, n_x))

    for i in range(n_x):
        Y[0][i] = u_0(xs[i]) + p_0(xs[i]) / c / rho
        Y[1][i] = u_0(xs[i] - c * tau) + p_0(xs[i] - c * tau) / c / rho
        Z[0][i] = u_0(xs[i]) - p_0(xs[i]) / c / rho
        Z[1][i] = u_0(xs[i] + c * tau) - p_0(xs[i] + c * tau) / c / rho


    for i in range(n_t):
        Y[i][0] = u_t(xs[0], tau * i) + p_t(xs[0], tau * i) / c / rho
        Y[i][-1] = u_t(xs[-1], tau * i) + p_t(xs[-1], tau * i) / c / rho
        Z[i][0] = u_t(xs[0], tau * i) - p_t(xs[0], tau * i) / c / rho
        Z[i][-1] = u_t(xs[-1], tau * i) - p_t(xs[-1], tau * i) / c / rho


    for j in range(1, n_t - 1):

        for i in range(1, n_x - 1):
            Y[j + 1][i] = arr[0] * Y[j - 1][i - 2] + arr[1] * Y[j - 1][i] + \
                          arr[2] * Y[j][i - 1] + arr[3] * Y[j][i + 1]

        for i in range(0, n_x - 2):
            Z[j + 1][i] = arr[0] * Z[j - 1][i + 2] + arr[1] * Z[j - 1][i] + \
                          arr[2] * Z[j][i + 1] + arr[3] * Z[j][i - 1]

    _plot(scheme[0], Y[step], Z[step])


def _plot(name, u, v):
    mpl.style.use('seaborn')
    fig = plt.figure()
    fig.suptitle(name + " " + "U", fontsize=10)
    plt.plot(xs, [u_t(x, step * tau) for x in xs], label='analytic')
    plt.plot(xs, (u + v) / 2, label=f'step={step}')
    plt.legend()
    plt.show()