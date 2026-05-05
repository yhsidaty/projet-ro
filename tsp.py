import itertools

villes = ["A", "B", "C", "D", "E"]

distances = {
    ("A", "B"): 10, ("A", "C"): 15, ("A", "D"): 20, ("A", "E"): 25,
    ("B", "C"): 35, ("B", "D"): 25, ("B", "E"): 17,
    ("C", "D"): 30, ("C", "E"): 28,
    ("D", "E"): 12
}

def distance(a, b):
    if a == b:
        return 0
    return distances.get((a, b), distances.get((b, a)))

def distance_tour(tour):
    total = 0
    for i in range(len(tour) - 1):
        total += distance(tour[i], tour[i+1])
    total += distance(tour[-1], tour[0])
    return total

depart = "A"
autres_villes = [v for v in villes if v != depart]

meilleur_tour = None
meilleure_distance = float("inf")

for permutation in itertools.permutations(autres_villes):
    tour = [depart] + list(permutation)
    d = distance_tour(tour)

    if d < meilleure_distance:
        meilleure_distance = d
        meilleur_tour = tour

print("Meilleur tour :", " -> ".join(meilleur_tour + [depart]))
print("Distance minimale :", meilleure_distance)