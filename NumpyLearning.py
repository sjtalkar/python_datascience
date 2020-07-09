import numpy as np
from bs4 import BeautifulSoup
import requests as req
import pandas as pd

URL = "https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table"
whatDidIGet = pd.read_html(URL)
print(len(whatDidIGet))


# response = req.get(URL)
# soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
# table = soup.find("table", {"class": "wikitable sortable"}).tbody

# print(table)


newArray = np.array([1, 2, 3, 4])
# print(newArray)
# print(newArray * 2)
# print(newArray)

twoDimensional = np.array([newArray, 2 * newArray, 3 * newArray])
# print(twoDimensional)
# print(twoDimensional[2, 2])

identityMatrix = np.eye(2, 2)
# print(identityMatrix.dtype)
identityMatrix = identityMatrix.astype("i")
# print(identityMatrix)

rangeArray = np.arange(0, 20, 4)
# print(rangeArray)

linspaceArray = np.linspace(0, 21, 4)
# print(linspaceArray)

# print(twoDimensional.shape)
# Use vstack to stack arrays in sequence vertically (row wise).
# print(np.vstack([twoDimensional, 2 * twoDimensional]))
# Use hstack to stack arrays in sequence horizontally (column wise).
# print(np.hstack([twoDimensional, 2 * twoDimensional]))
o = np.linspace(0, 4, 9)  # return 9 evenly spaced values from 0 to 4
# print(o)
# `resize` changes the shape and size of array in-place.

o.resize(3, 3)
# print(o)


# Operations
# Use +, -, *, / and ** to perform element wise addition, subtraction, multiplication, division and power.

x = np.array([1, 2, 3])
y = np.array([7, 8, 9])
# print(x + y)  # elementwise addition     [1 2 3] + [4 5 6] = [5  7  9]
# print(x - y)  # elementwise subtraction  [1 2 3] - [4 5 6] = [-3 -3 -3]
# print(x * y) # elementwise multiplication  [1 2 3] * [4 5 6] = [4  10  18]
# print(x / y) # elementwise divison         [1 2 3] / [4 5 6] = [0.25  0.4  0.5]
# print(x**2) # elementwise power  [1 2 3] ^2 =  [1 4 9]

# Dot Product:

# print(x.dot(y))  # dot product  1*7 + 2*8 + 3*9

z = np.array([y, y ** 2])
# print(len(z))  # number of rows of array

# Let's look at transposing arrays. Transposing permutes the dimensions of the array.

# z = np.array([y, y**2])
# print(z)

# The shape of array z is (2,3) before transposing.
# print(z.shape)

# Use .T to get the transpose.
transposeOfZ = z.T
# print(transposeOfZ)
# print(transposeOfZ.shape)

oneArray = np.array([7, 8, 9, 49, 64, 81])
newZ = transposeOfZ.reshape(2, 3)
# print(newZ)

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
# print(x + y)  # elementwise addition     [1 2 3] + [4 5 6] = [5  7  9]
# print(x - y)


x = np.array([1, 2, 3])
y = np.array([7, 8, 9])
# print(x + y)  # elementwise addition     [1 2 3] + [4 5 6] = [5  7  9]

# The number of rows has swapped with the number of columns.

# z.T.shape

# Use .dtype to see the data type of the elements in the array.

# z.dtype

# Use .astype to cast to a specific type.

# z = z.astype('f')
# z.dtype


# Math Functions
# Numpy has many built in math functions that can be performed on arrays.

# a = np.array([-4, -2, 1, 3, 5])
# a.sum()
# a.max()
# a.min()
# a.mean()
# a.std()

# argmax and argmin return the index of the maximum and minimum values in the array.

# a.argmax()
# a.argmin()


# Indexing / Slicing
# s = np.arange(13)**2
# s

# Use bracket notation to get the value at a specific index. Remember that indexing starts at 0.

# s[0], s[4], s[-1]

# Use : to indicate a range. array[start:stop]

# Leaving start or stop empty will default to the beginning/end of the array.

# s[1:5]

# Use negatives to count from the back.

# s[-4:]

# A second : can be used to indicate step-size. array[start:stop:stepsize]

# Here we are starting 5th element from the end, and counting backwards by 2 until the beginning of the array is reached.

# s[-5::-2]

# Let's look at a multidimensional array.

# r = np.arange(36)
# r.resize((6, 6))
# r

# Use bracket notation to slice: array[row, column]

# r[2, 2]

# And use : to select a range of rows or columns

# r[3, 3:6]

# Here we are selecting all the rows up to (and not including) row 2, and all the columns up to (and not including) the last column.

# r[:2, :-1]

# This is a slice of the last row, and only every other element.

# r[-1, ::2]

# We can also perform conditional indexing. Here we are selecting values from the array that are greater than 30. (Also see np.where)

# r[r > 30]

# Here we are assigning all values in the array that are greater than 30 to the value of 30.

# r[r > 30] = 30
# r


# Copying Data
# Be careful with copying and modifying arrays in NumPy!

# r2 is a slice of r

# r2 = r[:3,:3]
# r2

# Set this slice's values to zero ([:] selects the entire array)

# r2[:] = 0
# r2

# r has also been changed!

# r

# To avoid this, use r.copy to create a copy that will not affect the original array

# r_copy = r.copy()
# r_copy

# Now when r_copy is modified, r will not be changed.

# r_copy[:] = 10
# print(r_copy, '\n')
# print(r)


# Iterating Over Arrays
# Let's create a new 4 by 3 array of random numbers 0-9.

test = np.random.randint(0, 10, (4, 3))
print(test)

# Iterate by row:

# for row in test:
#     print(row)

# Iterate by index:

# for i in range(len(test)):
#     print(test[i])

# Iterate by row and index:

# for i, row in enumerate(test):
#     print('row', i, 'is', row)

# Use zip to iterate over multiple iterables.

# test2 = test**2
# test2
# for i, j in zip(test, test2):
#     print(i,'+',j,'=',i+j)


people = [
    "Dr. Christopher Brooks",
    "Dr. Kevyn Collins-Thompson",
    "Dr. VG Vinod Vydiswaran",
    "Dr. Daniel Romero",
]


def split_title_and_name(person):
    return person.split()[0] + " " + person.split()[-1]


# option 1
# for person in people:
#     print(
#         split_title_and_name(person)
#         == (lambda x: x.split()[0] + " " + x.split()[-1])(person)
#     )

# # option 2
# list(map(split_title_and_name, people)) == list(
#     map(lambda person: person.split()[0] + " " + person.split()[-1], people)
# )


# def times_tables():
#     lst = []
#     for i in range(10):
#         for j in range(10):
#             lst.append(i * j)
#     return lst


# # print([i * j for i in range(10) for j in range(10)])

# lowercase = "abcdefghijklmnopqrstuvwxyz"
# digits = "0123456789"

# answer = [
#     first + second + third + fourth
#     for first in lowercase
#     for second in lowercase
#     for third in digits
#     for fourth in digits
# ]
# # print(answer)

canChange = "myString"
# print(canChange.capitalize())
# print(canChange)

# print(["a", "b", "c"] + [1, 2, 3])

r = np.arange(36)
# print(r)
rNew = r.reshape(6, 6)
# print(rNew)
# print(rNew[2:4, 2:4])

# print(r.reshape(36)[::7])

