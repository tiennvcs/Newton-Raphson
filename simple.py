import os
import argparse
import numpy as np

# Assumtion that f(x) = x^3 - 2x^2 - 3

def f(x: float):
    return x**3 - 2*x**2 - 3

def derivFunc(x: float):
    return 3*x**2 - 4*x


def newton_raphson(x=0, epxilon=10e-6):
    """
    @arguments:
        - x (float) is the initial value when run the newton-raspson method.
        - epxilon (float) is the differenc between actual solution and the approximate solution.
    @return values:
        - The value x:  approximate solution.
        - n (int) The number of iterators we actually need do to archive the accuracy.
    @note:
        - The fomular for the newton-raphson method is: 
                    x = x - f(x) / derivFunc(x) 
    """
    R = 1000
    L = -1000
    solution = np.array([])
    iterators = np.array([])
    while (R > L):
        n = 0
        h = f(x) / derivFunc(x)
        while abs(h) >= epxilon:
            fx = f(x)
            df =  derivFunc(x)
            if(df == 0):
                df += 10e-6
            x = x - fx/df
            n += 1
        
        L = L + x
        R = R - x

        differents = abs(solution - x)
        # If the value x is not in solution
        if all(differents > 0.01):
            solution = np.append(solution, x)
            iterators = np.append(iterators, n)
        else:
            x = (L + R) / 2
            print(f"The initial value x is {x}")
    return (solution, iterators)

def main(args):
    x = float(args.x_0)
    epxilon = float(args.epx)
    (solution, iterators) = newton_raphson(x=x, epxilon=epxilon)
    
    # display the result :)
    for i in range(len(solution)):
        print("\t\tThe {i}th root:")
        print(f"\t\t\tThe root of equation is ............. {solution[i]}")
        print(f"\t\t\tThe number of iterators is .......... {iterators[i]}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--x_0", help="The initial value", default=0.01)
    parser.add_argument("--epx", help="The accuracy", default=10e-10)
    args = parser.parse_args()
    main(args)

