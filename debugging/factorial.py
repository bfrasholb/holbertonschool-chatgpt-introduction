#!/usr/bin/env python3.8
import sys

def factorial(n):
	if n < 0:
		raise ValueError("Factorial of Negative Numbers is Undefined")
	result = 1
	while n > 1:
		result *= n
		n -= 1
	return result

f = factorial(int(sys.argv[1]))
print(f)
