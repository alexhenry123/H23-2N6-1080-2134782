# Programme pour créer un 
# GUI avec le module customtkinter 


import customtkinter as ctk         #pip install customtkinter
import csv
import os
from PIL import ImageTk, Image      #pip install pillow
# pour l'apparence de la fenêtre  (choix Light, Dark, System)
ctk.set_appearance_mode('Dark')

os.chdir(os.path.dirname(__file__))   # Pour se positionner dans le répertoire de ce script
# pour l'apparence des composants graphiques dans la fenêtre
# choix possibles: green, dark-blue, blue
ctk.set_default_color_theme('green')

# Dimensions de la fenêtre
ChoixWidth, ChoixHeight = 900, 740

ls_stages =  []
def remplir_ls_stages():
    with open('reseau.csv','r',encoding='utf-8') as data_CSV:
        csv_data = csv.reader(data_CSV,delimiter=';')
        for line in csv_data:
            ls_stages.append(f"{line[0]} {line[1]}") 
           

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")


# Choix Class
class Choix(ctk.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.img_logo = ctk.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size = (900, 120))

        self.img_REZO_H23_1= ctk.CTkImage(Image.open(os.path.join(image_path, "REZO_H23_1.png")), size = (700, 500))
        self.img_REZO_H23_2= ctk.CTkImage(Image.open(os.path.join(image_path, "REZO_H23_2.png")), size = (700, 500))
        self.img_REZO_H23_3= ctk.CTkImage(Image.open(os.path.join(image_path, "REZO_H23_3.png")), size = (700, 500))
        self.img_REZO_H23_4 = ctk.CTkImage(Image.open(os.path.join(image_path, "REZO_H23_4.png")), size = (700, 500))
        self.img_REZO_H23_5 = ctk.CTkImage(Image.open(os.path.join(image_path, "REZO_H23_5.png")), size = (700, 500))
        self.img_REZO_H23_6 = ctk.CTkImage(Image.open(os.path.join(image_path, "REZO_H23_6.png")), size = (700, 500))
        self.img_REZO_H23_7 = ctk.CTkImage(Image.open(os.path.join(image_path, "REZO_H23_7.png")), size = (700, 500))
        self.img_REZO_H23_8 = ctk.CTkImage(Image.open(os.path.join(image_path, "REZO_H23_8.png")), size = (700, 500))        

        self.dc_images = {"REZO_H23_1": self.img_REZO_H23_1,
                          "REZO_H23_2": self.img_REZO_H23_2,
                          "REZO_H23_3": self.img_REZO_H23_3,
                          "REZO_H23_4": self.img_REZO_H23_4,
                          "REZO_H23_5": self.img_REZO_H23_5,
                          "REZO_H23_6": self.img_REZO_H23_6,
                          "REZO_H23_7": self.img_REZO_H23_7,
                          "REZO_H23_8": self.img_REZO_H23_8}


        # titre de la fenêtre
        self.title("Fais tes 3 choix")
        self.geometry(f"{ChoixWidth}x{ChoixHeight}")
        #self.grid_rowconfigure((0,1,2,3,4), weight=1) 
        self.grid_columnconfigure((0), weight=1)
        self.grid_columnconfigure((1), weight=4)        
        # CTkLabel pour logo
        self.lbl_logo  = ctk.CTkLabel(self, image=self.img_logo, text="")
        self.lbl_logo.grid(row=0,column=0,columnspan=2, sticky="ew")
        
        ########  FRAME CHOIX CONTENU
        self.frm_contenu = ctk.CTkFrame(
            master=self,
            width=700
        )
        self.frm_contenu.grid( row=1, column=0, padx=5, pady=0,columnspan=2,sticky="nsew")
        ########  FRAME CHOIX STAGES
        self.frm_choix_stage = ctk.CTkFrame(
            master=self.frm_contenu,
            width=600
        )
        self.frm_choix_stage.grid( row=1, column=0, padx=0, pady=0,sticky="ns")
        #self.frm_choix_stage.propagate(1)
        # CTkOptionMenu  pour les choix de stage
        self.choix_1 = ctk.CTkOptionMenu(master=self.frm_choix_stage,
                                        values=['PREMIER CHOIX']+ls_stages,width=350,
                                    height=25,command=self.voir_details)
        self.choix_1.grid(row=0, column=0,
                                    padx=(0,0), pady=(0,5),
                                    sticky="e")
        self.choix_1.set("REZO_H23_1 Groupe SL")
        
                # CTkOptionMenu  pour les choix de stage
        self.choix_2 = ctk.CTkOptionMenu(master=self.frm_choix_stage,
                                    values=['DEUXIÈME CHOIX']+ls_stages,width=350,
                                    height=25,command=self.voir_details)
        self.choix_2.grid(row=1, column=0,
                                    padx=(0,0), pady=(0,5),
                                    sticky="e")
        
                # CTkOptionMenu  pour les choix de stage
        self.choix_3 = ctk.CTkOptionMenu(master=self.frm_choix_stage,
                                    values=['TROISIÈME CHOIX']+ls_stages,width=350,
                                    height=25,command=self.voir_details)
        
        self.choix_3.grid(row=2, column=0,
                                    padx=(0,0), pady=(0,5),
                                    sticky="e")
        

                
        ########  FRAME DÉTAILS
        self.frm_details = ctk.CTkFrame(
            master=self.frm_contenu,
            width=800
        )
        self.frm_details.grid( row=1, column=1, padx=0, pady=0)
        
        # CTkLabel pour les détails
        self.lbl_details  = ctk.CTkLabel(master=self.frm_details, image=self.img_REZO_H23_1)
        self.lbl_details.grid(row=0,column=0)
        
                # Entry pour le matricule
        self.matricule = ctk.CTkEntry(master=self,
                        placeholder_text="Entrez votre matricule", text_color='red')
        self.matricule.grid(row=3, column=0,
                            columnspan=2, sticky="ew")
        
        # CTkButton enregistrer_choix_etudiant
        self.btn_enregistrer_choix = ctk.CTkButton(master=self,
                                        text="Enregistrer tes choix",
                                        command=self.enregistrer_choix,width=300,
                                height=25)
        self.btn_enregistrer_choix.grid(row=4, column=0,columnspan=2,
                                        padx=5,
                                        pady=(5,5)) 
        
                # CTkLabel pour messages
        self.lbl_message = ctk.CTkLabel(self,
                                    text="Fais tes choix",width=200,
                               height=25)
        self.lbl_message.grid(row=5, column=0,columnspan=2,
                                padx=5,pady=(0,5))  #enlevé sticky="ew"
         
        
    def voir_details(self, choix):
        image_splitee = choix.split(' ')
        valeur = self.dc_images[image_splitee[0]]
        self.lbl_details.configure(image=valeur)

        
    # Pour enregistrer les choix dans un fichier
    def enregistrer_choix(self):
        # À FAIRE. Voir document Word.
        # Utiliser la méthode .get() pour obtenir la valeur des choix et du matricule.
        # Commencez par faire UNE vérification et le message qui s'affiche dans lbl_message si cela ne marche pas.
        # Une fois que vous avez ayé lancer le programme et qu'il a le comportement attendu, passez à la prochaine vérification.
        pass


if __name__ == "__main__":
    remplir_ls_stages()
    Choix = Choix()
    Choix.mainloop()    
