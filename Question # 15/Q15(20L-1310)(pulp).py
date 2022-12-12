# QUESTION 15 PULP SOLVER
# 
# X1 = the number of acres of wheat planted
# 
# X2 = the number of acres of corn planted
# 
# X3 = the number of acres of oats planted
# 
# X4 = the number of acres of soybeans planted
# 
# __Profit coefficients__ are 210($3.20) - $50 = $622, 300($2.55) - $75 = $690,
# 
# 180($1.45) - $30 = $231, and 240($3.10) - $60 = $684 respectively.
# 
# __MAX__ 622X1 + 690X2 + 231X3 + 684X4
# 
# __S.T.__
# 
# 4X1 + 5X2 + 3X3 + 10X4 <= 1,800 (Labor hours)
# 
# 50X1 + 75X2 + 30X3 + 60X4 <= 25,000 (Expenses)
# 
# 2X1 + 6X2 + X3 + 4X4 <= 1,200 (Water)
# 
# 210X1 >= 30,000 (Min. Wheat)
# 
# 300X2 >= 30,000 (Min. Corn)
# 
# 180X3 <= 25,000 (Max Oats)
# 
# X1 + X2 + X3 + X4 <= 300 (Total acres)
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

# Defining the objective Function
prob += 622*x1 + 690*x2 + 231*x3 + 684*x4

# Defining the constraints
prob += 4*x1 + 5*x2 + 3*x3 + 10*x4 <= 1800, "1st constraint"
prob += 50*x1 + 75*x2 + 30*x3 + 60*x4 <= 25000, "2nd constraint"
prob += 2*x1 + 6*x2 + 1*x3 + 4*x4 <= 1200, "3rd constraint"
prob += 210*x1 >= 30000, "4th constraint"
prob += 300*x2 >= 30000 , "5th constraint"
prob += 180*x3 <= 25000, "6th constraint"
prob += 1*x1 + 1*x2 + 1*x3 + 1*x4 <= 300, "7th constraint"

# solve the linear programming problem
prob.solve()

# print the result
print("Status: ",LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=" , v.varValue)
    
print("The optimal value of the objective function is = ", value(prob.objective))