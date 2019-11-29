from sympy import Function, Derivative
from sympy.abc import x # x is the independent variable
f = Function("f")(x) # f is a function of x
# f_ will be the derivative of f with respect to x
f_ = Derivative(f, x)
print(f_)