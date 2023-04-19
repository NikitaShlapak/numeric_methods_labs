import numpy as np
from utils import System


def create_and_solve(var):
    ar = System(var)
    print('точное решение:', ar.get_accurate_solution(),
          'прогоночное решение:', ar.solve_numerically(),
          sep='\n')


if __name__ == '__main__':
    create_and_solve(3)
