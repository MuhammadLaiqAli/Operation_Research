# # QUESTION 1 (PULP SOLVER)
# X1 = Number of 20-inch girls bicycles produced this week
# X2 = Number of 20-inch boys bicycles produced this week
# X3 = Number of 26-inch girls bicycles produced this week
# X4 = Number of 26-inch boys bicycles produced this week
# __MAX__ 27X1 + 32X2 + 38X3 + 51X4
# __S.T.__
# X1 + X3 >= 200 (Min girls models)
# X2 + X4 >= 200 (Min boys models)
# 12X1 + 12X2 + 9X3 + 9X4 <= 4800 (Production minutes)
# 6X1 + 9X2 + 12X3 + 18X4 <= 4800 (Assembly minutes)
# 2X1 + 2X2 <= 500 (20-inch tires)
# 2X3 + 2X4 <= 800 (26-inch tires)
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
x4 = LpVariable("x4",0)

# Defining the objective Function
prob += 27*x1 +32*x2 +38*x3 +51*x4

# Defining the constraints
prob += 1*x1 + 1*x3 >= 200, "1st constraint"
prob += 1*x2 + 1*x4 >= 200, "2nd constraint"
prob += 12*x1 + 12*x2 + 9*x3 + 9*x4 <= 4800, "3rd constraint"
prob += 6*x1 + 9*x2 + 12*x3 + 18*x4 <= 4800, "4th constraint"
prob += 2*x1 + 2*x2 <= 500, "5th constraint"
prob += 2*x3 + 2*x4 <= 800, "6th constraint"

# solve the linear programming problem
prob.solve()

# print the result
print("Status: ",LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=" , v.varValue)
    
print("The optimal value of the objective function is = ", value(prob.objective))
