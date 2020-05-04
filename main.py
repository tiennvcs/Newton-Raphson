import argparse
import random
import numpy as np
from numpy import linalg as LA
from parameters import *

def F(x: np.array):
    f1 = 4*x[1]**2 + 16*K1*x[2]**2 + 16*x[1]*x[2] - 4*A*x[1] - (8*A+4/K1)*x[2] + A**2
    f2 = (A+4*K2)*x[0] - 2*x[0]*x[1] - 4*x[0]*x[2] + 2*K2*x[1] - 2*K2*B
    f3 = (2*dH_CO-dH_CO2)*x[0] + (dH_H2+dH_CO-dH_H2O_k)*x[1] + (dH_H2-dH_CH4)*x[2]+C
    return np.array([f1, f2, f3])

def Jacobian(x):
    df1 =  np.array([0, 8*x[1]+16*x[2]-4*A, 32*K1*x[2]+16*x[1]-(8*A+4/K1)])
    df2 = np.array([A+4*K2-2*x[1]-4*x[2], -2*x[0]+2*K2, -4*x[0]])
    df3 = np.array([2*dH_CO-dH_CO2, dH_H2+dH_CO-dH_H2O_k, dH_H2-dH_CH4])
    return np.array([df1, df2, df3])

def getArguments():
	parser = argparse.ArgumentParser(description="Solve equation system using Newton-Raphson")
	parser.add_argument("-ER", help="Hệ số không khí cấp", default=0.2) # 0.25, 0.3, 0.35, 0.4
	parser.add_argument("-T2", help="Nhiệu độ vừng khử", default=750)   # 750, 800, 850, 900
	parser.add_argument(
			"-init_values",
			help="Nghiệm khởi tạo trước khi chạy thuật toán",
			default=np.array([random.uniform(1e6, 1e10)]*3))

	parser.add_argument("-epsilon", help="The accuracy of method", default=1e-4)
	parser.add_argument("-N", help="Số lượng vòng lặp giới hạn", default=1000)
	args = parser.parse_args()
	return args

def display(x: np.ndarray, y: np.ndarray, n: int):
	print(f"{n}th -- Solution: {x} -- The error: {LA.norm(y, ord=None)}")

def getResult(x):
	print(x)
	n2 = (A-2*x[1]-4*x[2])/2
	n3 = (B-2*x[0]-x[1])
	n1 = 1-n3-x[0]-x[2]
	n4 = x[0]
	n5 = x[1]
	n6 = x[2]
	return {'n1': n1, 'n2': n2, 'n3': n3, 'n4': n4, 'n5': n5, 'n6': n6}

def getExpectation(solution: np.ndarray):
	sum_solution = np.sum(solution)
	percent1 = (12*solution[0]/23.52)*100
	percent2 = (solution[1] / sum_solution ) * 100
	percent3 = (solution[2] / sum_solution) * 100
	percent4 = (solution[3] / sum_solution) * 100
	percent6 = (solution[5] / sum_solution) * 100
	return np.array([percent1, percent2, percent3, percent4, percent6])

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

		# Customize for the problem
		for i in range(3):
				if x[i] < 0:
					x[i] = np.random.rand()

		if LA.norm(y, ord=None) <= epsilon:
			return {'x':x.tolist(), 'n': n, 'error': LA.norm(y, ord=None), 'success': 1}
		n = n + 1

	return {'x': x.tolist(), 'n': n, 'error': LA.norm(y, ord=np.inf), 'success': 0}

def main(args):
	ER = float(args.ER)
	T2 = float(args.T2)
	x = args.init_values  # x = [n4, n5, n6]
	epsilon = float(args.epsilon)
	N = int(args.N)
	np.set_printoptions(precision=4, linewidth=10)
	result = newton_raphson(x=x, epsilon=epsilon, N=N)
	solution = getResult(x=result['x'])
	print(solution)

if __name__ == "__main__":
	args = getArguments()
	main(args)
