

# créé et écrit dans un fichier
fichier = open("demo5.txt","w",encoding="utf-8")
fichier.write("Fichier données\n")
fichier.write("738 ordinateurs dans le réseau\n")


# La lecture ne marche pas ? D'où vien cette erreur ?
fichier_lu = open("demo5.txt","r",encoding="utf-8")
print(fichier_lu.readline(), end="")
print(fichier_lu.readline(), end="")



#Les mêmes instructions mais avec l'instruction with
with open("demo5-b.txt","w",encoding="utf-8") as fichier2:
    fichier2.write("Fichier données\n")
    fichier2.write("738 ordinateurs dans le réseau\n")
    
    
with open("demo5.txt","r",encoding="utf-8") as fichier_lu2:
    print(fichier_lu2.readline(), end="")
    print(fichier_lu2.readline(), end="")
#Ces instructions fonctionnent, pourquoi ?