# QUESTION 12(b) PULP SOLVER
# 
# X1 = Number of plates made per day
# 
# X2 = Number of mugs made per day
# 
# X3 = Number of steins made per day
# 
# X4 = Total daily production
# 
# MAXIMUM: 2.50X1 + 3.25X2 + 3.90X3
# 
# S.T.
# 
# 2X1 + 3X2 + 6X3 <= 1920 ((4)(8)(60) Molding min.)
# 
# 8X1 + 12X2 + 14X3 <= 3840 ((8)(8)(60) Finishing min.)
# 
# X2 >= 150 (Minimum mugs)
# 
# -2X1 - 2X2 + X3 <= 0 (Steins <= 2(Plates + Mugs)
# 
# X1 + X2 + X3 - X4 = 0 (Total Definition)
# 
# X1 - .3X4 <= 0 (Plates <= 30% Total Produced)
# 
# All X's >= 0
# 
# __b) Combine the first two constraints into one:__
# 
# 10X1 + 15X2 + 20X3 <= 5760


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
prob += 2.50*x1 + 3.25*x2 + 3.90*x3

# Defining the constraints
prob += 10*x1 + 15*x2 + 20*x3 <= 5760, "1st constraint"
prob += 1*x2 >= 150, "2nd constraint"
prob += -2*x1 - 2*x2 + 1*x3 <= 0 , "3rd constraint"
prob += 1*x1 + 1*x2 + 1*x3 - 1*x4 == 0 , "4th constraint"
prob += 1*x1 - 0.3*x4 <= 0, "5th constraint"

# solve the linear programming problem
prob.solve()

# print the result
print("Status: ",LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=" , v.varValue)
    
print("The optimal value of the objective function is = ", value(prob.objective))