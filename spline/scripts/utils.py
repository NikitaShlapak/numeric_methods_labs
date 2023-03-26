import numpy as np


class TaskData:
    x = [1, 2, 3, 4]
    s1 = 18
    s4 = 0
    b = [1, 1, 1, 1]
    c_left = np.array([
        [1, 0, 0, 0],
        [x[1] - x[0], 2 * (x[2] - x[0]), x[2] - x[1], 0],
        [0, x[2] - x[1], 2 * (x[3] - x[1]), x[3] - x[2]],
        [0, 0, 0, 1],
    ])
    d = [1, 1, 1, 1]

    def __init__(self, m):
        self.solved = False
        self.m = m
        self.f = []
        for i in range(1, 5):
            self.f.append(-i ** 3 + 12 * i ** 2 + m * i)
        self.c_right = [self.s1 / 2, 1, 1, 0]

        self.c_right[1] = 3 * ((self.f[2] - self.f[1]) / (self.x[2] - self.x[1]) - (self.f[1] - self.f[0]) / (
                self.x[1] - self.x[0]))

        self.c_right[2] = 3 * ((self.f[3] - self.f[2]) / (self.x[3] - self.x[2]) - (self.f[2] - self.f[1]) / (
                self.x[2] - self.x[1]) - self.s4 / (6 * (self.x[3] - self.x[2])))

        self.c_right = np.array(self.c_right)

    def print_data(self):
        print(self.c_left, self.c_right)

    def solve(self):
        self.c = np.linalg.solve(self.c_left, self.c_right)

        for i in range(len(self.c) - 1):
            self.b[i] = (self.f[i + 1] - self.f[i]) / (self.x[i + 1] - self.x[i]) - 1 / 3 * (
                    self.x[i + 1] - self.x[i]) * (self.c[i] + 2 * self.c[i + 1]) - 1
            self.d[i] = (self.c[i + 1] - self.c[i]) / 3 / (self.x[i + 1] - self.x[i])

        self.d[-1] = (self.s4 - 2 * self.c[-1]) / 6 / (self.x[-1] - self.x[-2])

        self.b[-1] = ((self.f[-1] - self.f[-2]) - (2 / 3 * self.c[-1] + self.s4 / 6)) / (self.x[-1] - self.x[-2])

    def print_solved(self):
        if not self.solved:
            self.solve()

        print(f"a:{self.f}\nb:{self.b}\nc:{self.c}\nd:{self.d}\n")


class Spline:
    coefs = {'a': 1,
             'b': 1,
             'c': 1,
             'd': 1,
             }

    def __init__(self, x=0):
        self.x = x

    def setcoefs(self, **kwargs):
        # print(kwargs)
        for key in kwargs.keys():
            # print(key)
            # print(key in self.coefs)
            if key in self.coefs:
                self.coefs[key] = kwargs[key]

    def at_point(self, x):
        return self.coefs['a'] + self.coefs['b'] * (x - self.x) + self.coefs['c'] * (x - self.x) ** 2 + self.coefs[
            'd'] * (x - self.x) ** 3

    def to_standart(self):
        ans = ''

        a = self.coefs['d']
        b = self.coefs['c'] - 3 * self.coefs['d'] * self.x
        c = self.coefs['b'] - 2 * self.coefs['c'] * self.x + 3 * self.coefs['d'] * self.x ** 2
        d = self.coefs['a'] - self.coefs['b'] * self.x + self.coefs['c'] * self.x ** 2 - self.coefs['d'] * self.x ** 3
        i = 3

        for let in [a, b, c, d]:
            x = ''
            if let != 0:
                if let < 0:
                    ans = ans + '-'
                else:
                    ans = ans + '+'
                if i != 0:
                    if i ==1:
                        x = 'x'
                    else:
                        x = f'x^{i}'
                if abs(let) == 1:
                    ans = ans + x
                elif abs(a) != 0:
                    ans = ans + f"{abs(let)}{x}"
                i = i-1
        return ans

    def __str__(self):
        out = f'x={self.x}|'
        if self.coefs['a']:
            out = out + str(self.coefs['a'])

        if self.coefs['b'] != 1:
            if self.coefs['b'] > 0:
                out = out + f"+{self.coefs['b']}(x-{self.x})"
            elif self.coefs['b'] < 0:
                out = out + f"{self.coefs['b']}(x-{self.x})"
        else:
            out = out + f"+(x-{self.x})"

        if self.coefs['c'] != 1:
            if self.coefs['c'] > 0:
                out = out + f"+{self.coefs['c']}(x-{self.x})^2"
            elif self.coefs['c'] < 0:
                out = out + f"{self.coefs['c']}(x-{self.x})^2"
        else:
            out = out + f"+(x-{self.x})^2"

        if self.coefs['d'] != 1:
            if self.coefs['d'] > 0:
                out = out + f"+{self.coefs['d']}(x-{self.x})^3"
            elif self.coefs['d'] < 0:
                out = out + f"{self.coefs['d']}(x-{self.x})^3"
        else:
            out = out + f"+(x-{self.x})^3"

        return out
