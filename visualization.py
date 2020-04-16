import argparse
import subprocess
import numpy as np
from main import newton_raspson
from matplotlib import pyplot as plt
from main import getExpectation
from datetime import datetime

def plotGraph(expectations: np.ndarray, iterators: np.ndarray, errors: np.ndarray, ERs: list, T2: float):
	"""
	@parameters:
		- solutions is a matrix that contain all solution vectors of system of equations.
		- ERs (list): list of values ER we provide for the problem.
		- T2 (float): the temparature we provide for the problem.
		- N (int): the number of iterators
	@return values:
		- None
	"""
	plt.style.use('seaborn-deep')
	fig, ax = plt.subplots(figsize=(9,6))

	ax.plot(ERs, expectations[:, 0], color='b', label='C')
	ax.plot(ERs, expectations[:, 1], color='g', label='H2')
	ax.plot(ERs, expectations[:, 2], color='r', label='CO')
	ax.plot(ERs, expectations[:, 3], color='c', label='CO2')
	ax.plot(ERs, expectations[:, 4], color='y', label='CH4')

	ax.set_xlabel('ER', fontsize=14)
	ax.set_ylabel('Syngas Compositions(%)', fontsize=14)
	ax.set_title('Effect when changing ER', fontsize=20)
	legend = ax.legend(shadow=True, fontsize='x-large')
	legend.get_frame().set_facecolor('C1')
	plt.xticks(ticks=ERs)
	plt.xlim(0.19, np.max(ERs)+1e-4)
	plt.ylim(0, np.max(expectations)+1)

	plt.show()

	while True:
		key = input("Do you want to save the figure (Yes/No)? ")
		if key.upper() == "YES" or key.upper() == 'Y':
			now = datetime.now()
			dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
			fig.savefig('output/' + dt_string + '.jpeg')
			exit(0)
		elif key.upper() == "NO" or key.upper() == "N":
			exit(0)

	while True:
		key = input("Do you want to save the figure (Yes/No)? ")
		if key.upper() == "YES" or key.upper() == 'Y':
			now = datetime.now()
			dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
			fig.savefig('output/' + dt_string + '.jpeg')
			exit(0)
		elif key.upper() == "NO" or key.upper() == "N":
			exit(0)


def main(args):
	T2 = args.T2
	ERs = [0.2, 0.25, 0.3, 0.35, 0.4]
	expectations = np.array([])
	iterators = np.array([])
	errors = np.array([])
	for ER in ERs:
		running = subprocess.run(['python', 'main.py', '-ER', '0.3', '-T2', '900'], stdout=subprocess.PIPE)
		output = running.stdout.decode('utf-8').split("\n")[1].split(" ")
		solution = np.array(output[0:6], np.float32)
		n = int(output[6])
		error = float(output[7])
		expectation = getExpectation(solution=solution)
		expectations = np.append(expectations, expectation)
		iterators = np.append(iterators, n)
		errors = np.append(errors, error)

	expectations = expectations.reshape(int(len(expectations)/5), 5)
	plotGraph(expectations=expectations, iterators=iterators, errors=errors, ERs=ERs, T2=T2)


if __name__ == "__main__":
	parser = argparse.ArgumentParser("Visualize result")
	parser.add_argument("-T2", help="The value T2", default=750)
	args = parser.parse_args()
	plot = main(args)
