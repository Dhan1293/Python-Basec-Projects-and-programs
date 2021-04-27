import math
import cmath

def quadratic():
  print("Enter values of a, b and c.\nForm of equation (ax² + bx + c = 0)")
  a = int(input("Enter a - "))
  b = int(input("Enter b - "))
  c = int(input("Enter c - "))

  d = (b**2) - (4*a*c)
  sol1 = (-b + cmath.sqrt(d))/(2*a)
  sol2 = (-b - cmath.sqrt(d))/(2*a)

  print("Solution 1 - {:.2f}\nSolution 2 - {:.2f}".format(sol1, sol2))


quadratic()
