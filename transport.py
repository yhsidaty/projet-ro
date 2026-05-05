from pulp import *

model = LpProblem("Transport", LpMinimize)

x11 = LpVariable('x11', lowBound=0)
x12 = LpVariable('x12', lowBound=0)
x13 = LpVariable('x13', lowBound=0)

x21 = LpVariable('x21', lowBound=0)
x22 = LpVariable('x22', lowBound=0)
x23 = LpVariable('x23', lowBound=0)

model += 2*x11 + 4*x12 + 5*x13 + 3*x21 + 1*x22 + 7*x23

model += x11 + x12 + x13 <= 100
model += x21 + x22 + x23 <= 150
model += x11 + x21 == 80
model += x12 + x22 == 120
model += x13 + x23 == 50

model.solve()

for v in model.variables():
    print(v.name, "=", v.varValue)

print("Cost =", value(model.objective))