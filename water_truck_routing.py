points = ["Depot", "P1", "P2", "P3", "P4", "P5", "P6"]

demandes = {
    "P1": 200,
    "P2": 150,
    "P3": 300,
    "P4": 100,
    "P5": 250,
    "P6": 180,
}

capacite_camion = 1000

distances = {
    ("Depot", "P1"): 5,
    ("Depot", "P2"): 8,
    ("Depot", "P3"): 6,
    ("Depot", "P4"): 10,
    ("Depot", "P5"): 7,
    ("Depot", "P6"): 9,
    ("P1", "P2"): 4,
    ("P1", "P3"): 3,
    ("P1", "P4"): 7,
    ("P1", "P5"): 5,
    ("P1", "P6"): 6,
    ("P2", "P3"): 6,
    ("P2", "P4"): 5,
    ("P2", "P5"): 4,
    ("P2", "P6"): 7,
    ("P3", "P4"): 8,
    ("P3", "P5"): 3,
    ("P3", "P6"): 5,
    ("P4", "P5"): 6,
    ("P4", "P6"): 4,
    ("P5", "P6"): 3,
}

def distance(a, b):
    if a == b:
        return 0
    return distances.get((a, b), distances.get((b, a)))

non_visites = list(demandes.keys())
route = ["Depot"]
charge = 0
distance_totale = 0
position = "Depot"

while non_visites:
    possibles = [
        p for p in non_visites
        if charge + demandes[p] <= capacite_camion
    ]

    if not possibles:
        distance_totale += distance(position, "Depot")
        route.append("Depot")
        position = "Depot"
        charge = 0
        continue

    prochain = min(possibles, key=lambda p: distance(position, p))

    distance_totale += distance(position, prochain)
    route.append(prochain)
    charge += demandes[prochain]
    position = prochain
    non_visites.remove(prochain)

distance_totale += distance(position, "Depot")
route.append("Depot")

print("Routage des camions d'eau")
print("Route proposée :", " -> ".join(route))
print("Distance totale :", distance_totale, "km")
print("Capacité camion :", capacite_camion, "L")