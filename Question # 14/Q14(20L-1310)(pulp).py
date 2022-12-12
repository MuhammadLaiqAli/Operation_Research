#  QUESTION 14 PULP SOLVER
# 
# X1 = Motor home cabinets produced in regular time in July
# 
# X2 = Motor home cabinets produced in overtime in July
# 
# X3 = Motor home cabinets produced in regular time in August
# 
# X4 = Motor home cabinets produced in overtime in August
# 
# XJS1 = Motor home cabinets produced in regular time in September
# 
# XJS2 = Motor home cabinets produced in overtime in September
# 
# X7 = Mobile home cabinets produced in regular time in July
# 
# X8 = Mobile home cabinets produced in overtime in July
# 
# X9 = Mobile home cabinets produced in regular time in August
# 
# X10 = Mobile home cabinets produced in overtime in August
# 
# YJS1 = Mobile home cabinets produced in regular time in September
# 
# YJS2 = Mobile home cabinets produced in overtime in September
# 
# X13 = Motor home cabinets stored in July
# 
# X14 = Motor home cabinets stored in August
# 
# X15 = Motor home cabinets stored in September
# 
# X16 = Mobile home cabinets stored in July
# 
# X17 = Mobile home cabinets stored in August
# 
# X18 = Mobile home cabinets stored in September
# 
# MINIMUM: 188X1 + 209X2 + 194X3 + 218X4 + 200 X5 + 227X6 +280X7 + 315X8 + 290X9 + 330X10 + 300 X11 + 345X12 +
# 6X13 + 6SA + 6SS + 9TJ + 9TA + 9Ts
# 
# S.T
# 
# Storage Constraints
# 
# X13 = 25 + X1 + X2 - 250 (Motor Home - July)
# 
# X14 = X13 + X3 + X4 - 250 (Motor Home - August)
# 
# X15 = X14 + X5 + X6 - 150 (Motor Home - September)
# 
# X16 = 20 + X7 + X8 - 100 (Mobile Home - July)
# 
# X17 = X16 + X9 + X10 - 300 (Mobile Home - August)
# 
# X18 = X17 + X11 + X12 - 400 (Mobile Home - September)
# 
# Required For September:
# 
# X15 >= 10 (Motor Home)
# 
# X18 >= 25 (Mobile Home)
# 
# Maximum Storage in any Month
# 
# X13 + X16 <= 300 (July)
# 
# X14 + X17 <= 300 (August)
# 
# X15 + X18 <= 300 (September)
# 
# ##  __Production__
# 
# ___RegularTime___
# 
# 3X1 + 5X7 <= 2100 (July)
# 
# 3X3 + 5X9 <= 1500 (August)
# 
# 3X5 + 5X11 <= 1200 (September)
# 
# ___Overtime___
# 
# 3X2 + 5X8 <= 1050 (July)
# 
# 3X4 + 5X10 <= 750 (August)
# 
# 3X6 + 5X12 <= 600 (September)
# 
# ___Non-negativity___
# 
# All X's, Y's, S's, and T's >= 0


from pulp import*
import matplotlib.pyplot as plt
import numpy as np

# create an object of a model
prob = LpProblem("Simple_Lp_Problem", LpMinimize)

# Defining decision variables
XJR  = LpVariable("XJR ",0)
XJO = LpVariable("XJO",0)
XAR = LpVariable("XAR",0)
XAO = LpVariable("XAO",0)
XSR = LpVariable("XSR",0)
XSO = LpVariable("XSO",0)
YJR = LpVariable("YJR",0)
YJO = LpVariable("YJO",0)
YAR = LpVariable("YAR",0)
YAO = LpVariable("YAO",0)
YSR = LpVariable("YSR",0)
YSO = LpVariable("YSO",0)
SJ = LpVariable("SJ",0)
SA = LpVariable("SA",0)
SS = LpVariable("SS",0)
TJ = LpVariable("TJ",0)
TA = LpVariable("TA",0)
TS = LpVariable("TS",0)

# Defining the objective Function
prob += 188*XJR + 209*XJO + 194*XAR + 218*XAO + 200*XSR + 227*XSO + 280*YJR + 315*YJO + 290*YAR + 330*YAO + 300*YSR + 345*YSO + 6*SJ + 6*SA + 6*SS + 9*TJ + 9*TA + 9*TS

# Defining the constraints
prob += 1*SJ - 1*XJR - 1*XJO == -225, "Motor Home - July"
prob += 1*SA - 1*SJ - 1*XAR - 1*XAO == -250, "Motor Home - August"
prob += 1*SS - 1*SA - 1*XSR - 1*XSO == -150, "Motor Home - September"
prob += 1*TJ - 1*YJR - 1*YJO == -80 , "Mobile Home - July"
prob += 1*TA - 1*TJ - 1*YAR - 1*YAO == -300 , "Mobile Home - August"
prob += 1*TS - 1*TA - 1*YSR - 1*YSO == -400 , "Mobile Home - September"
prob += 1*SS >= 10, "Motor Home"
prob += 1*TS >= 25, "Mobile Home"
prob += 1*SJ + 1*TJ <= 300, "July- Maximum Storage"
prob += 1*SA + 1*TA <= 300 , "August- Maximum Storage"
prob += 1*SS + 1*TS <= 300 , "September- Maximum Storage"
prob += 3*XJR + 5*YJR <= 2100 , "July-RegularTime"
prob += 3*XAR + 5*YAR <= 1500 , "August-RegularTime"
prob += 3*XSR + 5*YSR <= 1200 , "September-RegularTime"
prob += 3*XJO + 5*YJO <= 1050 , "July-Overtime"
prob += 3*XAO + 5*YAO <= 750 , "August-Overtime"
prob += 3*XSO + 5*YSO <= 600 , "September-Overtime"

# solve the linear programming problem
prob.solve()

# print the result
print("Status: ",LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=" , v.varValue)
    
print("The optimal value of the objective function is = ", value(prob.objective))