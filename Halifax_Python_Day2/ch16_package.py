from python_package import area, calculate

# Test area functions
print(area.square(4))
print(area.rect(3, 4))
print(area.circle(3))

# Test calculation functions
print(calculate.add(5, 3))
print(calculate.subtract(10, 5))
print(calculate.multiply(5, 4))
print(calculate.divide(20, 4))

from math import sqrt, pow
number = 16
square_root = sqrt(16)
power = pow(2,3)

print(f'the square root of {number} is {square_root}')
print(f'2 raised to power of 3 is {power}')
