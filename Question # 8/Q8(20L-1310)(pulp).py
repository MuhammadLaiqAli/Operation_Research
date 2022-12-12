# QUESTION 8 PULP SOLVER
# 
# X1 = the number of Delta assemblies produced daily
# 
# X2 = the number of Omega assemblies produced daily
# 
# X3 = the number of Theta assemblies produced daily
# 
# MAXIMUM 800X1 + 900X2 + 600X3
# 
# S.T.
# 
# X1 + X2 + X3 <= 7 (X70686 chips)
# 
# 2X1 + X2 + X3 <= 8 (Production hours)
# 
# 80X1 + 160X2 + 80X3 <= 480 (Quality minutes)
# 
# All X's >= 0

from pulp import*
import matplotlib.pyplot as plt
import numpy as np


# create an object of a model
prob = LpProblem("Simple_Lp_Problem", LpMaximize)

# Defining decision variables
x1 = LpVariable("x1",0)
x2 = LpVariable("x2",0)
x3 = LpVariable("x3",0)

# Defining the objective Function
prob += 800*x1 + 900*x2 + 600*x3

# Defining the constraints
prob += 1*x1 + 1*x2 + 1*x3 <= 7, "1st constraint"
prob += 2*x1 + 1*x2 + 1*x3 <= 8, "2nd constraint"
prob += 80*x1 + 160*x2 + 80*x3 <= 480, "3rd constraint"

# solve the linear programming problem
prob.solve()

# print the result
print("Status: ",LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=" , v.varValue)

print("The optimal value of the objective function is = ", value(prob.objective))





