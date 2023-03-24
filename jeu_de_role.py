import random
import sys



nb_potions = 3

pv_joueur = 50
pv_enemi =50


while pv_joueur or pv_enemi != 0:
        try:
                choix_menu = int(input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? : "))
                if choix_menu == 1:
                                
                                degats_joueur = random.randint(5,15)
                                degats_enemi = random.randint(10,30)
                                pv_enemi -= degats_joueur
                                pv_joueur -= degats_enemi
                                print(f"Vous infligez {degats_joueur} a l'enemi !")
                                print(f"HP enemi : {pv_enemi}/50")
                                if pv_enemi <= 0:
                                        print("Vous avez gagné !")
                                        sys.exit()
                                else:
                                        print(f"l'enemi attaque ! il vous inflige {degats_enemi} points de dégats !")
                                        if pv_joueur <= 0:
                                                print(f"Vous n'avez plus de PV...")
                                                print("vous avez perdu.")
                                                sys.exit()
                                        else:
                                                print(f"Il vous reste {pv_joueur}")


                elif choix_menu ==2:
                        if nb_potions <= 0:
                                print("Vous n'avez plus de potions !")
                                continue
                        else:
                                nb_potions -= 1
                                soins = random.randint(15,50)
                                pv_joueur +=  soins
                                degats_enemi = random.randint(5,15)
                                pv_joueur -= degats_enemi
                                print(f"Vous consomez une potion de santé")
                                print(f"Vous récuperez {soins} PV, santé actuelle : {pv_joueur}")
                                print(f"l'enemi attaque ! il vous inflige {degats_enemi} points de dégats !")
                                print(f"Il vous reste {pv_joueur}")
                else:
                        print("Veuillez saisir un choix valide svp")
        except ValueError:
                print("Veuillez saisir un choix valide")  

        print("-" * 20)
        print(f"VOS PV : {pv_joueur}")
        print(f"PV ENEMI : {pv_enemi}")
        print("-" * 20)
        




