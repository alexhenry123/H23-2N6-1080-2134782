import os
# placement du terminal dans le répertoire où se trouve ce script.
chemin = os.path.dirname(__file__)
os.chdir(chemin)
if os.path.exists("demo6.txt"): os.remove("demo6.txt")  # supprime fichier demo6.txt créé par le script
if os.path.exists("test.txt"): os.remove("test.txt")    # supprime fichier test.txt créé par le script



with open("test.txt","w") as file: 
    pass

os.system("cls")
# renommer un fichier ou un dossier #
os.rename('test.txt', 'demo6.txt')
print(f'Liste des répertoires et fichiers est : {os.listdir()}')
print(80*"_")

# différentes fonctions du sous-module path. Le fichier dem
print(os.path.basename(f'{chemin}/demo6.txt'))  # 'demo6.txt'
print(os.path.dirname(f'{chemin}/demo6.txt'))   # 'c:\\Users\\......\\R04_demo'
print(os.path.split(f'{chemin}/demo6.txt'))     # ('c:\\Users\\......\\R04_demo', 'demo6.txt')
print(os.path.exists(f'{chemin}/demo6.txt'))    # True
print(os.path.isfile(f'{chemin}/demo6.txt'))    # True
print(os.path.isdir(f'{chemin}/demo6.txt'))     # False
print(os.path.splitext(f'{chemin}/demo6.txt'))  #('c:\\Users\\......\\R04_demo', '.txt')#

