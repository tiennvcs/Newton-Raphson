import argparse
import numpy as np
<<<<<<< HEAD
from numpy import linalg as LA
from functions import (f1, f2, f3, f4, f5, f6)
from derivatives import (derivF_1, derivF_2, derivF_3, derivF_4, derivF_5, derivF_6)

def F(x: np.ndarray):
	F = np.array([])
	f1_x = f1(x[0], x[1], x[2], x[3], x[4], x[5])
	f2_x = f2(x[0], x[1], x[2], x[3], x[4], x[5])
	f3_x = f3(x[0], x[1], x[2], x[3], x[4], x[5])
	f4_x = f4(x[0], x[1], x[2], x[3], x[4], x[5])
	f5_x = f5(x[0], x[1], x[2], x[3], x[4], x[5])
	f6_x = f6(x[0], x[1], x[2], x[3], x[4], x[5])
	
	return np.array([f1_x, f2_x, f3_x, f4_x, f5_x, f6_x])
=======
>>>>>>> 96e54d561ea84a519fa689c4ed02121f1a07c71d

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
	print(f"Iterator {n}th -- Solution: {x} -- The accuracy: {LA.norm(y, ord=None)}")



def newton_raspson(x: np.ndarray, epxilon=10e-10, N=1000):
	"""
	@parameters:
		- x (np.array): the initial solution vector when run Newton - Raspson method.
		- epxilon (float): the accuracy determine when we stop the alogithms.
	@return values:
		- An array contains all root of equation system.
		- A number of iterators for each value.
	"""
	import parameters
<<<<<<< HEAD
	n = 1
	y = np.ones(6)
	while ((LA.norm(y, ord=None) > epxilon or n == 1) and n <= N): # Use l2 norm
		
		# Calculate the F(x)
		Fx = F(x=x)
	
		# Calculate the Jacobian matrix
		jacobi = Jacobian(x=x)
	
		# Solve the nxn linear system J(x)y = F(x)
		y = solveLinearSystem(jacobi=jacobi, Fx=Fx)
	
		# Update solution
		x = x - y	
		display(x, y, n)
=======
	from functions import (f1, f2, f3, f4, f5, f6)
	from derivatives import (derivF_1, derivF_2, derivF_3, derivF_4, derivF_5, derivF_6)
	
	
	solution = np.array([])
	iterators = np.array([])
>>>>>>> 96e54d561ea84a519fa689c4ed02121f1a07c71d

		n = n + 1

	return (x, n)


def main(args):
	ER = float(args.ER)
	T2 = float(args.T2)
	x = args.init_values
	epxilon = float(args.epxilon)
	N = int(args.N)

	np.set_printoptions(precision=4)

	print(" -----------------------------------------------------------------------------------------------------------------")
	print(" |---------------------------------------------------------------------------------------------------------------|")
	print(" |                           Chương trình tìm nghiệp xấp xỉ bằng phương pháp Newton - Raspson                    |")
	print(" -----------------------------------------------------------------------------------------------------------------")
	print(" |Các giá trị đầu vào:                                                                              |")
	print(f" | \tHệ số không khí cấp ER: {ER}")
	print(f" | \tNhiệt độ vùng khử  T2: {T2}")
	print(f" | \tGiá trị khởi tạo [n_1, n_2, n_3, n_4, n_5, n_6]: {x}")
	print(f" | \tĐộ chính xác cho trước epxilon: {epxilon}")
	print(" |---------------------------------------------------------------------------------------------------------------|")
	print(" -----------------------------------------------------------------------------------------------------------------")

        # Solve the problem with default values.
	solution, iterators = newton_raspson(x=x, epxilon=epxilon, N=N)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Solve equation system using Newton - Raspson")
	parser.add_argument("-ER", help="Hệ số không khí cấp", default=0.2) # 0.25, 0.3, 0.35, 0.4
	parser.add_argument("-T2", help="Nhiệu độ vừng khử", default=550)
<<<<<<< HEAD
	parser.add_argument(
			"-init_values", 
			help="Nghiệm khởi tạo trước khi chạy thuật toán",
			default=np.array(np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1])))

	parser.add_argument("-epxilon",
						help="The accuracy of method", default=1e-10)
	parser.add_argument("-N", help="Số lượng vòng lặp giới hạn", default=1000)
=======
	parser.add_argument("--init_values", help="Nghiệm khởi tạo trước khi chạy thuật toán", default=np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1]))
	parser.add_argument("--epxilon", help="The accuracy of method", default=10e-10)
>>>>>>> 96e54d561ea84a519fa689c4ed02121f1a07c71d
	args = parser.parse_args()
	main(args)
