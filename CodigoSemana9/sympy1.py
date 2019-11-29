import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import sympy
import pprint

t, k, T0, Ta = sympy.symbols("t, k, T_0, T_a")
T = sympy.Function("T")
print(T)

ode = T(t).diff(t) + k*(T(t) - Ta)
eq1=sympy.Eq(ode)
print(eq1 )

ode_sol = sympy.dsolve(ode)
print(ode_sol)

print(ode_sol.lhs)
print(ode_sol.rhs)

ics = {T(0): T0}
print(ics)
C_eq = sympy.Eq(ode_sol.lhs.subs(t, 0).subs(ics), ode_sol.rhs.subs(t, 0)) 
print(C_eq)

C_sol = sympy.solve(C_eq)
print(C_sol)

print(ode_sol.subs(C_sol[0]) )

