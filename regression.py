import numpy as np
import argparse
from sklearn.preprocessing import PolynomialFeatures
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from get_values import get_values_n1, get_values_n2, get_values_n3, get_values_n4, get_values_n6
import pandas as pd
from statsmodels.formula.api import ols
import statsmodels.api as sm


n_i = {
    "n1":get_values_n1,
    "n2":get_values_n2,
    "n3":get_values_n3,
    "n4":get_values_n4,
    "n6":get_values_n6,
}

def getArguments():
    parser = argparse.ArgumentParser(description="Solve equation system using Newton-Raphson")
    parser.add_argument("-var", default="n1",
                        choices=['n1', 'n2', 'n3', 'n4', 'n6', 'lhv', 'n1 lhv', 'lhv n1'],
                        help="The function need find")
    parser.add_argument("--linear", '-li', type=int, default=1, help="Linear or non-linear regression algorithm")
    return parser.parse_args()


def get_LHV(file_path):
    with open(file_path, 'r') as f:
        f.readline()
        content = f.readlines()
    X = []
    y = []
    for line in content:
        T2, ER, LHV = line.rstrip().split()
        X.append(np.array([float(T2), float(ER)]))
        y.append(float(LHV))
    return np.array(X), np.array(y)


def get_data(name: str, path: str):
    get_values = n_i[name]
    X, y = get_values(path)
    X = np.array(X)
    y = np.array(y)
    return X, y


def linear_regression(X, y):
    # reg = LinearRegression()
    # reg.fit(X, y)
    # return reg.coef_, reg.intercept_, reg.score(X, y)
    data = pd.DataFrame({'x': X[:,0].flatten(), 'y': X[:, 1].flatten(), 'z': y.flatten()})
    model = ols("z ~ x + y", data).fit()
    print(model.summary())
    return (model._results.params[1:], model._results.params[0], model._results.rsquared)


def polynorminal_regression(X, y):
    poly = PolynomialFeatures(2)
    X = poly.fit_transform(X)
    model = sm.OLS(y, X)
    results = model.fit()
    print(results.summary())
    return (results.params[1:], results.params[0], results.rsquared)


def visualize2Equation(LHV, Cs, LHV_coefs, C_coefs):
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = np.linspace(700, 1000, 1000)
    Y = np.linspace(0.19, 0.41, 1000)
    X, Y = np.meshgrid(X, Y)
    
    Z_LHV = LHV_coefs['coef'][0]*1 + LHV_coefs['coef'][1]*X + LHV_coefs['coef'][2] * Y + LHV_coefs['coef'][3] * X**2 + LHV_coefs['coef'][4]*X*Y + LHV_coefs['coef'][5] *Y**2 + LHV_coefs['intercept']
    Z_C = Z = C_coefs['coef'][0]*X + C_coefs['coef'][1]*Y + C_coefs['intercept']

    # # Plot the surface.
    surf = ax.plot_surface(X, Y, Z_LHV/(np.max(Z_LHV)+1), cmap=cm.coolwarm, label='LHV',
                           linewidth=0, antialiased=False)
    # # Plot the surface.
    surf = ax.plot_surface(X, Y, Z_C/(np.max(Z_C)+1), cmap=cm.coolwarm, label='C',
                           linewidth=0, antialiased=False)

    # Customize the z axis.
    #ax.set_zlim(-1+int(np.min(np.min(Z_C), int(np.min(Z_LHV)))), int(np.max(np.max(Z_C)), int(np.max(Z_LHV)+1)))
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    ax.set_xlabel("T2")
    ax.set_ylabel("ER")
    surf._facecolors2d=surf._facecolors3d
    surf._edgecolors2d=surf._edgecolors3d

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    #ax.set_title(r'The ${}$ representation and The approximate function'.format(label))

    ax.legend()
    plt.show()


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
        Z = coef[0] * X + coef[1] * Y + coef[2] * X**2 + coef[3] * X * Y + coef[4] * Y**2 + intercept

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    # Customize the z axis.
    ax.set_zlim(-1+np.min(Z), np.max(Z)+1)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    ax.set_xlabel("T2")
    ax.set_ylabel("ER")
    fig.colorbar(surf, shrink=0.5, aspect=5)

    ax.set_title(r'The ${}$ representation and The approximate function'.format(label))
    plt.show()


def main(args):
    
    name = args.var
    path = "output_solutions"
    
    if name == 'n1' or name == 'n4':
        X, y = get_data(name=name, path=path)
        coef, intercept, score  = linear_regression(X, y)
        print(coef, intercept, score)
        visualize(X.T, y, coef, intercept, label=name, linear=True)
    elif name == 'n2' or name == 'n3' or name == 'n6':
        X, y = get_data(name=name, path=path)
        coef, intercept, score = polynorminal_regression(X, y)
        print(coef, intercept, score)
        visualize(X.T, y, coef, intercept, label=name, linear=False)
    elif name == 'lhv':
        X, y = get_LHV('./experimental_data/LowHitValues.txt')
        coef, intercept, score = polynorminal_regression(X, y)
        print(coef, intercept, score)
        visualize(X.T, y, coef, intercept, label=name.upper(), linear=False)
    elif name == 'n1 lhv' or name == 'lhv n1':
        X_LHV, y_LHV = get_LHV('./experimental_data/LowHitValues.txt')
        coef_LHV, intercept_LHV, score_LHV = polynorminal_regression(X_LHV, y_LHV)
        print("The coefficients of yLHV equation:", coef_LHV, intercept_LHV, score_LHV)
        X_C, y_C = get_data(name='n1', path=path)
        coef_C, intercept_C, score_C = linear_regression(X_C, y_C)
        print("The coefficients of yC equation:", coef_C, intercept_C, score_C)
        visualize2Equation({'X_LHV':X_LHV, 'y_LHV':y_LHV}, {'X_C':X_C, 'y_C':y_C}, 
                {'coef': coef_LHV, 'intercept':intercept_LHV, 'score':score_LHV}, 
                {'coef':coef_C, 'intercept':intercept_C, 'score':score_C})


if __name__ == '__main__':
    args = getArguments()
    main(args)
