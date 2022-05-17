import random

from dataclasses import dataclass


@dataclass
class Seed:
    creature: str
    problem: str
    complication: str


def roll_seed(mix=False):
    seeds = {
        11: [
            "pêcheuse",
            "A été accusé d’un crime",
            "L'employé d'un PJ est responsable",
        ],
        12: [
            "Famille dissidente",
            "Cherche une nouvelle maison",
            "Il faut traverser rivière",
        ],
        13: [
            "Sorcier",
            "suivi",
            "L'antagoniste est sa propre ombre",
        ],
        14: [
            "Gardien de cafards",
            "A découvert un étrange artefact",
            "Il est amnésique",
        ],
        15: ["Fermier", "Témoin d’un présage inquiétant", "L'antagoniste est déguisé"],
        16: [
            "Souris des Bourgs",
            "assassiner un rival",
            "La maison d'un PJ est impliquée",
        ],
        21: [
            "Fourrageur",
            "retrouver un trésor perdu",
            "C'est protégé par d'étranges bêtes",
        ],
        22: [
            "Commerçant",
            "A vu sa maison se faire détruire",
            "L'antagoniste est un ami très proche",
        ],
        23: [
            "Marchand itinérant",
            "Dépouillé d'un bien précieux",
            "C'est le véritable antagoniste",
        ],
        24: [
            "Chevaucheur de pigeon",
            "A été kidnappé",
            "L'ami d'un PJ est impliqué",
        ],
        25: ["Brasseur", "A été exilé de son village", "Il a été piégé"],
        26: ["Herboriste", "Cherche un remède rare", "C'est très urgent"],
        31: ["Messager", "A perdu son chemin", "Il dispose d'une information vitale"],
        32: [
            "Vagabond",
            "S'est fait voler toute sa nourriture",
            "L'antagoniste a une bonne raison",
        ],
        33: [
            "Sujet d'expériences",
            "Est pourchassé par des humains",
            "Il est suivi par une puce",
        ],
        34: [
            "Mineur d'étain",
            "A été détroussé par des bandits",
            "L'antagoniste est complètement saoûl",
        ],
        35: [
            "Boulanger",
            "A mangé une baie empoisonnée",
            "L'antagoniste est un membre de la famille",
        ],
        36: [
            "Chevalier des ",
            "Haies",
            "Un membre de sa famille a disparu",
            "Il est mourant",
        ],
        41: [
            "Collecteur d'impôts",
            "A perdu un grand nombre de pépins",
            "Il est complètement bourré",
        ],
        42: [
            "Matriarche",
            "A été accusé de meurtre",
            "L'antagoniste est un change-forme",
        ],
        43: [
            "Prospecteur",
            "Sa tortue de trait est coincée",
            "Il est bien plus riche qu'il ne le semble",
        ],
        44: [
            "Chef de la Guilde des Tunnels ",
            "A été assassiné",
            "Le rival d'un PJ est impliqué",
        ],
        45: [
            "Noble souris",
            "Sa maison est attaquée",
            "L'antagoniste cherche à se venger",
        ],
        46: ["Bandit rat", "Veut voler un rival", "Un fantôme hante les lieux"],
        51: [
            "Reine abeille",
            "Voyage vers un nouveau domicile",
            "Ses suivants ne sont pas d'accord",
        ],
        52: [
            "Officier de l'armée fourmi",
            "Est chassé par des ennemis",
            "Il est sérieusement blessé",
        ],
        53: ["Mage Hibou", "Veut retrouver un sort rare", "C'est au fond d'une grotte"],
        54: ["Seigneur Chat", "Veut être diverti", "Il a piégé les PJ"],
        55: ["Caneton", "A perdu sa mère", "Il doit rejoindre une île"],
        56: [
            "Mille-pattes géant",
            "Veut un endroit chaud où dormir",
            "A besoin d'un objet porté par un PJ",
        ],
        61: [
            "Ambassadeur Lilliputien",
            "Veut atteindre la reine souris",
            "Ne comprend pas les coutumes locales",
        ],
        62: [
            "Fantôme piégé",
            "Veut trouver le grand amour",
            "Ne peut pas quitter ce lieu",
        ],
        63: ["Emissaire fée", "Veut enlever une souris", "Sa cible est un PJ"],
        64: [
            "Nuée de midges",
            "Veut voler une des souris-joueuses",
            "L'antagoniste est exceptionnellement doué",
        ],
        65: ["Mémé araignée", "A perdu un trésor ancien", "Elle l'a avalé"],
        66: ["Oisillon", "Ne peut pas rentrer à la maison", "Doit grimper à un arbre"],
    }
    if not mix:
        creature, problem, complication = seeds.get(random.choice(list(seeds.keys())))
    else:
        creature, problem, complication = [
            seeds.get(random.choice(list(seeds.keys())))[k] for k in range(3)
        ]
    return Seed(creature, problem, complication)


if __name__ == "__main__":
    print(roll_seed(mix=True))
