def jeu(stat,pseudo):
    import fonction
    import sys
    
    if fonction.event() == "combat":
        fin_event = fonction.tour(stat,pseudo)
        if fin_event == "dead":
            print("Game Over")
            stop = input("Avez vous bien aimez le jeu ?")
            if stop == "yes":
                jeu()
            else:
                sys.exit()
        stat[fonction.recherche_ordre(stat,"PV")]["valeur"] = fin_event
        fonction.ajout_stat(stat)
        print(f"Vous avez maintenant {stat[fonction.recherche_ordre(stat,"PT")]["valeur"]} de point")

def info():
    print("Jeu développer par divin_hunter le 15 Avril 2026.")
    print("Titre: Monde des dieux")

def initialisation_profil():
    '''
    Renvoie un nom de type str.
    '''
    pseudo = None

    while pseudo == None:
        pseudo = str(input("Qu'elle est votre pseudo ?\n"))

    return pseudo

def initialisation_stat(tableau):
    '''
    Modifie les valeurs d'un tableau, aléatoirement entre 5 à 10.
    '''
    import random

    for numéro in range(len(tableau)):
        tableau[numéro]["valeur"] = random.randint(5,10)
        print(f"Votre {tableau[numéro]["type"]} vaut {tableau[numéro]["valeur"]}")

def event():
    '''
    Renvoie une valeur de type str entre ces évènements:
    - combat
    - rien
    '''
    import random
    liste_event = [{"event": "combat"}]
    num_event = 0
    return liste_event[num_event]["event"]

def recherche(stat,mot):
    '''
    Recherche la valeur d'un mot par rapport à la liste. le mot est de type str.
    '''
    for numéro in range(len(stat)):
        if stat[numéro]["type"] == mot:
            return stat[numéro]["valeur"]
        
def recherche_ordre(stat,mot):
    '''
    Recherche le rang d'un mot par rapport à la liste. le mot est de type str.
    '''
    for numéro in range(len(stat)):
        if stat[numéro]["type"] == mot:
            return numéro
        
def tour(stat,pseudo):
    '''
    Modifie les PV et PT des stats selon le combat, prend en compte l'attaque et la défense et même les PT.
    Le pseudo est noter dans les renvoies.
    '''
    import random
    import fonction

    choix = None
    pv = fonction.recherche(stat,"PV")
    ennemi_pv = random.randint(int(fonction.recherche(stat,"PT")/2),int(fonction.recherche(stat,"PT")))
    ennemi = fonction.choix_ennemi()
    print(f"un {ennemi} apparait avec {ennemi_pv} de PV.")

    while ennemi_pv >= 0:
        choix = str(input(f"Le {ennemi} est en vie, qu'est ce que je fais ?\n- attaquer\n- défendre\n- observer mes stats\n"))
        if choix == "attaquer" or "défendre":
            if choix == "attaquer":
                ennemi_dommage = int(random.randint(1,int(fonction.recherche(stat,"PV")-1)))

                pv = int(pv - ennemi_dommage)
                if pv <= 0:
                    print(f"{pseudo} a reçu {ennemi_dommage} de dégât, il lui reste 0 PV")
                    return "dead"
                print(f"{pseudo} a reçu {ennemi_dommage} de dégât, il lui reste {pv} PV")

                dommage = random.randint(1,fonction.recherche(stat,"attaque"))

                ennemi_pv -= dommage
                if ennemi_pv <= 0:
                    print(f"{pseudo} a donner {dommage} de dégât, il reste 0 de PV à {ennemi}")
                    print(f"{pseudo} a gagnez")
                    return pv
                print(f"{pseudo} a donner {dommage} de dégât, il reste {ennemi_pv} de PV à {ennemi}")

            elif choix == "défendre":
                ennemi_dommage = int(random.randint(1,int(fonction.recherche(stat,"PV")-4)))
                if ennemi_dommage <= random.randint(1,fonction.recherche(stat,"défense")):
                    dommage = random.randint(1,fonction.recherche(stat,"attaque"))

                    ennemi_pv -= dommage
                    if ennemi_pv <= 0:
                        print(f"{pseudo} a bloquer l'attaque, {pseudo} renvoie {dommage} de dégât, il reste 0 de PV à {ennemi}")
                        print(f"{pseudo} a gagnez")
                        return pv
                    print(f"{pseudo} a bloquer l'attaque, {pseudo} renvoie {dommage} de dégât, il reste {ennemi_pv} de PV à {ennemi}")
                else:
                    pv = int(pv - ennemi_dommage)
                    if pv <= 0:
                        print(f"{pseudo} a pas pu bloquer entièrement l'attaque, {pseudo} reçois {ennemi_dommage} de dégât, il lui reste 0 PV")
                        return "dead"
                    print(f"{pseudo} a pas pu bloquer entièrement l'attaque, {pseudo} reçois {ennemi_dommage} de dégât, il lui reste {pv} PV")
            elif choix == "observer mes stats":
                for numéro in range(len(stat)):
                    print(f"{pseudo} a {stat[numéro]["valeur"]} de {stat[numéro]["type"]}")
        
def ajout_stat(tableau):
    '''
    Modifie les stats d'attaque selon les PT gagner.
    '''
    import fonction
    import random

    for numéro in range(len(tableau)):
        if tableau[numéro]["type"] != "PT":
            tableau[numéro]["valeur"] += int(fonction.recherche(tableau,"PT") *  random.uniform(1,1.9))
            print(f"Votre {tableau[numéro]["type"]} est de {tableau[numéro]["valeur"]}")
    tableau[fonction.recherche_ordre(tableau,"PT")]["valeur"] += int(fonction.recherche_ordre(tableau,"PT") * random.uniform(1,3))

def choix_ennemi():
    '''
    Retourne un nom d'ennemi par la liste proposées.
    '''
    import random
    liste_ennemi = [
        {"nom": "Chasseur de dieu"}, 
        {"nom": "Géant de cristal"}, 
        {"nom":"Dieu"},
        {"nom":"Gardien du temple"},
        {"nom":"Cyclope"},
        {"nom":"Guerrier"},
        {"nom":"étoile"}
    ]

    return liste_ennemi[random.randint(0,2)]["nom"]