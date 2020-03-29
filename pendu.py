import donnees
import fonctions
import random
import pickle
from os import path

#initialisation
mot_liste = donnees.mots_listes
index = random.randrange(len(mot_liste))
mot = list(mot_liste[index])
essais = donnees.nombre_essais
file_path = donnees.path_user_file

#check if file exists
if path.exists(file_path) == False:
    io = open(file_path,"wb")
    mon_pick = pickle.Pickler(io)
    dictionnaire = dict()
    mon_pick.dump(dictionnaire)
    io.close()

#nom joueur
nom_joueur = input("Veuillez rensigner votre nom : ")
score_joueur = 0
dictionnaire = dict() # score des joueur
exists = path.exists(file_path)

if exists == True:
    io = open(file_path,"rb")
    mon_pick = pickle.Unpickler(io)
    dictionnaire = mon_pick.load()
    if nom_joueur in dictionnaire:
        score_joueur = dictionnaire[nom_joueur]
        print("bienvenue {}, votre dernier score lors de la dernière partie était : {} \n nous vous souhaitons une bonne chance :)".format(nom_joueur,score_joueur))
    else:
        score_joueur = 5
        print("étant donné que vous etes un nouveau client, nous vous attrions un score cadeau de 5 point, bonne chance !")
    io.close()

print("Voici le mot que vous devez deviner lettre par lettre :")
#creation dune liste de liste, chaque element contient [0,"lettre"] s'il n'est pas encore trouvé
# et [1,"lettre"] si elle a été déja trouvé 
map = list()
for j, elt in enumerate(mot):
    map.append([0,elt])

# copie du mot
mot_original = mot.copy()

#init variable de la boucle while
partie = True; i =0
while(partie):
    if i>=essais :
        print("vous avez perdu ! le mot était : ",str(mot_original))
        partie = False
        break


    fonctions.printMot(map)
    lettre = input("devinez une lettre :")
    i+=1
    if lettre in mot:
        mot.remove(lettre)
        index = map.index([0,lettre])
        map[index][0] = 1
        if len(mot)==0:
            fonctions.printMot(map)
            print("Félicitation vous avez gagné !!")
            partie = False
            break
        print("bien joué la lettre '{}' y est bien, il ne vous reste que {} lettres à trouver et {} tentatives".format(lettre,len(mot),essais-i))
    else :
        print("loupé ! il ne vous reste que {} chances".format(essais-i))

print ("Votre nouveau score est {} \n A très bientot ^_^".format(score_joueur + essais - i))
io = open(file_path,"wb")
mon_pick = pickle.Pickler(io)
dictionnaire[nom_joueur]= score_joueur
mon_pick.dump(dictionnaire)
io.close()