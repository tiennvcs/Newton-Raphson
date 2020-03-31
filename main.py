import argparse
import numpy as np

def newton_raspson(init_values: list, epxilon=10e-10):
	"""
	@parameters:
		- init_values (list): the initial solution when run Newton - Raspson method.
		- epxilon (float): the accuracy determine when we stop the alogithms.
	@return values:
		- An array contains all root of equation system.
		- A number of iterators for each value.
	"""
	import parameters
	from functions import (f1, f2, f3, f4, f5, f6)
	from derivatives import (derivF_1, derivF_2, derivF_3, derivF_4, derivF_5, derivF_6)
	
	
	
	solution = np.array([])
	iterators = np.array([])



	return (solution, iterators)

def main(args):
	ER = float(args.ER)
	T2 = float(args.T2)
	init_values = args.init_values
	epxilon = float(args.epxilon)

	print(" ----------------------------------------------------------------------------------------------------")
	print(" |--------------------------------------------------------------------------------------------------|")
	print(" |                  Chương trình tìm nghiệp xấp xỉ bằng phương pháp Newton - Raspson                |")
	print(" ----------------------------------------------------------------------------------------------------")
	print(" |Các giá trị đầu vào:                                                                              |")
	print(f" | \tHệ số không khí cấp ER: {ER}")
	print(f" | \tNhiệt độ vùng khử  T2: {T2}")
	print(f" | \tGiá trị khởi tạo [n_1, n_2, n_3, n_4, n_5, n_6]: {init_values}")
	print(f" | \tĐộ chính xác cho trước epxilon: {epxilon}")
	print(" |--------------------------------------------------------------------------------------------------|")
	print(" ----------------------------------------------------------------------------------------------------")

        # Solve the problem with default values.
	solution, iterators = newton_raspson(init_values=init_values, epxilon=epxilon)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Solve equation system using Newton - Raspson")
	parser.add_argument("-ER", help="Hệ số không khí cấp", default=0.2) # 0.25, 0.3, 0.35, 0.4
	parser.add_argument("-T2", help="Nhiệu độ vừng khử", default=550)
	parser.add_argument("--init_values", help="Nghiệm khởi tạo trước khi chạy thuật toán", default=np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1]))
	parser.add_argument("--epxilon", help="The accuracy of method", default=10e-10)
	args = parser.parse_args()
	main(args)
