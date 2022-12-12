# QUESTION 13 PULP SOLVER
# 
# X1 = $ invested in first trust deeds
# 
# X2 = $ invested in second trust deeds
# 
# X3 = $ invested in third trust deeds
# 
# X4 = $ invested in commercial trust deeds
# 
# X5 = $ invested in a savings account
# 
# X6 = Total $ invested in residential trust deeds
# 
# X7 = Total $ invested in all trust deeds
# 
# MAXIMUM .0775X1 +.1125X2 +.1425X3 +.9875X4 +.0445X5
# 
# S.T.
# 
# X1 + X2 + X3 + X4 + X5 = 68,000,000 (Total)
# 
# X5 >= 5,000,000 (Save)
# 
# X1 + X2 + X3 + - X6 = 0 (Res Tr.)
# 
# X1 + X2 + X3 + X4 -X7 = 0 (Total Tr)
# 
# X6 - .8X7 >= 0 (80 %Res.)
# 
# X1 -.6X6 >= 0 (60 %First)
# 
# 4X1 + 6X2 + 9X3 + 3X4 <= 340,000,000 (*)
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
x4 = LpVariable("x4",0)
x5 = LpVariable("x5",0)
x6 = LpVariable("x6",0)
x7 = LpVariable("x7",0)

# Defining the objective Function
prob += 0.0775*x1 + 0.1125*x2 + 0.1425*x3 + 0.9875*x4 + 0.0445*x5

# Defining the constraints
prob += 1*x1 + 1*x2 + 1*x3 + 1*x4 + 1*x5 == 68000000 , "1st constraint"
prob += 1*x5 >= 5000000, "2nd constraint"
prob += 1*x1 + 1*x2 + 1*x3 + -1*x6 == 0, "3rd constraint"
prob += 1*x1 + 1*x2 + 1*x3 + 1*x4 - 1*x7 == 0, "4th constraint"
prob += 1*x6 - 0.8*x7 >= 0 , "5th constraint"
prob += 1*x1 -0.6*x6 >= 0, "6th constraint"
prob += 4*x1 + 6*x2 + 9*x3 + 3*x4 <= 340000000 , "7th constraint"

# solve the linear programming problem
prob.solve()

# print the result
print("Status: ",LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=" , v.varValue)

print("The optimal value of the objective function is = ", value(prob.objective))