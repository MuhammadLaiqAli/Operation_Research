# QUESTION 3 PULP SOLVER
# 
# X1 = the number of standard Z345’s produced weekly
# 
# X2 = the number of industrial Z345’s produced weekly
# 
# X3 = the number of standard W250’s produced weekly
# 
# X4 = the number of industrial W250’s produced weekly
# 
# X5 = the total number of products produced weekly
# 
# MAXIMUM: 400X1 + 560X2 + 560X3 + 700X4
# 
# S.T.
# 
# 25X1 + 46X2 + 16X3 + 34X4 <= 2500 (zinc)
# 
# 50X1 + 30X2 + 28X3 + 12X4 <= 2800 (iron)
# 
# X1 + X2 >= 20 (Min Z345’s)
# 
# X1 + X2 + X3 + X4 - X5 = 0 (X5 definition)
# 
# X2 + X4 - .50X5 >= 0 (Industrial min.)
# 
# X1 + X2 - .75X5 <= 0 (Max Z345’s)
# 
# X3 + X4 - .75X5 <= 0 (Max W250’s)
# 
# X1, X2, X3, X4, X5 >= 0
# 

# In[6]:


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
prob += 400*x1 + 560*x2+ 560*x3 + 700*x4

# Defining constraints
prob += 25*x1 + 46*x2 + 16*x3 + 34*x4 <= 2500, "1st constraint"
prob += 50*x1 + 30*x2 + 28*x3 + 12*x4 <= 2800, "2nd constraint"
prob += 1*x1 + 1*x2 >= 20, "3rd constraint"
prob += 1*x1 + 1*x2 + 1*x3 + 1*x4 - 1*x5 == 0, "4th constraint"
prob += 1*x2 + 1*x4 - 0.50*x5 >= 0, "5th constraint"
prob += 1*x1 + 1*x2 - 0.75*x5 <= 0, "6th constraint"
prob += 1*x3 + 1*x4 - 0.75*x5 <= 0, "7th constraint"

prob.solve()

# print the result
print("Status: ",LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=" , v.varValue)

print("The optimal value of the objective function is = ", value(prob.objective))


