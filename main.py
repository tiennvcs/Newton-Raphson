import argparse
import random
import numpy as np
from numpy import linalg as LA
from parameters import *
import time
import os


def F(x: np.array):
    f1 = x[0] + x[2] + x[3] + x[5] - 1
    f2 = 2*x[1] + 2*x[4] + 4*x[5] - a - 2*(w+q)
    f3 = x[2] + 2*x[3] + x[4] - (b + w + q + 2*m)
    f4 = K1 * x[1]**2 - x[5]
    f5 = K2 * x[2]*x[4] - x[1]*x[3]
    f6 = dH_H2 * x[1] + dH_CO * x[2] + dH_CO2 * x[3] + dH_H2O_k * x[4] + dH_CH4 * x[5] + 3.76*m*dH_N2 - dH_trau - w*dH_H2O_l
    return np.array([f1, f2, f3, f4, f5, f6])


def Jacobian(x):
    df1 =  np.array([1, 0, 1, 1, 0, 1])
    df2 = np.array([0, 2, 0, 0, 2, 4])
    df3 = np.array([0, 0, 1, 2, 1, 0])
    df4 = np.array([0, 2*K1*x[1], 0, 0, 0, -1])
    df5 = np.array([0, -x[3], K2*x[4], -x[1], K2*x[2], 0])
    df6 = np.array([0, dH_H2, dH_CO, dH_CO2, dH_H2O_k, dH_CH4])
    return np.array([df1, df2, df3, df4, df5, df6])


def getArguments():
    parser = argparse.ArgumentParser(description="Solve equation system using Newton-Raphson")
    parser.add_argument("-ER", help="Hệ số không khí cấp", type=float, default=0.2) # 0.25, 0.3, 0.35, 0.4
    parser.add_argument("-T2", help="Nhiệu độ vừng khử", type=int, default=750)   # 750, 800, 850, 900
    parser.add_argument( "-init_values", help="The initial solution", default=np.array([random.uniform(1e6, 1e10)]*6))
    parser.add_argument("-epsilon", help="The accuracy of method", default=1e-10)
    parser.add_argument("-N", help="The number of iterations", default=1000)
    parser.add_argument("--output", default='output_solutions/', help="The output file store found solution")
    args = parser.parse_args()
    return args


def display(x: np.ndarray, y: np.ndarray, n: int):
	print(f"{n}th -- Solution: {x} -- The error: {LA.norm(y, ord=None)}")


def getExpectation(solution: np.ndarray):
    sum_solution = np.sum(solution)
    percent1 = (12*solution[0]/23.52)*100
    percent2 = (solution[1] / sum_solution) * 100
    percent3 = (solution[2] / sum_solution) * 100
    percent4 = (solution[3] / sum_solution) * 100
    percent5 = (solution[4] / sum_solution) * 100
    percent6 = (solution[5] / sum_solution) * 100
    return np.array([percent1, percent2, percent3, percent4, percent5, percent6])


def check_constraints(x: np.ndarray):
    nt = np.sum(x)
    # The 1st expectation
    if not (0.3936666 <= x[0] <= 0.7873333):
        return False
    if not(0.05*nt <= x[1] <= 0.06*nt):
        return False
    if not(0.17*nt <= x[2] <= 0.2*nt):
        return False
    if not(0.01*nt <= x[3] <= 0.03*nt):
        return False
    if not(0.04*nt <= x[5] <= 0.08*nt):
        return False
    return True


def random_solution(ER: float, T2:float, alpha:float, beta:float):
    n1 = np.random.rand()*alpha/ER/T2
    n2 = np.random.rand()
    n3 = np.random.rand()
    n4 = np.random.rand()*ER*beta
    n5 = np.random.rand()
    n6 = np.random.rand()
    return np.array([n1, n2, n3, n4, n5, n6])


def get_solution_random(ER: float, T2: float, output: str):
    alpha = 140
    beta = 2
    solution = random_solution(ER, T2, alpha=alpha, beta=beta)
    notFound = True
    n = 0
    count = 0
    solutions = []
    while count != 10:
        n += 1

        solution = random_solution(ER=ER, T2=T2, alpha=alpha, beta=beta)

        check_exptected = check_constraints(x=solution)
        if not check_exptected:
            continue

        count += 1
        print("{n} th iterators, got the solution: {x}".format(n=n, x=solution.tolist()))
        with open(output, 'a+') as f:
            f.write("{n} {x}\n".format(n=n, x=solution.tolist()))

        # Add the new found solution vector to result list.
        solutions.append(solution)

        #input("Next ? ...")

    return solutions


def newton_raphson(x: np.ndarray, epsilon=1e-6, N=1000):
	n = 1
	while (n < N):
		# Calculate the F(x)
		Fx = F(x=x)
		# Calculate the Jacobian matrix
		jacobi = Jacobian(x=x)
		# Solve the n x n linear system J(x)y = F(x)
		y = LA.solve(jacobi, Fx)
		# Update solution
		x = x - y

		if LA.norm(y, ord=np.inf) <= epsilon:
			return {'x':x, 'n': n, 'error': LA.norm(y, ord=np.inf), 'success': 1}

		n = n + 1

	return {'x': x.tolist(), 'n': n, 'error': LA.norm(y, ord=np.inf), 'success': 0}


def main(args):
    np.random.seed(42)
    np.set_printoptions(precision=4, linewidth=10)
    ER = float(args.ER)
    T2 = float(args.T2)
    #x = args.init_values
    #epsilon = float(args.epsilon)
    #N = int(args.N)

    #result = newton_raphson(x=x, epsilon=epsilon, N=N)
    #print(result)
    output_file = os.path.join(args.output, "{ER}-{T2}.txt".format(ER=ER, T2=T2))
    get_solution_random(ER=args.ER, T2=args.T2, output=output_file)

if __name__ == "__main__":
	args = getArguments()
	main(args)
