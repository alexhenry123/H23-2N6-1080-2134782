# Cet exercice est un retour sur les fonctions (notion vue en programmation 1)

# Q1 A:  Définir une fonction sans paramètre                                    #
#        Faites une fonction qui va imprimer "Bonjour" 
#        Appelez-la bonjour
def bonjour():
    print("Bonjour")

# Q1 B:   Appel de la fonction 
bonjour()

# Q2 A:   Définir une fonction avec paramètre
#         Faites une fonction qui va imprimer "Bonjour XXXXXX" où XXXXXX est le nom passé en paramètre lors de l'appel de cette fonction
#         Appelez-la bonjour_toi
def bonjour_toi(ami):
    print(ami)

# Q2 B:  Appel de la fonction bonjour_toi avec en paramètre le nom de mon ami Pierre
bonjour_toi("Pierre")

# Q2 C:  Appel de la fonction bonjour_toi avec en paramètre le nom de mon amie Sylvie
bonjour_toi("Sylvie")

# Q3 A:  Définir une fonction sans paramètre mais qui va retourner une valeur de retour      #
#        Faites une fonction qui va imprimer "Bonjour" et qui va retourner le message "Cela va?"
#        Appelez-la cela_va
def cela_va():
    print("Bonjour")
    return "Cela va?"

# Q3 B:   Appel de la fonction et capture de la réponse
cela_va()

# Q4 A:  Définir une fonction avec paramètre et avec une valeur de retour      #
#        Faites une fonction qui va imprimer "Bonjour XXXXXX" où XXXXXX est le nom passé en paramètre lors de l'appel de cette fonction"
# 		 et qui va retourner le message "Je suis libre ce soir, et toi?"
#        Appelez-la cela_va_bien
def cela_va_bien(nom):
    print(f"""Bonjour {nom},
Je suis libre ce soir, et toi?""")

# Q4 B:   Appel de la fonction et capture de la réponse
cela_va_bien("Boris")