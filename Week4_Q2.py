__author__ = 'Vineets'
import sys

from math import sqrt

def cosine(x,y):
	num = sum([i * j for (i, j) in zip(x, y)])
	xlen = sqrt(sum([i * i for i in x]))
	ylen = sqrt(sum([i * i for i in y]))
	res = num / (xlen * ylen)
	return res

matrix = [[1, 0, 1, 0, 1, 2], [1, 1, 0, 0, 1, 6], [0, 1, 0, 1, 0, 2]]

r = len(matrix)
c = len(matrix[0])

while True:
    alpha  = float(sys.stdin.readline().strip())
    for i in range(r):
        matrix[i][c-1] *= alpha
    for i in range(r):
        for j in range(i+1, r):
                print i, j, cosine(matrix[i], matrix[j])
    for i in range(r):
        matrix[i][c-1] /= alpha

"""
2
0 1 0.946094540761
0 2 0.865180912697
1 2 0.952579344416
1
0 1 0.847318545736
0 2 0.617213399848
1 2 0.849836585599
0.5
0 1 0.721687836487
0 2 0.288675134595
1 2 0.666666666667
0
Traceback (most recent call last):
0 1 0.666666666667
  File "/Users/Vineets/PycharmProjects/Coursera_MMDS/Week4_Q2.py", line 26, in <module>
0 2 0.0
    matrix[i][c-1] /= alpha
1 2 0.408248290464
ZeroDivisionError: float division by zero

Process finished with exit code 1     """