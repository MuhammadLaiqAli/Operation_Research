# QUESTION 7 PULP SOLVER
# 
# X1 = Number of Student models produced each week
# 
# X2 = Number of Plus models produced each week
# 
# X3 = Number of Net models produced each week
# 
# X4 = Number of Pro models produced each week
# 
# MAXIMUM 70X1 + 80X2 + 130X3 + 150X4
# 
# S.T.
# 
# X3 >= 100 (Contract)
# 
# .4X1 + .5X2 + .6X3 + .8X4 <= 750 (Production Hours)
# 
# X1 + + X3 <= 700 (Celeron)
# 
# X2 + X4 <= 550 (Pentium)
# 
# X1 + X2 + X3 + <= 800 (20gb Hard Drives)
# 
# X4 <= 950 (30gb Hard Drives)
# 
# X1 + X2 + 2X3 + X4 <= 1600 (Floppy Drives)
# 
# X1 + X2 + X4 <= 1000 (Zip Drives)
# 
# X1 + X3 + X4 <= 1600 (CD R/W's)
# 
# X2 + X3 + X4 <= 900 (DVD's)
# 
# X1 + X2 <= 850 (15-in. monitors)
# 
# X3 + X4 <= 800 (17-in. monitors)
# 
# X2 + X3 <= 1250 (Mini-tower cases)
# 
# X1 + X4 <= 750 (Tower cases)
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

# Defining the objective Function
prob += 70*x1 + 80*x2 + 130*x3 + 150*x4

# Defining the constraints
prob += 1*x3 >= 100, "1st constraint"
prob += 0.4*x1 + 0.5*x2 + 0.6*x3 + 0.8*x4 <= 750, "2nd constraint"
prob += 1*x1 + 1*x3 <= 700, "3rd constraint"
prob += 1*x2 + 1*x4 <= 550, "4th constraint"
prob += 1*x1 + 1*x2 + 1*x3  <= 800, "5th constraint"
prob += 1*x4 <= 950, "6th constraint"
prob += 1*x1 + 1*x2 + 2*x3 + 1*x4 <= 1600, "7th constraint"
prob += 1*x1 + 1*x2 + 1*x4 <= 1000, "8th constraint"
prob += 1*x1 + 1*x3 + 1*x4 <= 1600, "9th constraint"
prob += 1*x2 + 1*x3 + 1*x4 <= 900, "10th constraint"
prob += 1*x1 + 1*x2 <= 850, "11th constraint"
prob += 1*x3 + 1*x4 <= 800, "12th constraint"
prob += 1*x2 + 1*x3 <= 1250, "13th constraint"
prob += 1*x1 + 1*x4 <= 750, "14th constraint"

# solve the linear programming problem
prob.solve()

# print the result
print("Status: ",LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=" , v.varValue)
 
print("The optimal value of the objective function is = ", value(prob.objective))
