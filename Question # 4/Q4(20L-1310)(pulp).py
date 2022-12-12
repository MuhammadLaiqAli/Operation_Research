# QUESTION 4 PULP SOLVER
#  
# X1 = amount invested in EAL stock
# 
# X2 = amount invested in BRU stock
# 
# X3 = amount invested in TAT stock
# 
# X4 = amount invested in long term bonds
# 
# X5 = amount invested in short term bonds
# 
# X6 = amount invested in the tax deferred annuity
# 
# X7 = the total amount invested in stocks only
# 
# MAXIMUM  .15X1 + .12 X2 + .09X3 + .11X4 + .085X5 + .06X6
# 
# S.T.
# 
# X1 + X2 + X3 + X4 + X5 + X6 = 50,000 (Total)
# 
# X6 >= 10,000 (TDA)
# 
# X1 + X2 + X3 - X7 = 0 (Stocks)
# 
# X3 -.25X7 >= 0 (Min TAT)
# 
# X4 + X5 - X7 >= 0(Bond  stock)
# 
# X3 + X5 + X6 <= 12,500 (Low %)
# 
# All X's >= 0
# 

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
x5 = LpVariable("x5",0)
x6 = LpVariable("x6",0)
x7 = LpVariable("x7",0)

# Defining the objective Function
prob += 0.15*x1 + 0.12*x2 + 0.09*x3 + 0.11*x4 + 0.085*x5 + 0.06*x6

# Defining the constraints
prob += 1*x1 + 1*x2 + 1*x3 + 1*x4 + 1*x5 + 1*x6 == 50000, "1st constraint"
prob += 1*x6 >= 10000, "2nd constraint"
prob += 1*x1 + 1*x2 + 1*x3 - 1*x7 == 0, "3rd constraint"
prob += 1*x3 - 0.25*x7 >= 0, "4th constraint"
prob += 1*x4 + 1*x5 - 1*x7 >= 0, "5th constraint"
prob += 1*x3 + 1*x5 + 1*x6 <= 12500, "6th constraint"

# solve the linear programming problem
prob.solve()

# print the result
print("Status: ",LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=" , v.varValue)
    
print("The optimal value of the objective function is = ", value(prob.objective))
