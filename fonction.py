def indice_liste(liste,mot,clès):
    '''
    Recherche l'indice d'une liste par rapport à un mot souhaitez.
    Une clès est nécessaire si la liste en possède.
    - L'indice renvoyez est de type int.
    - la liste doit être de type list.
    - le mot et la clès doit être de type str.
    Renvoie "False" lorsque le mot n'est pas trouvez.
    '''
    assert isinstance(liste, list), "Le tableau doit être de type list"
    assert isinstance(mot, str), "Le mot rechercher doit être de type str"

    if clès == None:
        for indice in range(len(liste)):
            if liste[indice] == mot:
                return indice
    elif clès != None:
        assert isinstance(clès, str), "La clès rechercher doit être de type str"
        for indice in range(len(liste)):
            if liste[indice][clès] == mot:
                return indice
    return False

def vérif_question(choix_disponible,phrase):
    '''
    Renvoie la reponse si l'utilisateur répond correctement à la question proposer par la phrase.
    - les choix disponibles doit être remplie et sous une liste.
    - la phrase doit être de type str.
    '''
    import fonction

    assert isinstance(choix_disponible, list), "Les choix doit être dans une liste de type list"
    assert len(choix_disponible) > 0, "La liste des choix doit être non vide."
    assert isinstance(phrase, str), "La phrase doit être de type str"

    boucle = False
    while boucle == False:
        reponse = str(input(f"{phrase}\n"))
        if choix_disponible[fonction.indice_liste(choix_disponible,reponse,None)] != False:
            return reponse
        print("Réponse invalide, vous devez répondre par rapport aux choix disponibles.")

def attaquer(stat_joueur,objets,profil_joueur,stat_monstre):
    '''
    Renvoie False si l'utilisateur à perdu ou True si il a gagné, sinon modifie les PV du monstre et de l'utilisateur et ne renvoie rien.
    - Tout les paramètres doivent être de type list.
    '''
    import fonction
    import random

    assert isinstance(stat_joueur, list), "Les stats doit être dans une liste de type list"
    assert isinstance(objets, list), "Les objets doit être dans une liste de type list"
    assert isinstance(profil_joueur, list), "Le profil doit être dans une liste de type list"
    assert isinstance(stat_monstre, list), "Les stats ennemis doit être dans une liste de type list"

    chance_objet = 2
    if profil_joueur[fonction.indice_liste(profil_joueur, "objet", "nom")]["valeur"] != None:
        if objets[fonction.indice_liste(objets, profil_joueur[fonction.indice_liste(profil_joueur, "objet", "nom")]["valeur"], "nom")]["type"] == "attaque":
            chance_objet = random.randint(1,2)
    
    if chance_objet == 1:
        dommage = int( objets[  fonction.indice_liste( objets , str(profil_joueur[fonction.indice_liste(profil_joueur,"objet","nom")]["valeur"]) , "nom" )  ][  "valeur"  ] * profil_joueur[fonction.indice_liste(profil_joueur, "attaque", "nom")]["valeur"] * random.uniform(0.1,1) )
        dommage_ennemi = int( stat_monstre[fonction.indice_liste(stat_monstre,"puissance", "nom")]["valeur"] * (stat_monstre[fonction.indice_liste(stat_monstre,"vie", "nom")]["valeur"] / 2) * profil_joueur[fonction.indice_liste(profil_joueur,"point","nom")]["valeur"] * random.uniform(0.1,1) )

        chance_attaque = random.randint(1,2)
        if chance_attaque == 1:
            print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} attaque en premier avec {dommage_ennemi} de dégât.")

            stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"] -= dommage_ennemi
            if stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"] <= 0:
                print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as plus que 0 de vie, vous êtes mort.")
                return False
            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as plus que {stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"]} de vie.")


            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} contre-attaque avec {profil_joueur[fonction.indice_liste(profil_joueur, "objet", "nom")]["valeur"]} pour {dommage_ennemi} de dégât.")

            stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"] -= dommage
            if stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"] <= 0:
                print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} n'as plus que 0 de vie, vous avez gagnez.")
                return True
            print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} n'as plus que {stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"]} de vie.")

        elif chance_attaque == 2:
            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} attaque en premier avec {profil_joueur[fonction.indice_liste(profil_joueur, "objet", "nom")]["valeur"]} pour {dommage_ennemi} de dégât.")

            stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"] -= dommage
            if stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"] <= 0:
                print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} n'as plus que 0 de vie, vous avez gagnez.")
                return True
            print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} n'as plus que {stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"]} de vie.")


            print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} contre-attaque avec {dommage_ennemi} de dégât.")

            stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"] -= dommage_ennemi
            if stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"] <= 0:
                print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as plus que 0 de vie, vous êtes mort.")
                return False
            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as plus que {stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"]} de vie.")


    elif chance_objet == 2:
        dommage = int(profil_joueur[fonction.indice_liste(profil_joueur, "attaque", "nom")]["valeur"] * random.uniform(0.1,1))
        dommage_ennemi = int( stat_monstre[fonction.indice_liste(stat_monstre,"puissance", "nom")]["valeur"] * (stat_monstre[fonction.indice_liste(stat_monstre,"vie", "nom")]["valeur"] / 2) * profil_joueur[fonction.indice_liste(profil_joueur,"point","nom")]["valeur"] * random.uniform(0.1,1) )

        chance_attaque = random.randint(1,2)
        if chance_attaque == 1:
            print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} attaque en premier avec {dommage_ennemi} de dégât.")

            stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"] -= dommage_ennemi
            if stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"] <= 0:
                print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as plus que 0 de vie, vous êtes mort.")
                return False
            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as plus que {stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"]} de vie.")


            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} contre-attaque avec {dommage_ennemi} de dégât.")

            stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"] -= dommage
            if stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"] <= 0:
                print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} n'as plus que 0 de vie, vous avez gagnez.")
                return True
            print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} n'as plus que {stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"]} de vie.")

        elif chance_attaque == 2:
            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} attaque en premier avec {dommage_ennemi} de dégât.")

            stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"] -= dommage
            if stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"] <= 0:
                print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} n'as plus que 0 de vie, vous avez gagnez.")
                return True
            print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} n'as plus que {stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"]} de vie.")


            print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} contre-attaque avec {dommage_ennemi} de dégât.")

            stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"] -= dommage_ennemi
            if stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"] <= 0:
                print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as plus que 0 de vie, vous êtes mort.")
                return False
            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as plus que {stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"]} de vie.")
    return None




def défense(stat_joueur,objets,profil_joueur,stat_monstre):
    '''
    Renvoie False si l'utilisateur à perdu ou True si il a gagné, sinon modifie les PV du monstre et de l'utilisateur et ne renvoie rien.
    - Tout les paramètres doivent être de type list.
    '''
    import fonction
    import random

    assert isinstance(stat_joueur, list), "Les stats doit être dans une liste de type list"
    assert isinstance(objets, list), "Les objets doit être dans une liste de type list"
    assert isinstance(profil_joueur, list), "Le profil doit être dans une liste de type list"
    assert isinstance(stat_monstre, list), "Les stats ennemis doit être dans une liste de type list"

    chance_objet = 2
    if profil_joueur[fonction.indice_liste(profil_joueur, "objet", "nom")]["valeur"] != None:
        if objets[fonction.indice_liste(objets, profil_joueur[fonction.indice_liste(profil_joueur, "objet", "nom")]["valeur"], "nom")]["type"] == "défense":
            chance_objet = random.randint(1,2)
    
    if chance_objet == 1:
        défense = int( objets[  fonction.indice_liste( objets , str(profil_joueur[fonction.indice_liste(profil_joueur,"objet","nom")]["valeur"]) , "nom" )  ][  "valeur"  ] * profil_joueur[fonction.indice_liste(profil_joueur, "défense", "nom")]["valeur"] * random.uniform(0.1,1) )
        dommage_ennemi = int( stat_monstre[fonction.indice_liste(stat_monstre,"puissance", "nom")]["valeur"] * (stat_monstre[fonction.indice_liste(stat_monstre,"vie", "nom")]["valeur"] / 2) * profil_joueur[fonction.indice_liste(profil_joueur,"point","nom")]["valeur"] * random.uniform(0.1,1) )
        riposte = int(profil_joueur[fonction.indice_liste(profil_joueur, "attaque", "nom")]["valeur"] * random.uniform(0.1,1))

        if défense >= dommage_ennemi:
            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} bloque l'attaque avec son {profil_joueur[fonction.indice_liste(profil_joueur,"objet","nom")]["valeur"]} et renvoie {riposte} de dégât.")

            stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"] -= riposte
            if stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"] <= 0:
                print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} n'as plus que 0 de vie, vous avez gagnez.")
                return True
            print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} n'as plus que {stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"]} de vie.")

        elif défense < dommage_ennemi:
            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as pas pu bloquez l'attaque et reçois {dommage_ennemi - défense} de dégât.")

            stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"] -= dommage_ennemi - défense
            if stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"] <= 0:
                print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as plus que 0 de vie, vous êtes mort.")
                return False
            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as plus que {stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"]} de vie.")


    elif chance_objet == 2:
        défense = int( profil_joueur[fonction.indice_liste(profil_joueur, "défense", "nom")]["valeur"] * random.uniform(0.1,1) )
        dommage_ennemi = int( stat_monstre[fonction.indice_liste(stat_monstre,"puissance", "nom")]["valeur"] * (stat_monstre[fonction.indice_liste(stat_monstre,"vie", "nom")]["valeur"] / 2) * profil_joueur[fonction.indice_liste(profil_joueur,"point","nom")]["valeur"] * random.uniform(0.1,1) )
        riposte = int(profil_joueur[fonction.indice_liste(profil_joueur, "attaque", "nom")]["valeur"] * random.uniform(0.1,1))

        if défense >= dommage_ennemi:
            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} bloque l'attaque et renvoie {riposte} de dégât.")

            stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"] -= riposte
            if stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"] <= 0:
                print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} n'as plus que 0 de vie, vous avez gagnez.")
                return True
            print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} n'as plus que {stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"]} de vie.")

        elif défense < dommage_ennemi:
            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as pas pu bloquez l'attaque et reçois {dommage_ennemi - défense} de dégât.")

            stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"] -= dommage_ennemi - défense
            if stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"] <= 0:
                print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as plus que 0 de vie, vous êtes mort.")
                return False
            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as plus que {stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"]} de vie.")
    return None


def pouvoir(element_attaque,profil_joueur,stat_joueur,objets,stat_monstre):
    '''
    Renvoie False si l'utilisateur à perdu ou True si il a gagné, sinon modifie les PV du monstre et de l'utilisateur et ne renvoie rien.
    - Tout les paramètres doivent être de type list.
    '''
    import fonction
    import random

    assert isinstance(stat_joueur, list), "Les stats doit être dans une liste de type list"
    assert isinstance(objets, list), "Les objets doit être dans une liste de type list"
    assert isinstance(profil_joueur, list), "Le profil doit être dans une liste de type list"
    assert isinstance(stat_monstre, list), "Les stats ennemis doit être dans une liste de type list"
    assert isinstance(element_attaque, list), "Les attaques des élément doit être dans une liste de type list"

    chance_objet = 2
    if profil_joueur[fonction.indice_liste(profil_joueur, "objet", "nom")]["valeur"] != None:
        if objets[fonction.indice_liste(objets, profil_joueur[fonction.indice_liste(profil_joueur, "objet", "nom")]["valeur"], "nom")]["type"] == "magie":
            chance_objet = random.randint(1,2)
    
    if chance_objet == 1:
        dommage = int( objets[  fonction.indice_liste( objets , str(profil_joueur[fonction.indice_liste(profil_joueur,"objet","nom")]["valeur"]) , "nom" )  ][  "valeur"  ] * profil_joueur[fonction.indice_liste(profil_joueur, "attaque", "nom")]["valeur"] * random.uniform(0.1,1) )
        dommage_ennemi = int( stat_monstre[fonction.indice_liste(stat_monstre,"puissance", "nom")]["valeur"] * (stat_monstre[fonction.indice_liste(stat_monstre,"vie", "nom")]["valeur"] / 2) * profil_joueur[fonction.indice_liste(profil_joueur,"point","nom")]["valeur"] * random.uniform(0.1,1) )

        liste_disponible = []
        cmpt = 1
        print("Vous avez le choix entre ces types d'attaque de votre pouvoir")
        for indice in range(len(element_attaque)):
            if element_attaque[indice]["cout"] <= stat_joueur[fonction.indice_liste(stat_joueur,"nexum","nom")]["valeur"]: 
                print(f"{element_attaque[indice]["attaque"]}: {element_attaque[indice]["cout"]} nexum")
                liste_disponible.append(cmpt)
                cmpt += 1

        cout = element_attaque[fonction.vérif_question(liste_disponible, "Quel attaque souhaitez vous utilisez ?")]["cout"]
        stat_joueur[fonction.indice_liste(stat_joueur,"nexum","nom")]["valeur"] -= cout
        dommage += cout
        if stat_monstre[fonction.indice_liste(stat_monstre, "faiblesse", "nom")]["valeur"] == profil_joueur[fonction.indice_liste(profil_joueur,"pouvoir", "nom")]["valeur"]:
            dommage *= 2

        chance_attaque = random.randint(1,2)
        if chance_attaque == 1:
            print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} attaque en premier avec {dommage_ennemi} de dégât.")

            stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"] -= dommage_ennemi
            if stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"] <= 0:
                print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as plus que 0 de vie, vous êtes mort.")
                return False
            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as plus que {stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"]} de vie.")


            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} contre-attaque avec {profil_joueur[fonction.indice_liste(profil_joueur, "objet", "nom")]["valeur"]} pour {dommage_ennemi} de dégât.")

            stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"] -= dommage
            if stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"] <= 0:
                print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} n'as plus que 0 de vie, vous avez gagnez.")
                return True
            print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} n'as plus que {stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"]} de vie.")

        elif chance_attaque == 2:
            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} attaque en premier avec {profil_joueur[fonction.indice_liste(profil_joueur, "objet", "nom")]["valeur"]} pour {dommage_ennemi} de dégât.")

            stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"] -= dommage
            if stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"] <= 0:
                print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} n'as plus que 0 de vie, vous avez gagnez.")
                return True
            print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} n'as plus que {stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"]} de vie.")


            print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} contre-attaque avec {dommage_ennemi} de dégât.")

            stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"] -= dommage_ennemi
            if stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"] <= 0:
                print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as plus que 0 de vie, vous êtes mort.")
                return False
            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as plus que {stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"]} de vie.")


    elif chance_objet == 2:
        dommage = int( objets[  fonction.indice_liste( objets , str(profil_joueur[fonction.indice_liste(profil_joueur,"objet","nom")]["valeur"]) , "nom" )  ][  "valeur"  ] * profil_joueur[fonction.indice_liste(profil_joueur, "attaque", "nom")]["valeur"] * random.uniform(0.1,1) )
        dommage_ennemi = int( stat_monstre[fonction.indice_liste(stat_monstre,"puissance", "nom")]["valeur"] * (stat_monstre[fonction.indice_liste(stat_monstre,"vie", "nom")]["valeur"] / 2) * profil_joueur[fonction.indice_liste(profil_joueur,"point","nom")]["valeur"] * random.uniform(0.1,1) )

        liste_disponible = []
        cmpt = 1
        print("Vous avez le choix entre ces types d'attaque de votre pouvoir")
        for indice in range(len(element_attaque)):
            if element_attaque[indice]["cout"] <= stat_joueur[fonction.indice_liste(stat_joueur,"nexum","nom")]["valeur"]: 
                print(f"{cmpt} - {element_attaque[indice]["attaque"]}: {element_attaque[indice]["cout"]} nexum")
                liste_disponible.append(cmpt)
                cmpt += 1

        cout = element_attaque[fonction.vérif_question(liste_disponible, "Quel attaque souhaitez vous utilisez ?")]["cout"]
        stat_joueur[fonction.indice_liste(stat_joueur,"nexum","nom")]["valeur"] -= cout
        dommage += cout
        if stat_monstre[fonction.indice_liste(stat_monstre, "faiblesse", "nom")]["valeur"] == profil_joueur[fonction.indice_liste(profil_joueur,"pouvoir", "nom")]["valeur"]:
            dommage *= 2

        chance_attaque = random.randint(1,2)
        if chance_attaque == 1:
            print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} attaque en premier avec {dommage_ennemi} de dégât.")

            stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"] -= dommage_ennemi
            if stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"] <= 0:
                print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as plus que 0 de vie, vous êtes mort.")
                return False
            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as plus que {stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"]} de vie.")


            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} contre-attaque avec {dommage_ennemi} de dégât.")

            stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"] -= dommage
            if stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"] <= 0:
                print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} n'as plus que 0 de vie, vous avez gagnez.")
                return True
            print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} n'as plus que {stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"]} de vie.")

        elif chance_attaque == 2:
            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} attaque en premier avec {dommage_ennemi} de dégât.")

            stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"] -= dommage
            if stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"] <= 0:
                print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} n'as plus que 0 de vie, vous avez gagnez.")
                return True
            print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} n'as plus que {stat_monstre[fonction.indice_liste(stat_monstre, "vie", "nom")]["valeur"]} de vie.")


            print(f"{stat_monstre[fonction.indice_liste(stat_monstre,"nom", "nom")]["valeur"]} contre-attaque avec {dommage_ennemi} de dégât.")

            stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"] -= dommage_ennemi
            if stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"] <= 0:
                print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as plus que 0 de vie, vous êtes mort.")
                return False
            print(f"{profil_joueur[fonction.indice_liste(profil_joueur,"pseudo", "nom")]["valeur"]} n'as plus que {stat_joueur[fonction.indice_liste(stat_joueur, "vie", "nom")]["valeur"]} de vie.")
    return None

def call_stat(profil,stats):
    '''
    Renvoie à la console les informations sur les deux listes.
    - Tout les paramètres doivent être de type list.
    '''

    assert isinstance(stats, list), "Les stats doit être dans une liste de type list"
    assert isinstance(profil, list), "Les informations du profil doit être dans une liste de type list"

    for indice in range(len(profil)):
        print(f"{profil[indice]["nom"]}: {profil[indice]["valeur"]}")

    for indice in range(len(stats)):
        print(f"{profil[indice]["nom"]}: {profil[indice]["valeur"]}")

def inventaire(objets,profil):
    '''
    Changes les valeurs du profil selon l'objet équipés.
    - Tout les paramètres doivent être de type list.
    '''
    import fonction

    assert isinstance(objets, list), "Les objets doit être dans une liste de type list"
    assert isinstance(profil, list), "Les informations du profil doit être dans une liste de type list"

    liste_disponible = []
    cmpt = 1
    print("Voici les objets disponibles:")
    for indice in range(len(objets)):
        print(f"{cmpt} - {objets[indice]["nom"]}: {objets[indice]["type"]}.")
        liste_disponible.append(cmpt)
        cmpt += 1
    profil[fonction.indice_liste(profil,"objet","nom")]["valeur"] = objets[fonction.vérif_question(liste_disponible, "Quel attaque souhaitez vous utilisez ?")]["nom"]

def spawn_monstre(monstres, profil_monstre, profil_joueur):
    '''
    Changes les valeurs du profil selon le monstre choisis.
    - Tout les paramètres doivent être de type list.
    '''
    import random
    import fonction

    assert isinstance(monstres, list), "Les monstres doit être dans une liste de type list"
    assert isinstance(profil_monstre, list), "Les informations du profil du monstre doit être dans une liste de type list"
    assert isinstance(profil_joueur, list), "Les informations du profil doit être dans une liste de type list"

    indice = random.randint(0,len(monstres)-1)
    profil_monstre[fonction.indice_liste(profil_monstre, "nom", "nom")]["valeur"] = monstres[indice]["nom"]
    profil_monstre[fonction.indice_liste(profil_monstre, "puissance", "nom")]["valeur"] = monstres[indice]["valeur"]
    profil_monstre[fonction.indice_liste(profil_monstre, "faiblesse", "nom")]["valeur"] = monstres[indice]["faiblesse"]
    profil_monstre[fonction.indice_liste(profil_monstre, "description", "nom")]["valeur"] = monstres[indice]["description"]
    profil_monstre[fonction.indice_liste(profil_monstre, "vie", "nom")]["valeur"] = int((monstres[indice]["valeur"] * profil_joueur[fonction.indice_liste(profil_joueur, "point", "nom")]["valeur"]) / 2)