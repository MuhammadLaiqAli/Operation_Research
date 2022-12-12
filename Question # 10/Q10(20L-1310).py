# QUESTION 10 PULP SOLVER
# 
# X1 = the number of ounces of Multigrain Cheerios in the mixture
# 
# X2 = the number of ounces of Grape Nuts in the mixture
# 
# X3 = the number of ounces of Product 19 in the mixture
# 
# X4 = the number of ounces of Frosted Bran in the mixture
# 
# X5 = the total number of ounces in the mixture
# 
# MINIMUM: 12X1 + 9X2 + 9X3 + 15X4
# 
# S.T.
# 
# 30X1 + 30X2 + 20X3 + 20X4 >= 50 (Vitamin A)
# 
# 25X1 + 2X2 + 100X3 + 25X4 >= 50 (Vitamin C)
# 
# 25X1 + 25X2 + 25X3 + 25X4 >= 50 (Vitamin D)
# 
# 25X1 + 25X2 + 100X3 + 25X4 >= 50 (Vitamin B6)
# 
# 45X1 + 45X2 + 100X3 + 25X4 >= 50 (Iron)
# 
# X1 + X2 + X3 + X4 - X5 = 0 (Total)
# 
# X1 - .1X5 >= 0 (>= 10% M/G Cheerios)
# 
# X2 - .1X5 >= 0 (>= 10% Grape Nuts)
# 
# X3 - .1X5 >= 0 (>= 10% Product 19)
# 
# X4 - .1X5 >= 0 (>= 10% Frosted Bran)
# 
# All X's >= 0

from pulp import*
import matplotlib.pyplot as plt
import numpy as np

# create an object of a model
prob = LpProblem("Simple_Lp_Problem", LpMinimize)

# Defining decision variables
x1 = LpVariable("x1",0)
x2 = LpVariable("x2",0)
x3 = LpVariable("x3",0)
x4 = LpVariable("x4",0)
x5 = LpVariable("x5",0)

# Defining the objective Function
prob += 12*x1 + 9*x2 + 9*x3 + 15*x4

# Defining the constraints
prob += 30*x1 + 30*x2 + 20*x3 + 20*x4 >= 50, "1st constraint"
prob += 25*x1 + 2*x2 + 100*x3 + 25*x4 >= 50, "2nd constraint"
prob += 25*x1 + 25*x2 + 25*x3 + 25*x4 >= 50, "3rd constraint"
prob += 25*x1 + 25*x2 + 100*x3 + 25*x4 >= 50 , "4th constraint"
prob += 45*x1 + 45*x2 + 100*x3 + 25*x4 >= 50, "5th constraint"
prob += 1*x1 + 1*x2 + 1*x3 + 1*x4 - 1*x5 == 0, "6th constraint"
prob += 1*x1 - 0.1*x5 >= 0, "7th constraint"
prob += 1*x2 - 0.1*x5 >= 0, "8th constraint"
prob += 1*x3 - 0.1*x5 >= 0, "9th constraint"
prob += 1*x4 - 0.1*x5 >= 0, "10th constraint"

# solve the linear programming problem
prob.solve()

# print the result
print("Status: ",LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=" , v.varValue)
    
print("The optimal value of the objective function is = ", value(prob.objective))