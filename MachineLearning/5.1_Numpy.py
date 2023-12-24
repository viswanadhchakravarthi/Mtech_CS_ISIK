# python objects:
# 1. high-level number objects: integers, floating point
# 2. containers: list( costless insertion and append), dictionaries( fast lookup )

# Numpy provides:
# 1. extension package to python for multi-dimension arrays
# 2. closer to hardware(efficiency)
# 3. designed for scientific computation (convenience)
# 4. also known as array oriented computing

from timeit import timeit
import numpy as np

a = np.array([0, 1, 2, 3]) # we have passed list as a parameter
print(a)
print(np.arange(10))

# Why numpy is useful ?
# Memory-efficient container that provides fast numerical operations
print(timeit("[i**2 for i in range(1000)]"))
a = np.arange(1000)
print(a**2) # this takes so less time

# 1-D
a = np.array([0, 1, 2, 3])
print(a)
# print dimensions
print(a.ndim)
# shape
print(a.shape)
print(len(a))

# 2-D, 3-D,...
b = np.array([[0, 1, 2], [3, 4, 5]])
print(b)
print(b.ndim)
print(b.shape)
print(len(b)) # len() returns the size of the first dimension

c = np.array([[[0, 1], [2, 3]], [[4, 5], [6, 7]]])
print(c)
print(c.ndim)
print(c.shape)

# 1-D array is called vector
# 2-D array is called matrix
# n-D array is called as Tensor in mathematics

# using np.arange()
a = np.arange(10)
print(a)
b = np.arange(1,10,2) # start, end(exclusive), step
print(b)

# using linspace()
a = np.linspace(0, 1, 6) #start, end, no of points
print(a)
# common arrays
a = np.ones((3, 3))
print(a)
b = np.zeros((3, 3))
print(b)

print(np.eye(3)) # identity matrix of dim - 3
print(np.eye(3, 2)) # identity matrix of dim - 3 rows & 2 cols

# create array using diag()
a = np.diag([1, 2, 3, 4]) # construct a diagnol array.
print(a)
print(np.diag(a)) # extract diagnol

# create array using random
# create an array of the given shape and populate it with random samples from uniform distribution
a = np.random.rand(4)
print(a)
a = np.random.randn(4) # returns a sample from "standard normal distribution"
print(a)

# basic DataTypes
a = np.arange(10)
print(a, a.dtype)
# you can explicitly specify which data-type you want:
a = np.arange(10, dtype='float64')
print(a, a.dtype)

# the default data type is float for zeros and ones function
a = np.zeros((3, 3))
print(a, a.dtype)

d = np.array([1+2j, 2+4j]) # complex datatype
print(d.dtype)
b = np.array([True, False, True, False]) # Boolean datatype
print(b.dtype)
s = np.array(['Ram', 'Robert', 'Rahim'])
print(s.dtype)

# each built-in datatype has a character code that uniquely identifies it
# b - Boolean
# i -(signed integers)
# u - unsigned integers
# f - floating point
# c - complex floating point
# m - timedelta
# M - dateTime
# O - (Python) objects
# S, a - (byte) string
# U - unicode
# v - raw data( void )
# https://docs.scipy.org/doc/numpy-1.10.1/user/basics.types.html

# indexing
a = np.arange(10)
print(a[5]) # indices begin at 0, like other python sequences( and c/c++)
# for multi-dimensional arrays, indexes are tuples of integers
a = np.diag([1, 2, 3])
print(a[2, 2])
a[2, 1] = 5
print(a)

# slicing
