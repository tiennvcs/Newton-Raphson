import os
import argparse
from equation import *
from fomular import *

def process():
	pass
	

def main(args):
	pass
	
	
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='The program solve the system equation using Newton-Raspson method.')
	parser.add_argument("-first argument", help="", default=0)
	parser.add_argument("-second argument", help="", default=1)
	args = parser.parse_args()
	main(args)
