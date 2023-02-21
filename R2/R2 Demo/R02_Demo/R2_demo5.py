#execution de lignes spécifiques

while True:
    print("Boucle infinie")

cartes_graphiques_en_stock = ['GeForce RTX 3070Ti', 
                              'Radeon RX 6950 XT', 
                              'Radeon RX 6900 XT']
for carte in cartes_graphiques_en_stock:
    print(f"La {carte} est disponnible en magasin.")


while True:
    print("Boucle infinie")

cartes_graphiques_rupture_de_stock = ['GeForce GTX 750Ti']
carte_en_rupture = cartes_graphiques_en_stock.pop()
cartes_graphiques_rupture_de_stock.append(carte_en_rupture)
print(f"La {carte_en_rupture} n'est pas disponnible en magasin pour l'instant.")

