from pulp import LpProblem, LpMinimize, LpVariable, LpStatus, value

model = LpProblem("Transport_de_poisson", LpMinimize)

x1 = LpVariable("camion_normal", lowBound=0, cat="Integer")
x2 = LpVariable("camion_frigorifique", lowBound=0, cat="Integer")

cout_normal = 6000
cout_frigorifique = 9000

capacite_normal = 2
capacite_frigorifique = 3

demande = 18

model += cout_normal * x1 + cout_frigorifique * x2

model += capacite_normal * x1 + capacite_frigorifique * x2 >= demande

model += x1 <= 4
model += x2 <= 6

model.solve()

print("Transport de poissons Nouadhibou - Nouakchott")
print("Statut :", LpStatus[model.status])
print("Nombre de camions normaux :", x1.varValue)
print("Nombre de camions frigorifiques :", x2.varValue)
print("Coût total minimal :", value(model.objective), "MRU")