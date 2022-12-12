#  QUESTION 5 PULP SOLVER
# 
#  Unit Profit
#  
# 19-3(.50)-55(.20) = 6.50
# 
# 26-4(.50)-75(.20) = 9.00
# 
# 32-6(.50)-95(.20) = 10.00
#                                                           
# X1 = Number of full comforters produced daily              
# 
# X2 = Number of queen comforters produced daily             
# 
# X3 = Number of king comforters produced daily              
# 
# MAXIMUM 6.50X1 + 9.00X2 + 10.00X3
# 
# S.T.
# 
# 3X1 + 4X2 + 6X3 <= 2,700 (Stuffing)
# 
# 55X1 + 75X2 + 95X3 <= 48,000 (Fabric)
# 
# 3X1 + 5X2 + 6X3 <= 3,000 (Cutting minutes)
# 
# 5X1 + 6X2 + 8X3 <= 12,000 (Sewing minutes)
# 
# All X's >= 120
# 

from pulp import*
import matplotlib.pyplot as plt
import numpy as np

# create an object of a model
prob = LpProblem("Simple_Lp_Problem", LpMaximize)

# Defining decision variables
x1 = LpVariable("x1",120)
x2 = LpVariable("x2",120)
x3 = LpVariable("x3",120)

# Defining the objective Function
prob += 6.50*x1 + 9.00*x2 + 10.00*x3

# Defining the constraints
prob += 3*x1 + 4*x2 + 6*x3 <= 2700, "1st constraint"
prob += 55*x1 + 75*x2 + 95*x3 <= 48000, "2nd constraint"
prob += 3*x1 + 5*x2 + 6*x3 <= 3000, "3rd constraint"
prob += 5*x1 + 6*x2 + 8*x3 <= 12000, "4th constraint"

# solve the linear programming problem
prob.solve()

# print the result
print("Status: ",LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=" , v.varValue)

print("The optimal value of the objective function is = ", value(prob.objective))