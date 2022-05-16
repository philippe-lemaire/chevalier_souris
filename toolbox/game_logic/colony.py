import random
from dataclasses import dataclass

colony_details = {
    1: (
        "Motifs élaborés tracés dans la fourrure",
        "Labyrinthe de tunnels défensifs, piégés",
        "Désastre, tous se préparent à partir",
    ),
    2: (
        "Sous l'emprise de plantes étranges",
        "Auberge confortable et bien équipée",
        "Mariage, les rues jonchées de fleurs",
    ),
    3: (
        "Refusent de traiter avec des étrangers",
        "Chapelle taillée dans un bois noir",
        "Préparation d’une grande fête",
    ),
    4: (
        "Avides de nouvelles du lointain",
        "Jardin aux champignons, pour méditer",
        "Une épidémie s'est répandue",
    ),
    5: (
        "Une fourrure soignée porte malheur",
        "Crâne de bœuf, investi par une guilde",
        "Entrepôt est envahi d'insectes",
    ),
    6: (
        "Portent des habits finement brodés",
        "Un fouillis de taudis très serrés",
        "Jour de marché, fermiers en nombre",
    ),
    7: (
        "Affinent des années un fromage fort",
        "Des maisons en bois suspendues",
        "Les souris se sautent à la gorge",
    ),
    8: (
        "Visages cachés par des capuches",
        "Portail orné, gardé par des statues",
        "Groupe se forme pour attaquer une bête",
    ),
    9: (
        "Appauvris par la dîme du seigneur chat",
        "Temple secret du culte chauve-souris",
        "Des enfants ont disparu",
    ),
    10: (
        "Coupent rituellement leur queue",
        "Perchoir de pigeonnier",
        "Un noble fait une demande frivole",
    ),
    11: (
        "Chassent de grandes bêtes",
        "Entrepôt, rempli de conserves",
        "Troupe de théâtre itinérante arrive",
    ),
    12: (
        "Parents d’une même matriarche",
        "Dock caché pour bateaux fluviaux",
        "Funérailles, rues recouvertes de fumée",
    ),
    13: (
        "Cuisinent d'excellentes tartes",
        "Moulin à laine, pales en tissu éclatant",
        "Arnaqueur prépare un grand coup",
    ),
    14: (
        "Echappés d'un laboratoire, naïfs",
        "Une machine humaine, en service",
        "Scarabée dressé devient fou",
    ),
    15: (
        "Paressent au bord de l’eau",
        "Un pont en bois rejoint la colonie ",
        "Requête impossible d'une émissaire fée",
    ),
    16: (
        "Experts en exploration de grottes",
        "Tour tortueuse incroyablement haute ",
        "Plante à croissance rapide tout près",
    ),
    17: (
        "Creusent de gigantesques tunnels",
        "Magnifique jardin fleuri ",
        "Un héritage précieux a été volé",
    ),
    18: (
        "Elèvent des vers à soie",
        "Moulin à aubes ",
        "Seigneur chat demande une lourde dîme",
    ),
    19: (
        "Connus pour leurs écoles",
        "Statue d'un héros passé, à l'abandon ",
        "Menace humaine imminente et mortelle",
    ),
    20: (
        "En bons termes avec un prédateur",
        "Marché florissant ",
        "Tour de sorcier arrive, à dos de tortue",
    ),
}


name_prefixes = [
    "Chêne",
    "Baie",
    "Saule",
    "Souche",
    "Pin",
    "Lune",
    "Vert",
    "Noir",
    "Pierre",
    "Colline",
    "Figue",
    "Pomme",
    "Marais ",
    "Chouette ",
    "Renard ",
    "Gland",
    "Cuivre ",
    "Voleur",
    "Tomme",
    "Fosse",
    "Rose",
    "Cuivre ",
    "Cher",
    "Tronc",
]


name_suffixes = [
    "mas",
    "ville",
    "moulin",
    "vallon",
    "bois",
    "cité",
    "val",
    "source",
    "cendre",
    "buisson",
    "point",
    "éclat",
    "fort",
    "colline",
    "tour",
    "ferme",
    "pont",
    "porte",
    "crique",
    "mare",
    "nid",
    "gué",
    "tombe",
    "feu",
]


colony_size = {
    1: "Ferme/Manoir (1-3 familles)",
    2: "Croisement (3-5 familles)",
    3: "Hameau (50-150 souris)",
    4: "Village (150-300 souris)",
    5: "Ville (300-1000 souris)",
    6: "Cité (1000+ souris)",
}


def roll_colony_size():
    rolls = [random.randint(1, 6) for die in range(2)]
    kept = min(rolls)
    return colony_size.get(kept)


@dataclass
class Colony:
    inhabitants: str
    element_of_note: str
    event: str
    name: str
    size: str


def generate_colony_obj():
    inhabitants, element_of_note, event = [
        colony_details.get(random.randint(1, 20))[n] for n in range(3)
    ]
    name = f"{random.choice(name_prefixes)} {random.choice(name_suffixes)}"
    size = roll_colony_size()

    return Colony(inhabitants, element_of_note, event, name, size)


if __name__ == "__main__":
    print(generate_colony_obj())
