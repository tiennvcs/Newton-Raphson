import argparse
import numpy as np
import matplotlib.pyplot as plt
import sys
import time
from numpy import linalg as LA
from functions import (f1, f2, f3, f4, f5, f6)
from derivatives import (derivF_1, derivF_2, derivF_3, derivF_4, derivF_5, derivF_6)

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

def F(x: np.ndarray):
	F = np.array([])
	f1_x = f1(x[0], x[1], x[2], x[3], x[4], x[5])
	f2_x = f2(x[0], x[1], x[2], x[3], x[4], x[5])
	f3_x = f3(x[0], x[1], x[2], x[3], x[4], x[5])
	f4_x = f4(x[0], x[1], x[2], x[3], x[4], x[5])
	f5_x = f5(x[0], x[1], x[2], x[3], x[4], x[5])
	f6_x = f6(x[0], x[1], x[2], x[3], x[4], x[5])

	return np.array([f1_x, f2_x, f3_x, f4_x, f5_x, f6_x])

def Jacobian(x: np.ndarray):
	jacobian = np.array([
			derivF_1(x[0], x[1], x[2], x[3], x[4], x[5]),
			derivF_2(x[0], x[1], x[2], x[3], x[4], x[5]),
			derivF_3(x[0], x[1], x[2], x[3], x[4], x[5]),
			derivF_4(x[0], x[1], x[2], x[3], x[4], x[5]),
			derivF_5(x[0], x[1], x[2], x[3], x[4], x[5]),
			derivF_6(x[0], x[1], x[2], x[3], x[4], x[5])])
	return jacobian

def solveLinearSystem(jacobi: np.ndarray, Fx: np.ndarray):
	y = LA.solve(jacobi, Fx)
	return y

def display(x: np.ndarray, y: np.ndarray, n: int):
	print(f"{n}th -- Solution: {x} -- The error: {LA.norm(y, ord=None)}")

def displayExpectation(solution: np.ndarray):
	"""
	n_t = n_1 + n_2 + n_3 + n_4 + n_5 + n_6
	12n_1/23,52 = 20-40%
	n_2/n_t = 5-6%
	n_3/n_t = 17-20%
	n_4/n_t = 1-3%
	n_6/n_t = 4-8%
	"""
	sum_solution = np.sum(solution)
	percent1 = (12*solution[0]/23.52)*100
	percent2 = (solution[1] / sum_solution ) * 100
	percent3 = (solution[2] / sum_solution) * 100
	percent4 = (solution[3] / sum_solution) * 100
	percent6 = (solution[5] / sum_solution) * 100
	print(f" |\tThe percentages of solution vector:")
	print(f" | \t\t* 12n_1/23.52 = {round(percent1, 3)} %")
	print(f" | \t\t* n_2/n_t     = {round(percent2, 3)} %")
	print(f" | \t\t* n_3/n_t     = {round(percent3, 3)} %")
	print(f" | \t\t* n_4/n_t     = {round(percent4, 3)} %")
	print(f" | \t\t* n_6/n_t     = {round(percent6, 3)} %")


def newton_raspson(x: np.ndarray, epxilon=10e-4, N=1000):
	"""
	@parameters:
		- x (np.array): the initial solution vector when run Newton - Raspson method.
		- epxilon (float): the accuracy determine when we stop the alogithms.
	@return values:
		- An array contains all root of equation system.
		- A number of iterators for each value.
	"""
	n = 1
	positive_solution = np.random.rand(6)
	y = np.ones(6)
	while ((LA.norm(y, ord=None) > epxilon or n == 1)): # Use l2 norm
		# Calculate the F(x)
		Fx = F(x=x)
		# Calculate the Jacobian matrix
		jacobi = Jacobian(x=x)
		# Solve the n x n linear system J(x)y = F(x)
		y = solveLinearSystem(jacobi=jacobi, Fx=Fx)
		# Update solution
		x = x - y
		if (x > 0).all():
			positive_solution = x[:]
		else:
			for i in range(6):
				if x[i] < 0:
					x[i] = np.random.rand()
		
		display(positive_solution, y, n)
		n = n + 1

	return (positive_solution, n-1, LA.norm(y, ord=None))


def main(args):
	ER = float(args.ER)
	T2 = float(args.T2)
	x = args.init_values
	epxilon = float(args.epxilon)
	N = int(args.N)

	np.set_printoptions(precision=4)

	print(" -----------------------------------------------------------------------------------------------------------------")
	print(" |---------------------------------------------------------------------------------------------------------------|")
	print(" |                           Chương trình tìm nghiệm xấp xỉ bằng phương pháp Newton - Raspson                    |")
	print(" -----------------------------------------------------------------------------------------------------------------")
	print(" | Các giá trị đầu vào                                                                                           |")
	print(f" | \tHệ số không khí cấp ER: {ER}")
	print(f" | \tNhiệt độ vùng khử  T2: {T2}")
	print(f" | \tVector nghiệm khởi tạo  [n_1, n_2, n_3, n_4, n_5, n_6]: {x}")
	print(f" | \tĐộ chính xác cho trước epxilon: {epxilon}")
	print(f" | \tSố vòng lặp giới hạn N: {N}")
	print(" |---------------------------------------------------------------------------------------------------------------|")
	print(" -----------------------------------------------------------------------------------------------------------------")

	key = input(" | This information is true (Yes/No)?\n | Please enter your confirm ? ")
	if key.upper() == "YES" or key.upper() == "Y":
        	# Solve the problem with default values
		print(" ----------------------------------------------------------------------------------------------------------------|")
		print(" | The result archived from method showing bellow                                                                |")
		solution, iterators, error  = newton_raspson(x=x, epxilon=epxilon, N=N)
		print(f" | \tThe final solution is: {solution}")
		print(f" | \tThe number of iterators is {iterators}")
		print(f" | \tThe error of algorithms is {error}")
		displayExpectation(solution)
		print(" ----------------------------------------------------------------------------------------------------------------")
	elif key.upper() == "NO" or key.upper() == "N":
		print("Please run again to solve problem and check your parameters")
		exit(1)


if __name__ == "__main__":
	args = getArguments()
	main(args)
