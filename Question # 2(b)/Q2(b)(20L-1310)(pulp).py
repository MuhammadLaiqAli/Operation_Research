# __Question – 3.2(b):__
# X1 = Number of stoves produced weekly
# X2 = Number of washers produced weekly
# X3 = Number of electric dryers produced weekly
# X4 = Number of gas dryers produced weekly
# X5 = Number of refrigerators produced weekly
# __MAX__ 110X1 + 90X2 + 75X3 + 80X4 + 130X5
# __S.T.__
# 5.5X1 + 5.2X2 + 5.0X3 + 5.1X4 + 7.5X5 <= 4800 (Molding/pressing)
# 4.5X1 <= 1200 (Stove assembly)
# 4.5X2 + 4.0X3 + 3.0X4 <= 2400 (Washer/dryer assembly)
# 9.0X5 <= 1200 (Refrigerator assembly)
# 4.0X1 + 3.0X2 + 2.5X3 + 2.0X4 + 4.0X5 <= 3000 (Packaging)
# X2 - X3 - X4 = 0 (Washers = Dryers)
# X3 - X4 <= 100 (E. Dryers <= G. Dryers + 100)
# -X3 + X4 <= 100 (G. Dryers <= E. Dryers + 100)
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

# Defining objective function
prob += 110*x1 + 90*x2 + 75*x3 + 80*x4 + 130*x5

# Defining Constraints
prob += 5.5*x1 + 5.2*x2 + 5.0*x3 + 5.1*x4 + 7.5*x5 <= 4800, "1st constraints"
prob += 4.5*x1 <= 1200, "2nd constraints"
prob += 4.5*x2 +4.0*x3 + 3.0*x4 <= 2400, "3rd constraints"
prob += 9.0*x5 <= 1200, "4th constraints"
prob += 4.0*x1 + 3.0*x2 + 2.5*x3 + 2.0*x4 + 4.0*x5 <= 3000, "5th constraints"
prob += 1*x2 - 1*x3 - 1*x4 == 0, "6th constraints"
prob += 1*x3 - 1*x4 <= 100, "7th constraints"
prob += -1*x3 + 1*x4 <= 100, "8th constraints"

prob.solve()

# print the result
print("Status: ",LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=" , v.varValue)

print("The optimal value of the objective function is = ", value(prob.objective))


