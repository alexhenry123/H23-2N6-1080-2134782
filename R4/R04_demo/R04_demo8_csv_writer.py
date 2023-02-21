import csv
#Nous avons une liste d'étudiants. 
liste_etudiants = [ ["Anna",543564,"420-INFO"],
                    ["Greg",987123,"420-INFO"],
                    ["Bob",369852,"238-FRAN"],
                    ["Joseph",753869,"135-PHYS"],
                    ["Hubert",125478,"238-FRAN"],
                    ["Zeus",659327,"135-PHYS"],
                    ["Joel",583649,"420-INFO"] ]


# Nous voulons écrire un fichier csv contenant les id en premier, suivi des noms et sans les départements

with open("etudiants_ids.csv") as fichier_csv :
    csv_writer = csv.writer(fichier_csv)
    csv_writer.writerow(["ID","nom"])
    for etudiant in liste_etudiants:
        csv_writer.writerow(etudiant[1],etudiant[0])

help (csv_writer.writerow)