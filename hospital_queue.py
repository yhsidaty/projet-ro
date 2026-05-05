import math

lam = 12
mu = 5
c = 3

rho = lam / (c * mu)

def p0(lam, mu, c):
    somme = 0

    for n in range(c):
        somme += (lam / mu) ** n / math.factorial(n)

    dernier = ((lam / mu) ** c) / (math.factorial(c) * (1 - rho))

    return 1 / (somme + dernier)

P0 = p0(lam, mu, c)

Lq = (
    P0
    * ((lam / mu) ** c)
    * rho
    / (math.factorial(c) * (1 - rho) ** 2)
)

Wq = Lq / lam
W = Wq + (1 / mu)

print("Modèle M/M/c - Centre hospitalier")
print("Taux d'arrivée λ =", lam, "patients/heure")
print("Taux de service μ =", mu, "patients/heure")
print("Nombre de serveurs c =", c)
print("Utilisation ρ =", round(rho, 3))
print("Nombre moyen en attente Lq =", round(Lq, 3))
print("Temps moyen d'attente Wq =", round(Wq * 60, 2), "minutes")
print("Temps moyen dans le système W =", round(W * 60, 2), "minutes")