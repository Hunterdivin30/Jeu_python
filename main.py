# ===== initialisation des listes ===== #
Liste_profil = [
    {"nom": "pseudo","valeur": None, "description": "Le pseudo permet de représenter votre personnage."},
    {"nom": "pouvoir", "valeur": None, "description": "Le pouvoir correspond au pouvoir que vous avez choisi au début du jeu."},
    {"nom": "objet", "valeur": None, "description": "Vous ne pouvez qu'avoir un seule objet, cette objet permet d'avoir des bonus sois dans l'attaque, sois dans la défense."},
    {"nom": "point", "valeur": None, "description": "Les points correspond à votre niveau dans le jeu."}
]

liste_stat = [
    {"nom": "attaque", "valeur": None, "description": "L'attaque correspond à la puissance de votre personnage à renvoyer des dégâts."},
    {"nom": "défense", "valeur": None, "description": "La défense correspond à la réduction des dégâts par votre personnage."},
    {"nom": "nexum", "valeur": None, "description": "Le nexum est la quantité de pouvoir que vous pouvez utilisez face aux ennemis."},
    {"nom": "vie", "valeur": None, "description": "La vie est la chose la plus essentiel, elle permet de continuer à jouez."}
]

liste_objet = [
    {"nom": "Bâton en bois", "valeur": 1, "type": "attaque", "description": "Ce petit bout de bois pourrez vous être utile dès le début."},
    {"nom": "Veste en cuir", "valeur": 1, "type": "défense", "description": "La veste en cuir vous permet de rester en chaud, de plus que les griffes ennemis auront plus de mal à vous atteindre."},
    {"nom": "Bouclier en bois", "valeur": 1, "type": "défense", "description": "Un rond composée de bois vous pourrez vous êtes utile lorsque vous essayerai de bloquer des attaques."},
    {"nom": "Lames de fer", "valeur": 3, "type": "attaque", "description": "Une lame très longue vous permettant d'abbatre vos ennemis."}
]

liste_objet_disponible_attaque = []

liste_element = [
    {"nom": "feu", "disponible": "yes", "description": "Le feu est l'élément principal à la création de la température et de la vie, sans elle, nous seront dans un environnement froid et inhabitable."},
    {"nom": "lumière", "disponible": "yes", "description": "La lumière permet de mettre la couleur dans le monde, elle est extrêment puissante face aux ténebres."},
    {"nom": "eau", "disponible": "yes", "description": "L'eau est un élément majeur et permet de rééquilibrer d'autre élément."},
    {"type": "terre", "disponible": "no", "description": "La terre compose tout les matériaux solide du monde, son pouvoir lui permet de prendre plusieurs forme."}
]

liste_element_attaque = [
    {"nom": "feu", "attaque": "Lance flamme", "cout": 10},{"nom": "feu", "attaque": "Boule de feu", "cout": 15},{"nom": "feu", "attaque": "Flammèche", "cout": 5},
    {"nom": "lumière", "attaque": "Lumière aveuglante", "cout": 5}, {"nom": "lumière", "attaque": "Laser lumineux", "cout": 20},
    {"nom": "eau", "attaque": "flèche humide", "cout": 3}, {"nom": "eau", "attaque": "tsunami", "cout": 20}
]

liste_element_disponible = []
# Listes des monstres #

liste_profil_monstre = [
    {"nom": "vie", "valeur": None},
    {"nom": "puissance", "valeur": None},
    {"nom": "nom", "valeur": None},
    {"nom": "faiblesse", "valeur": None},
    {"nom": "description", "valeur": None}
]

liste_monstre_grottes = [
    {"nom": "Chauves souris des ombres", "valeur": 1, "faiblesse": "lumière", "description": "Une petite chauves souris d'un regard rouge et d'une envellope noir brumeux."},
    {"nom": "Rocher vivant", "valeur": 2, "faiblesse": "eau", "description": "Un rocher surprenant tout explorateur des cavernes, elle n'est pas rocheuse, mais semble organique."},
    {"nom": "Explorateur enragé", "valeur": 1, "faiblesse": "feu", "description": "Un humain étant corrompu, mais par quoi ?"},
    {"nom": "Silouhette sombre", "valeur": 1, "faiblesse" : "lumière", "description": "Qu'est que sait ?"}
]

# ==================== #

liste_choix = ["attaquer", "défendre", "pouvoir", "stats?", "inventaire"]

# =============================================================================== #

import fonction
import random

print("Titre: Oria world - L'univers des dieux")
print("Développer par Oria Production.")
print("Version: Demo")
print("") # Espace pour laisser les autres fonctions écrires et aérer la console.

print("Il était une fois, un mortel, recevant la bénidiction de l'illusionniste.")
print("Cette bénidiction lui offrait le pouvoir de recevoir tout les pouvoirs des anciens gardiens disparu durant l'ère du chaos.")
print("Son dessein était maintenant désinnée... Faire renaitre ce monde détruit.")

Liste_profil[fonction.indice_liste(Liste_profil, "pseudo", "nom")]["valeur"] = str(input("Qu'elle est votre pseudo ?\n"))

print("Vous avez le choix entre ces types d'élément.")
liste_disponible = []
cmpt = 1
for indice in range(len(liste_element)):
    if liste_element[indice]["disponible"] == "yes":
        print(f"{cmpt} - {liste_element[indice]["nom"]}")
        print(f"Description: {liste_element[indice]["description"]}")
        print("")
        liste_disponible.append(cmpt)
        cmpt += 1

Liste_profil[fonction.indice_liste(Liste_profil, "pouvoir", "nom")]["valeur"] = liste_element[int(fonction.vérif_question(liste_disponible, "Quel attaque souhaitez vous utilisez ?"))]["nom"]
for indice in range(len(liste_element_attaque)):
    if liste_element_attaque[indice]["nom"] == Liste_profil[fonction.indice_liste(Liste_profil, "pouvoir", "nom")]["valeur"]:
        liste_objet_disponible_attaque.append(liste_element_attaque[indice])

print(f"{Liste_profil[fonction.indice_liste(Liste_profil,"pseudo","nom")]["valeur"]} récupère ces stats suivant:")
liste_disponible = []
cmpt = 1
for indice in range(len(liste_stat)):
    liste_stat[indice]["valeur"] = random.randint(5,20)
    print(f"- {cmpt} {liste_stat[indice]["nom"]}: {liste_stat[indice]["valeur"]}")
    liste_disponible.append(cmpt)
    cmpt += 1
boucle = False
while boucle != True:
    indice = fonction.vérif_question(liste_disponible, "Qu'elle description souhaitez vous voir ?")
    if indice != int:
        boucle = True
    else:
        print(f"Description: {liste_stat[indice]["description"]}")

while liste_stat[fonction.indice_liste(liste_stat, "vie", "nom")]["valeur"] > 0:
    fonction.spawn_monstre(liste_monstre_grottes, liste_profil_monstre, Liste_profil)
    print(f"Un {liste_profil_monstre[fonction.indice_liste(liste_profil_monstre, "nom", "nom")]["valeur"]} apparait")

    while liste_profil_monstre[fonction.indice_liste(liste_profil_monstre, "vie", "nom")]["valeur"] > 0:
        print(f"Le {liste_profil_monstre[fonction.indice_liste(liste_profil_monstre, "nom", "nom")]["valeur"]} est en vie")
        liste_disponible = []
        cmpt = 1
        for indice in range(len(liste_choix)):
                print(f"{cmpt} - {liste_choix[indice]}")
                print("")
                liste_disponible.append(cmpt)
                cmpt += 1
        choix = fonction.vérif_question(liste_disponible, "Que faites vous ?")
        if choix == liste_choix[fonction.indice_liste(liste_choix, "attaquer", None)]:
            fonction.attaquer(liste_stat,liste_objet,Liste_profil,liste_profil_monstre)
        elif choix == liste_choix[fonction.indice_liste(liste_choix, "défendre", None)]:
             fonction.défense(liste_stat,liste_objet,Liste_profil,liste_profil_monstre)
        elif choix == liste_choix[fonction.indice_liste(liste_choix, "pouvoir", None)]:
             fonction.pouvoir(liste_element_disponible,Liste_profil,liste_stat,liste_objet,liste_profil_monstre)
        elif choix == liste_choix[fonction.indice_liste(liste_choix, "stats?", None)]:
             fonction.call_stat(Liste_profil,liste_stat)
        elif choix == liste_choix[fonction.indice_liste(liste_choix, "inventaire", None)]:
             fonction.inventaire(liste_objet, Liste_profil)

    for indice in range(len(liste_stat)):
        liste_stat[indice]["valeur"] += random.randint(1,Liste_profil[fonction.indice_liste(Liste_profil,"point","nom")]["valeur"])
    Liste_profil[fonction.indice_liste(Liste_profil,"point","nom")]["valeur"] += random.randint(1,Liste_profil[fonction.indice_liste(Liste_profil,"point","nom")]["valeur"])