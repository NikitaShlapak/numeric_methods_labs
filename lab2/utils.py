import numpy as np


class System:
    a = -1
    b = 1
    var = 1

    def f(self, x):
        a = 1 + self.var / 2
        return -12 * a * x ** 2 - 4 * a * x ** 3

    def get_accurate_solution(self):
        a = 1 + self.var / 2
        sol = []
        for x in self.x_arr:
            sol.append(a * (1 - x ** 4))

        return np.array(sol)

    def solve_numerically(self):

        p = np.zeros(len(self.x_arr) - 1)
        q = np.ones(len(self.x_arr) - 1)
        p[0] = -1 * self.matrix[0, 1] / self.matrix[0, 0]
        q[0] = self.vector[0] / self.matrix[0, 0]

        for i in range(1, len(self.vector) - 1):
            p[i] = -self.matrix[i, i + 1] / (self.matrix[i, i - 1] * p[i - 1] + self.matrix[i, i])
            q[i] = (self.vector[i] - self.matrix[i, i - 1] * q[i - 1]) / (
                    self.matrix[i, i - 1] * p[i - 1] + self.matrix[i, i])

        self.res_vector = np.ones(len(self.vector))

        self.res_vector[-1] = (self.vector[-1] - self.matrix[-1, -2] * q[-1]) / (
                self.matrix[-1, -2] * p[-1] + self.matrix[-1, -1])

        for i in range(len(self.vector) - 1):
            self.res_vector[-i - 2] = self.res_vector[-i - 1] * p[-i - 1] + q[-i - 1]

        return np.array(self.res_vector)

    def __init__(self, var, y0=0, yn=0, step=0.4):
        print("Инициализация системы уравнений...")
        self.res_vector = None
        self.h = step
        self.var = var
        a = 1 + self.var / 2
        self.x_arr = np.arange(self.a, self.b + self.h, self.h)
        self.matrix = np.zeros((len(self.x_arr), len(self.x_arr)))
        self.vector = np.zeros(len(self.x_arr))

        for i in range(len(self.x_arr)):
            if i == 0:
                self.matrix[i, 0] = 1
                self.vector[i] = y0
            elif i == len(self.x_arr) - 1:
                self.matrix[i, -1] = 1
                self.vector[i] = yn
            else:
                self.matrix[i, i - 1] = 1 / (self.h ** 2) - 1 / (2 * self.h)
                self.matrix[i, i] = -2 / (self.h ** 2)
                self.matrix[i, i + 1] = 1 / (self.h ** 2) + 1 / (2 * self.h)
                self.vector[i] = self.f(self.x_arr[i])

        print(f"Столбец X: {self.x_arr}",
              f"Матрица системы:\n{self.matrix}",
              f"Столбец ответов: {self.vector}",
              f"Функция: f(x)={-12 * a}x^2 {-4 * a}x^3",
              f"Точное решение: y(x)={a}(1-x^4)",
              sep='\n\n')
        print("Инициализация системы уравнений окончена")
