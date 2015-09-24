import numpy as np

class DualNumber:
    def __init__(self, *args, **kwargs):
        self._data = np.zeros(2)

        if len(args) == 1 and isinstance(args[0], np.ndarray):
            if not args[0].shape == (2, ):
                raise ValueError("bad initialization value: array with bad dims: {}".format(args[0].shape))
            self._data += args[0]
        elif len(args) == 1:
            self._data[0] = args[0]
        elif len(args) == 2:
            self._data += args
        elif len(args) == 0:
            pass
        else:
            raise ValueError("bad initialization value: too many parameters")

    def __add__(self, other):
        if isinstance(other, DualNumber):
            return DualNumber(self._data + other._data)
        else:
            return DualNumber(self._data[0] + x, self._data[1])

    def __sub__(self, other):
        if isinstance(other, DualNumber):
            return DualNumber(self._data - other._data)
        else:
            return DualNumber(self._data[0] - other, self._data[1])

    def __neg__(self):
        return DualNumber(-self._data)

    def __mul__(self, other):
        if isinstance(other, DualNumber):
            return DualNumber(self._data[0] + x._data[0], self._data[0] * other._data[1] + self._data[1] * other._data[0])
        else:
            print self._data
            return DualNumber(self._data * other)

    def __repr__(self):
        return "({} + {}*e)".format(self._data[0], self._data[1])


def df(f, x_0):
    dual_diff = f( DualNumber(x_0, 1.) ) - f( DualNumber(x_0, 0.) )
    return dual_diff._data[1]

if __name__ == '__main__':
    x = DualNumber()
    print x
    y = DualNumber(1, 1)
    print (x + y) * 5
    print (x + y) * 5 + y * 0.5
    print x - y  - y


    f = lambda x: x*x

    for x_0 in [-2, 0, 2]:
        d = df(f, x_0)
        print 'with x_0 = {}, df/dx is equal to: {}, while it should be: {}'.format(x_0, d, 2 * x_0)

