import numpy
from itertools import combinations
points = numpy.array([2,2,3,2,5,6,1])
DIM = 7

original = [3.,-1.,0.,-2.,2.]

eewee = combinations(range(7),5)

mat = numpy.array([[      0,       0,       0,0,1],
                  [       1,       1,       1,1,1],
                  [(2**4)%7,(2**3)%7,(2**2)%7,2,1],
                  [(3**4)%7,(3**3)%7,(3**2)%7,3,1],
                  [(4**4)%7,(4**3)%7,(4**2)%7,4,1],
                  [(5**4)%7,(5**3)%7,(5**2)%7,5,1],
                  [(6**4)%7,(6**3)%7,(6**2)%7,6,1]])
print(mat)
possible = []

for check in eewee:
    test_mat = []
    test_pts = []
    for i in check:
        test_mat.append(mat[i])
        test_pts.append(points[i])
    something = numpy.linalg.solve(test_mat, test_pts)
    print(something, check)
