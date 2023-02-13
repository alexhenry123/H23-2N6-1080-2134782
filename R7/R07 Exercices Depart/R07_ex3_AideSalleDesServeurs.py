# Q1 A  Faites une fonction qui va demander de l'aide à un ami pour installer un équipement dans la salle des serveurs
#       La fonction prendra en paramètre le prénom de l'ami et l'équipement à installer
nom = ""
raison_demande = ""
équipement_commandé = ""
def demande_aide_info(nom, raison_demande, équipement):
    print(f"""Salut {nom},
Il faudrait {raison_demande}. J'ai enfin reçu les {équipement} que j'ai commandé.""")    
    
# Q1 B  Faites l'appel de cette fonction, de façon à imprimer le message suivant: 
#                          Salut Marc, 
#                               Il faudrait changer la configuration de la salle de serveur. J'ai enfin reçu les Rack nvent Shroff que j'ai commandé.
demande_aide_info("Marc", "changer la configuration de la salle de serveurs", "Rack nvent Shroff")

# Q1 B  Faites l'appel de cette fonction, de façon à imprimer le message suivant: 
#                          Salut Pierre, 
#                               Il faudrait changer la configuration de la salle de serveur. J'ai enfin reçu les commutateurs que j'ai commandé.
demande_aide_info("Pierre", "changer la configuration de la salle de serveurs", "commutateurs")