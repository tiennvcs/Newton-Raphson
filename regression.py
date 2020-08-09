import numpy as np
import argparse
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from get_values import get_values_n1, get_values_n2, get_values_n3, get_values_n4, get_values_n6
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


n_i = {
    "n1":get_values_n1,
    "n2":get_values_n2,
    "n3":get_values_n3,
    "n4":get_values_n4,
    "n6":get_values_n6,
}

def getArguments():
    parser = argparse.ArgumentParser(description="Solve equation system using Newton-Raphson")
    parser.add_argument("-n_i", default="n1",
                        choices=['n1', 'n2', 'n3', 'n4', 'n6'],
                        help="The function need find")
    parser.add_argument("--linear", '-li', type=int, default=1, help="Linear or non-linear regression algorithm")
    return parser.parse_args()

def get_data(name: str, path: str):
    T2_values = [750, 800, 850, 900]
    ER_values = [0.2, 0.25, 0.3, 0.35, 0.4]
    get_values = n_i[name]

    X = []
    y = []

    for T2 in T2_values:

        percents, values = get_values(path, T2)
        i = 0
        for ER in ER_values:
            X.append(np.array([T2, ER]))
            y.append(percents[i])
            i += 1

    X = np.array(X)
    y = np.array(y)

    return X, y

def linear_regression(X, y):
    reg = LinearRegression()
    reg.fit(X, y)
    return reg.coef_, reg.intercept_, reg.score(X, y)


def polynorminal_regression(X, y):
    poly = PolynomialFeatures(2)
    features = poly.fit_transform(X)
    reg = LinearRegression()
    reg.fit(features, y)
    return reg.coef_.tolist(), reg.intercept_, reg.score(features, y)


def visualize(X, y, coef, intercept, label=None, linear=True):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    y = np.reshape(y, (-1, 1))

    # Plot a basic wireframe.
    ax.scatter(X[0], X[1], np.array(y))

    X = np.linspace(700, 1000, 1000)
    Y = np.linspace(0.19, 0.41, 1000)
    X, Y = np.meshgrid(X, Y)
    if linear:
        Z = coef[0] * X + coef[1] * Y + intercept
    else:
        Z = coef[0] * 1 + coef[1] * X + coef[2] * Y + coef[3] * X**2 + coef[4] * X * Y + coef[5] * Y**2 + intercept

    # # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    # Customize the z axis.
    ax.set_zlim(-1+np.min(Z), np.max(Z)+1)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    ax.set_xlabel("T2")
    ax.set_ylabel("ER")

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    ax.set_title(r'The ${}$ representation and The approximate function'.format(label))

    #ax.legend(label)
    plt.show()


def main(args):
    name = args.n_i
    path = "output_solutions"
    X, y = get_data(name=name, path=path)
    if name == 'n1' or name == 'n4':
        coef, intercept, score = linear_regression(X, y)
        print(coef, intercept, score)
        visualize(X.T, y, coef, intercept, label=name, linear=True)
    else:
        coef, intercept, score = polynorminal_regression(X, y)
        print(coef, intercept, score)
        visualize(X.T, y, coef, intercept, label=name, linear=False)


if __name__ == '__main__':
    args = getArguments()
    main(args)
