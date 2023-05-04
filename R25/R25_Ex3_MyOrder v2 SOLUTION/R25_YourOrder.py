import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

import os
from PIL import ImageTk, Image   


window = tk.Tk()
ta_commande = "Ta commande: \n"
veut_smarin = tk.StringVar(value="0")
veut_poutine = tk.StringVar(value="0")
choix_smarin =  tk.StringVar(value="steak")
size_smarin =  tk.StringVar(value="10")
veut_pizza = tk.StringVar(value="0")
choix_pizza =  tk.StringVar(value="nature")
size_pizza =  tk.StringVar(value="7")
choix_poutine =  tk.StringVar(value="regulière")
prix_total = 0

def ajouter_smarin():
    prix=0
    veut_smarin = chk_smarin.get()
    size_smarin_val = size_smarin.get()
    choix_smarin_val = choix_smarin.get()
    if (veut_smarin=='1'):
        if( size_smarin_val == '10'):
            if (choix_smarin_val == 'steak'): prix=14.99
            if (choix_smarin_val == 'peperroni'): prix=14.99
            if (choix_smarin_val == 'duchef'): prix=15.99
        else:
            if (choix_smarin_val == 'steak'): prix=16.99
            if (choix_smarin_val == 'pepperoni'): prix=16.99
            if (choix_smarin_val == 'duchef'): prix=17.99            
        global ta_commande
        ta_commande+=f"Un sous-marin {choix_smarin_val} {size_smarin_val}po :\t{round(prix,2)}$\n"
        global prix_total
        prix_total += prix

               
def ajouter_pizza():
    prix=0
    veut_pizza = chk_pizza.get()
    size_pizza_val = size_pizza.get()
    choix_pizza_val = choix_pizza.get()
    if (veut_pizza=='1'):
        if( size_pizza_val == '7'):
            if (choix_pizza_val == 'nature'): prix=14.99
            if (choix_pizza_val == 'végétarienne'): prix=14.99
            if (choix_pizza_val == 'toute garnie'): prix=16.99
        else:
            if (choix_pizza_val == 'nature'): prix=16.99
            if (choix_pizza_val == 'végétarienne'): prix=16.99
            if (choix_pizza_val == 'toute garnie'): prix=18.99            
        global ta_commande
        ta_commande+=f"Une pizza {choix_pizza_val} {size_pizza_val}po :\t{prix}$\n"
        global prix_total
        prix_total += prix
        
def ajouter_poutine():
    prix=0
    veut_poutine = chk_poutine.get()
    choix_poutine_val = choix_pizza.get()
    if (veut_poutine=='1'):
            if (choix_poutine_val == 'régulière'): prix=10.99
            if (choix_poutine_val == 'italienne'): prix=12.99
            if (choix_poutine_val == 'du chef'): prix=14.99
            
    global ta_commande
    ta_commande+=f"Une poutine {choix_poutine_val}  :\t{prix}$\n"
    global prix_total
    prix_total += prix
               
def ajouter():
    ajouter_smarin()
    ajouter_pizza()
    ajouter_poutine()
    global ta_commande
    global prix_total
    displayBox.delete("0.0", tk.END)
    la_commande = f"{ta_commande} \n \t Pour un total de :  {prix_total}$"
    displayBox.insert("0.0", la_commande)

    
window.rowconfigure((0,1,2,3,4), weight=1, minsize=150)
window.columnconfigure((0,1), weight=1, minsize=75)
# external padding avec padx et pady appliqués sur le .grid()
# internal padding avec padx et pady appliqués sur les widgets dans le pack()
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
logo_image = ImageTk.PhotoImage(Image.open(os.path.join(image_path, "Logo.jpg")), size=(26, 26))
smarin_image = ImageTk.PhotoImage(Image.open(os.path.join(image_path, "sousmarin.jpg")), size=(16, 16))
pizza_image = ImageTk.PhotoImage(Image.open(os.path.join(image_path, "pizza.jpg")), size=(16, 16))
poutine_image = ImageTk.PhotoImage(Image.open(os.path.join(image_path, "poutine.jpg")), size=(16, 16))
lbl_logo  = tk.Label(master=window, image=logo_image)
lbl_logo.grid(row=0,column=0,columnspan=2)

########  FRAME SOUS-MARIN
frm_sousmarin = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
frm_sousmarin.grid(row=1, column=0, padx=5, pady=0)

frm_order_smarin = tk.Frame(
            master=frm_sousmarin,
            relief=tk.RAISED,
            borderwidth=1
        )
frm_order_smarin.grid(row=1, column=0, padx=5, pady=5)

chk_smarin = ctk.CTkCheckBox(master=frm_order_smarin, text='Oui! Un sous-marin!', 
	    variable=veut_smarin,
	    onvalue='1', offvalue='0')
chk_smarin.grid(row=0, column=0)

lbl_img_smarin  = tk.Label(master=frm_order_smarin, image=smarin_image, width="220", height="120")
lbl_img_smarin.grid(row=1, column=0 )

frm_smarin_choix = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
frm_smarin_choix.grid(row=1, column=1, padx=5, pady=5)

# Choix sous-marin
lbl_choixsmarin = ctk.CTkLabel(frm_smarin_choix,
										text="Choix")
lbl_choixsmarin.grid(row=0, column=0,sticky="w")

smarin_steak = ttk.Radiobutton(frm_smarin_choix, text='Steak', variable=choix_smarin, value='steak')
smarin_pepperoni = ttk.Radiobutton(frm_smarin_choix, text='Pepperoni', variable=choix_smarin, value='pepperoni')
smarin_duchef = ttk.Radiobutton(frm_smarin_choix, text='Du Chef', variable=choix_smarin, value='duchef')
smarin_steak.grid(row=1, column=0,padx=2,pady=2,sticky="w")
smarin_pepperoni.grid(row=2, column=0,padx=2,pady=2,sticky="w")
smarin_duchef.grid(row=3, column=0,padx=2,pady=2,sticky="w")
# Choix sous-marin grandeur
lbl_choixsmarin_size = ctk.CTkLabel(frm_smarin_choix,
										text="Grandeur")
lbl_choixsmarin_size.grid(row=4, column=0,sticky="w")

smarin10po = ttk.Radiobutton(frm_smarin_choix, text='10"', variable=size_smarin, value='10')
smarin14po = ttk.Radiobutton(frm_smarin_choix, text='14"', variable=size_smarin, value='14')
smarin10po.grid(row=5, column=0,padx=2,pady=2,sticky="w")
smarin14po.grid(row=6, column=0,padx=2,sticky="w")
# window.columnconfigure et window.rowconfigure pour que chaque frame s'ajuste à la grandeur de la fenêtre
btn_voirCommande = ttk.Button(frm_sousmarin, text="Ajouter", command=ajouter)
btn_voirCommande.grid(column=2, row=3, sticky='w') 


###########   FRAME PIZZA
frm_pizza = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
frm_pizza.grid(row=2, column=0, padx=5, pady=0)

frm_order_pizza = tk.Frame(
            master=frm_pizza,
            relief=tk.RAISED,
            borderwidth=1
        )
frm_order_pizza.grid(row=1, column=0, padx=5, pady=5)


chk_pizza = ctk.CTkCheckBox(master=frm_order_pizza, text='Oui! Une pizza!', 
	    variable=veut_pizza,
	    onvalue='1', offvalue='0')
chk_pizza.grid(row=0, column=0)

lbl_img_pizza  = tk.Label(master=frm_order_pizza, image=pizza_image, width="220", height="120")
lbl_img_pizza.grid(row=1, column=0 )

frm_pizza_choix = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
frm_pizza_choix.grid(row=2, column=1, padx=5, pady=5)

# Choix pizza
lbl_choixpizza = ctk.CTkLabel(frm_pizza_choix,
										text="Choix")
lbl_choixpizza.grid(row=0, column=0,sticky="w")

pizza_nature = ttk.Radiobutton(frm_pizza_choix, text='Nature', variable=choix_pizza, value='nature')
pizza_vege = ttk.Radiobutton(frm_pizza_choix, text='Végétarienne', variable=choix_pizza, value='végétarienne')
pizza_garnie = ttk.Radiobutton(frm_pizza_choix, text='Toute garnie', variable=choix_pizza, value='toute garnie')
pizza_nature.grid(row=1, column=0,padx=2,pady=2,sticky="w")
pizza_vege.grid(row=2, column=0,padx=2,pady=2,sticky="w")
pizza_garnie.grid(row=3, column=0,padx=2,pady=2,sticky="w")
# Choix grandeur pizza
lbl_choixpizza_size = ctk.CTkLabel(frm_pizza_choix,
										text="Grandeur")
lbl_choixpizza_size.grid(row=4, column=0,sticky="w")

pizza7po = ttk.Radiobutton(frm_pizza_choix, text='7"', variable=size_pizza, value='7')
pizza14po = ttk.Radiobutton(frm_pizza_choix, text='14"', variable=size_pizza, value='14')
pizza7po.grid(row=5, column=0,padx=2,pady=2,sticky="w")
pizza14po.grid(row=6, column=0,padx=2,sticky="w")
# window.columnconfigure et window.rowconfigure pour que chaque frame s'ajuste à la grandeur de la fenêtre
btn_voirCommande = ttk.Button(frm_pizza, text="Ajouter", command=ajouter)
btn_voirCommande.grid(column=2, row=3, sticky='w') 

########  FRAME POUTINE
frm_poutine = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
frm_poutine.grid(row=3, column=0, padx=5, pady=0)

frm_order_poutine = tk.Frame(
            master=frm_poutine,
            relief=tk.RAISED,
            borderwidth=1
        )
frm_order_poutine.grid(row=0, column=0, padx=5, pady=5)

chk_poutine = ctk.CTkCheckBox(master=frm_order_smarin, text='Oui! Une poutine!', 
	    variable=veut_poutine,
	    onvalue='1', offvalue='0')
chk_poutine.grid(row=0, column=0)

lbl_img_poutine  = tk.Label(master=frm_order_poutine, image=poutine_image, width="220", height="120")
lbl_img_poutine.grid(row=1, column=0 )

frm_poutine_choix = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
frm_poutine_choix.grid(row=1, column=1, padx=5, pady=5)

# Choix poutine
lbl_choixpoutine = ctk.CTkLabel(frm_poutine_choix,
										text="Choix")
lbl_choixpoutine.grid(row=0, column=0,sticky="w")

poutine_reg = ttk.Radiobutton(frm_smarin_choix, text='Régulière', variable=choix_smarin, value='reguliere')
poutine_italienne = ttk.Radiobutton(frm_smarin_choix, text='Italienne', variable=choix_smarin, value='italienne')
poutine_duchef = ttk.Radiobutton(frm_smarin_choix, text='Du Chef', variable=choix_smarin, value='duchef')
poutine_reg.grid(row=1, column=0,padx=2,pady=2,sticky="w")
poutine_italienne.grid(row=2, column=0,padx=2,pady=2,sticky="w")
poutine_duchef.grid(row=3, column=0,padx=2,pady=2,sticky="w")

# window.columnconfigure et window.rowconfigure pour que chaque frame s'ajuste à la grandeur de la fenêtre
btn_voirCommande = ttk.Button(frm_sousmarin, text="Ajouter", command=ajouter)
btn_voirCommande.grid(column=2, row=3, sticky='w') 

##   FRAME VOIR LA COMMANDE
frm_voirCommande = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
frm_voirCommande.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
# Text Box
displayBox = ctk.CTkTextbox(frm_voirCommande,
                                width=400,
                                height=200, border_width=2)
displayBox.grid(row=1, column=0, sticky="nsew", pady=0)


window.mainloop()