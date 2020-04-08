from main import newton_raspson
from matplotlib import pyplot as plt

def plotGraph(solutions: np.ndarray, iterators: np.ndarray, errors: np.ndarray, ERs: list, T2: float):
	"""
	@parameters:
		- solutions is a matrix that contain all solution vectors of system of equations.
		- ERs (list): list of values ER we provide for the problem.
		- T2 (float): the temparature we provide for the problem.
		- N (int): the number of iterators
	@return values:
		- None
	"""
	plt.style.use('seaborn')
	fig, ax = plt.subplots(figsize=(9,6))

	ax.plot(ERs, solutions[:, 0], color='b')
	ax.plot(ERs, solutions[:, 1], color='g')
	ax.plot(ERs, solutions[:, 2], color='r')
	ax.plot(ERs, solutions[:, 3], color='c')
	ax.plot(ERs, solutions[:, 4], color='m')
	ax.plot(ERs, solutions[:, 5], color='y')

	ax.set_xlabel('ER', fontsize=14)
	ax.set_ylabel('y', fontsize=14)
	ax.set_title('Oservation when ER change', fontsize=20)
	plt.xlim(0.19, np.max(ERs)+1e-4)
	plt.ylim(0, np.max(solutions)+1)
	plt.show()


def main(args):
    T2 = float(args.T2)
    N = int(args.N)
    x = args.init_values
    epxilon = args.epxilon

    solutions = np.array([[]])
    iterators = np.array([])
    errors = np.array([])
    ERs = np.arange(0.2, 0.41, 0.05)
    for ER in ERs:
	# Cập nhật các tham số
	
        solution, iterator, error = newton_raspson(x=x, epxilon=epxilon, N=N)
        solutions = np.append(solutions, solution)
        iterators = np.append(iterators, iterator)
        errors = np.append(errors, error)

    solutions = solutions.reshape(int(len(solutions)/6), 6)
    plotGraph(solutions=solutions, iterators=iterators, errors=errors, ERs=ERs, T2=T2)

if __name__ == "__main__":
    args = getArguments()
    main(args)
