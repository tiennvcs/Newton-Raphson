import argparse
import numpy as np
from numpy import linalg as LA
from functions import F
from derivatives import Jacobian

def getArguments():
	parser = argparse.ArgumentParser(description="Solve equation system using Newton - Raspson")
	parser.add_argument("-ER", help="Hệ số không khí cấp", default=0.2) # 0.25, 0.3, 0.35, 0.4
	parser.add_argument("-T2", help="Nhiệu độ vừng khử", default=750)   # 750, 800, 850, 900
	parser.add_argument(
			"-init_values",
			help="Nghiệm khởi tạo trước khi chạy thuật toán",
			default=np.array(np.random.rand(6)))

	parser.add_argument("-epxilon", help="The accuracy of method", default=1e-4)
	parser.add_argument("-N", help="Số lượng vòng lặp giới hạn", default=1000)
	args = parser.parse_args()
	return args

def solveLinearSystem(jacobi: np.ndarray, Fx: np.ndarray):
	y = LA.solve(jacobi, Fx)
	return y

def display(x: np.ndarray, y: np.ndarray, n: int):
	print(f"{n}th -- Solution: {x} -- The error: {LA.norm(y, ord=None)}")

def getExpectation(solution: np.ndarray):
	sum_solution = np.sum(solution)
	percent1 = (12*solution[0]/23.52)*100
	percent2 = (solution[1] / sum_solution ) * 100
	percent3 = (solution[2] / sum_solution) * 100
	percent4 = (solution[3] / sum_solution) * 100
	percent6 = (solution[5] / sum_solution) * 100
	return np.array([percent1, percent2, percent3, percent4, percent6])

def newton_raspson(x: np.ndarray, epxilon=1e-4, N=1000):
	"""
	@parameters:
		- x (np.array): the initial solution vector when run Newton - Raspson method.
		- epxilon (float): the accuracy determine when we stop the alogithms.
	@return values:
		- An array contains all root of equation system.
		- A number of iterators for each value.
	"""
	n = 1
	y = np.ones(6)
	while (n < N): # Use l2 norm
		# Calculate the F(x)
		Fx = F(x=x)
		# Calculate the Jacobian matrix
		jacobi = Jacobian(x=x)
		# Solve the n x n linear system J(x)y = F(x)
		y = solveLinearSystem(jacobi=jacobi, Fx=Fx)
		# Update solution
		x = x - y
		for i in range(6):
				if x[i] < 0:
					x[i] = np.random.rand()

		if LA.norm(y, ord=None) <= epxilon:
			return {'x':x, 'n': n, 'error': LA.norm(y, ord=None), 'success': 0}
		n = n + 1

	return {'x': x, 'n': n, 'error': LA.norm(y, ord=None), 'success': 1}


def main(args):
	ER = float(args.ER)
	T2 = float(args.T2)
	x = args.init_values
	epxilon = float(args.epxilon)
	N = int(args.N)

	result = newton_raspson(x=x, epxilon=epxilon, N=N)
	print(
            result['x'][0], result['x'][1], result['x'][2], result['x'][3], result['x'][4], result['x'][5],
            result['n'],
            result['error'],
            result['success'])


if __name__ == "__main__":
	args = getArguments()
	main(args)
