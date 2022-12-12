# QUESTION 9 PULP SOLVER
# 
# X1 = the number in group I contacted by telephone
# 
# X2 = the number in group II contacted by telephone
# 
# X3 = the number in group III contacted by telephone
# 
# X4 = the number in group IV contacted by telephone
# 
# X5 = the number in group I contacted in person
# 
# X6 = the number in group II contacted in person
# 
# X7 = the number in group III contacted in person
# 
# X8 = the number in group IV contacted in person
# 
# MINIMUM :
# 
# 15X1 + 12X2 + 20X3 + 18X4 + 35X5 + 30X6 + 50X7 + 40X8
# 
# S.T.
# 
# X1 + X2 + X3 + X4 + X5 + X6 + X7 + X8 = 2000 (Total)
# 
# X1 + X2 + X5 + X6 >= 1000 (W&R)
# 
# X5 + X6 + X7 + X8 >= 500 (In person)
# 
# -.5X1 + .5X5 >= 0 (W&R,ip)
# 
# X2 + X4 + X6 + X8 <= 800(Small)
# 
# -0.25X2 - 0.25X4 + 0.75X6 + 0.75X8 <= 0 (Small,ip)
# 
# X1 + X5 >= 200 (Min I)
# 
# X2 + X6 >= 200 (Min II)
# 
# X3 + X7 >= 200 (Min III)
# 
# X4 + X8 >= 200 (Min IV)
# 
# X1 + X5 <= 1000 (Max I)
# 
# X2 + X6 <= 1000 (Max II)
# 
# X3 + X7 <= 1000 (Max III)
# 
# X4 + X8 <= 1000 (Max IV)
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
x6 = LpVariable("x6",0)
x7 = LpVariable("x7",0)
x8 = LpVariable("x8",0)

# Defining the objective Function
prob += 15*x1 + 12*x2 + 20*x3 + 18*x4 + 35*x5 + 30*x6 + 50*x7 + 40*x8

# Defining the constraints
prob += 1*x1 + 1*x2 + 1*x3 + 1*x4 + 1*x5 + 1*x6 + 1*x7 + 1*x8 == 2000, "1st constraint"
prob += 1*x1 + 1*x2 + 1*x5 + 1*x6 >= 1000, "2nd constraint"
prob += 1*x5 + 1*x6 + 1*x7 + 1*x8 >= 500, "3rd constraint"
prob += -0.5*x1 + 0.5*x5 >= 0, "4th constraint"
prob += 1*x2 + 1*x4 + 1*x6 + 1*x8 <= 800, "5th constraint"
prob += -0.25*x2 - 0.25*x4 + 0.75*x6 + 0.75*x8 <= 0, "6th constraint"
prob += 1*x1 + 1*x5 >= 200, "7th constraint"
prob += 1*x2 + 1*x6 >= 200 , "8th constraint"
prob += 1*x3 + 1*x7 >= 200 , "9th constraint"
prob += 1*x4 + 1*x8 >= 200 , "10th constraint"
prob += 1*x1 + 1*x5 <= 1000 , "11th constraint"
prob += 1*x2 + 1*x6 <= 1000, "12th constraint"
prob += 1*x3 + 1*x7 <= 1000, "13th constraint"
prob += 1*x4 + 1*x8 <= 1000 , "14th constraint"

# solve the linear programming problem
prob.solve()

# print the result
print("Status: ",LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=" , v.varValue)
   
print("The optimal value of the objective function is = ", value(prob.objective))




