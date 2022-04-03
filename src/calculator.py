from math import sin, cos, tan, log2, log


class Arithmetics:
    def __init__(self, expression):
        self._stack = []
        self._expression = expression
        self._operations = {
            '+': self._sum,
            '-': self._subtract,
            '*': self._multiply,
            '/': self._divide,
            '^': self._expo,
            'sin': self._sin,
            'cos': self._cos,
            'tg': self._tan,
            'ctg': self._cot,
            'log': self._log,
            'ln': self._ln,
            'u': self._UM
        }

    def _sum(self):
        self._stack[-2] = self._stack[-2] + self._stack[-1]
        del self._stack[-1]

    def _subtract(self):
        self._stack[-2] = self._stack[-2] - self._stack[-1]
        del self._stack[-1]

    def _multiply(self):
        self._stack[-2] = self._stack[-2] * self._stack[-1]
        del self._stack[-1]

    def _divide(self):
        self._stack[-2] = self._stack[-2] / self._stack[-1]
        del self._stack[-1]

    def _expo(self):
        self._stack[-2] = self._stack[-2] ** self._stack[-1]
        del self._stack[-1]

    def _sin(self):
        self._stack[-1] = sin(self._stack[-1])

    def _cos(self):
        self._stack[-1] = cos(self._stack[-1])

    def _tan(self):
        self._stack[-1] = tan(self._stack[-1])

    def _cot(self):
        self._stack[-1] = 1 / (tan(self._stack[-1]))

    def _log(self):
        self._stack[-1] = log2(self._stack[-1])

    def _ln(self):
        self._stack[-1] = log(self._stack[-1])

    def _UM(self):
        self._stack[-1] = -1 * self._stack[-1]

    def solve(self, x: float):
        for item in self._expression:
            if item == "x":
                item = x
            if isinstance(item, float) or isinstance(item, int):
                self._stack.append(item)
            else:
                self._operations[item]()

        return self._stack[-1]


def secant_method(f, x1, x2):
    iterations = 90
    for i in range(iterations):
        y1 = f(x1)
        y2 = f(x2)
        if y1 * y2 > 0:
            print("Невозможно определить корни уравнения")
            return None
        else:
            k = (y1 - y2) / (x1 - x2)
            b = y2 - k * x2
            new_x = -(b / k)
            new_y = f(new_x)
            if new_y * y1 > 0:
                x1 = new_x
            else:
                x2 = new_x
    return new_x


def integral(instance, a: float, b: float):
    N = int(100000 / 4)
    dx = (b - a) / N
    res = 0

    for i in range(N):
        try:
            res += (dx / 6) * (instance(a + i * dx) + 4 * instance((2 * a + (2 * i + 1) * dx) / 2) + instance(
                a + (i + 1) * dx))
        except TypeError:
            pass

    return res
