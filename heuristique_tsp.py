villes = ["A", "B", "C", "D", "E"]

distances = {
    ("A", "B"): 10,
    ("A", "C"): 15,
    ("A", "D"): 20,
    ("A", "E"): 25,
    ("B", "C"): 35,
    ("B", "D"): 25,
    ("B", "E"): 17,
    ("C", "D"): 30,
    ("C", "E"): 28,
    ("D", "E"): 12,
}

def distance(a, b):
    if a == b:
        return 0
    return distances.get((a, b), distances.get((b, a)))

depart = "A"
tour = [depart]
ville_actuelle = depart
distance_totale = 0

while len(tour) < len(villes):
    non_visitees = [v for v in villes if v not in tour]

    prochaine_ville = min(
        non_visitees,
        key=lambda ville: distance(ville_actuelle, ville)
    )

    distance_totale += distance(ville_actuelle, prochaine_ville)
    tour.append(prochaine_ville)
    ville_actuelle = prochaine_ville

distance_totale += distance(ville_actuelle, depart)

print("Tour trouvé par heuristique greedy :")
print(" -> ".join(tour + [depart]))
print("Distance totale :", distance_totale)