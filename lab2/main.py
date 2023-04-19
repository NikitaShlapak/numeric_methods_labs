import numpy as np
from utils import System


def create_and_solve(var):
    ar = System(var, step=5e-5)
    print(f'точное решение:\n{ar.get_accurate_solution()}',
          f'прогоночное решение:\n{ar.solve_numerically()}',
          f'Отличие:\n{ar.solve_numerically() - ar.get_accurate_solution()}, max:{max(abs(ar.solve_numerically() - ar.get_accurate_solution()))}',
          sep='\n\n')


if __name__ == '__main__':
    create_and_solve(1)
