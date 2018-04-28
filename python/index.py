import numpy
import class_name
from numpy import pi
import pandas


def go():
    # vectot = numpy.array([1,23,4.0])
    # matrix = numpy.array([[3,3,4],[2,34,4],[1,34,5]])
    # print vectot.shape
    # print matrix.shape
    # print vectot.dtype
    # print matrix[:,1]

    vectot = numpy.array([5, 10, 15, 20])
    print vectot.astype(float)

    print vectot.sum(axis=0)

    # print matrix == 3


def numpy_func():
    a = numpy.arange(15).reshape(3, 5)
    print a.shape
    print a.ndim
    print a.size
    print numpy.zeros((3, 5))
    print numpy.ones((3, 5), dtype=numpy.int32)
    print numpy.random.random((2, 3))

    print numpy.linspace(0, 2 * pi, 1)

    a = numpy.array([20, 30, 40])
    b = numpy.array(4)
    print a - b
    print b ** 2


def base_func():
    # a = numpy.array([[1, 1], [0, 1]])
    # b = numpy.array([[2, 0], [3, 4]])
    # print a
    # print a.dot(b)
    # print numpy.dot(a, b)
    # a = numpy.arange(3 * 2)
    # print a
    # print numpy.sqrt(a)

    a = numpy.floor(10 * numpy.random.random((2, 2)))
    b = numpy.floor(10 * numpy.random.random((2, 2)))

    print a
    print a.ravel()
    print a.T
    print '*' * 10
    print numpy.hstack((a, b))
    print numpy.vstack((a, b))
    print(numpy.hsplit(a, 2))


def repet_func():
    a = numpy.arange(12)
    b = a
    print (b is a)
    print id(a)
    print id(b)
    print a.view()


def sort_func():
    a = numpy.array([[4, 3, 5], [1, 2, 1]])
    print(a)
    print a.sort(axis=1)

    a = numpy.array([4, 3, 1, 2])
    j = numpy.argsort(a)
    print j
    print(a[j])


def pandss():

    pass


if __name__ == '__main__':
    pandss()
    # sort_func()
    # repet_func()
    # base_func()
    # numpy_func()
    # go()
