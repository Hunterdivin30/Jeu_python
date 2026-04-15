import fonction

stat = [
    {"type": "attaque", "valeur": None},
    {"type": "défense", "valeur": None},
    {"type": "PV", "valeur": None},
    {"type": "PT", "valeur": None}
]

fonction.info()
pseudo = fonction.initialisation_profil()
fonction.initialisation_stat(stat)
while stat[fonction.recherche_ordre(stat,"PV")]["valeur"] > 0:
    fonction.jeu(stat,pseudo)