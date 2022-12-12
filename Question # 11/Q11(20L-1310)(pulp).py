# QUESTION 11 PULP SOLVER
# 
# X1 = Number of refrigerator/ovens produced
# 
# X2 = Number of French fry makers produced
# 
# X3 = Number of French toast makers produced
# 
# MINIMUM: 140X1 + 50X2 + 36X3
# 
# S.T.
# 
# 100X1 + 35X2 + 27X3 >= 2,000,000 (Min Profit)
# 
# X1 >= 5,000 (Min Refrig/oven)
# 
# X2 >= 4,000 (Min French fry maker)
# 
# X3 >= 2,300 (Min French toast maker)
# 
# X1 <= 15,000 (Max Refrig/oven)
# 
# X2 <= 15,000 (Max French fry maker)
# 
# X3 <= 15,000 (Max French toast maker)

from pulp import*
import matplotlib.pyplot as plt
import numpy as np

# create an object of a model
prob = LpProblem("Simple_Lp_Problem", LpMinimize)

# Defining decision variables
x1 = LpVariable("x1",0)
x2 = LpVariable("x2",0)
x3 = LpVariable("x3",0)

# Defining the objective Function
prob += 140*x1 + 50*x2 + 36*x3

# Defining the constraints
prob += 100*x1 + 35*x2 + 27*x3 >= 2000000 , "1st constraint"
prob += 1*x1 >= 5000, "2nd constraint"
prob += 1*x2 >= 4000, "3rd constraint"
prob += 1*x3 >= 2300, "4th constraint"
prob += 1*x1 <= 15000, "5th constraint"
prob += 1*x2 <= 15000 , "6th constraint"
prob += 1*x3 <= 15000 , "7th constraint"

# solve the linear programming problem
prob.solve()

# print the result
print("Status: ",LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=" , v.varValue)
 
print("The optimal value of the objective function is = ", value(prob.objective))