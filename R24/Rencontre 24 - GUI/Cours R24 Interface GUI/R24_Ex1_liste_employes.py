import customtkinter

class MyFrameAfficher(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure((0,1), weight=1)  # configure grid system
        self.grid_columnconfigure((0,1,2), weight=1)
        
        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self, text="Employe Courant")
        self.label.grid(row=0, column=1, padx=5, pady=5)
        
        self.btn_precedent = customtkinter.CTkButton(master=self, text="Précédent",command=self.aller_au_precedent, font = ("inter",14))
        self.btn_precedent.grid(row=1, column=0, padx=5, pady=5)
        
        self.nom = customtkinter.CTkEntry(master=self,  font = ("inter",14),width=300)
        self.nom.grid(row=1, column=1, padx=5, pady=5)
        self.nom.insert(0,ls_employes[0])
        
        self.btn_suivant = customtkinter.CTkButton(master=self, text="Suivant",command=self.aller_au_suivant, font = ("inter",14))
        self.btn_suivant.grid(row=1, column=2, padx=5, pady=5)
        
    def aller_au_precedent(self):
        global index_courant
        if index_courant == 0:
            index_courant = len(ls_employes)-1
        else:
            index_courant -= 1
        texte_courant_nom = self.nom.get()
        self.nom.delete(0,len(texte_courant_nom))
        self.nom.insert(0,ls_employes[index_courant])
        
    def aller_au_suivant(self):
        global index_courant
        if index_courant == len(ls_employes)-1:
            index_courant = 0
        else:
            index_courant += 1
        text_courant_nom = self.nom.get()
        self.nom.delete(0,len(text_courant_nom))
        self.nom.insert(0,ls_employes[index_courant])
        
class MyFrameModifier(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure((0,1,2,3), weight=1)  # configure grid system
        self.grid_columnconfigure((0,1,2), weight=1)
        
        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(master=self, text="Ajouter/Enlever un employé")
        self.label.grid(row=0, column=1, padx=5, pady=5)
       
        self.btn_ajouter = customtkinter.CTkButton(master=self, text="Ajouter", command=self.ajouter, font = ("inter",14))
        self.btn_ajouter.grid(row=1, column=1, padx=5, pady=5)
        
        self.nouveau_nom = customtkinter.CTkEntry(master=self, placeholder_text="Entrez un nom d'employé",width=400,font = ("inter",14),  )
        self.nouveau_nom.grid(row=2, column=1, padx=5, pady=5, columnspan=1, sticky="nsew")  
        
        self.avertissement = customtkinter.CTkLabel(master=self, text=" ", width=180,font = ("inter",14),state="disabled",command=self.enlever )
        self.avertissement.grid(row=3, column=1, padx=5, pady=5)
        
        self.btn_enlever = customtkinter.CTkButton(master=self, text="Enlever",command=self.enlever, font = ("inter",14))
        self.btn_enlever.grid(row=4, column=1, padx=5, pady=5)     
    
    def ajouter(self):
        try:
            if len(self.nouveau_nom.get()) > 2:
                for employe in ls_employes:
                    if employe == self.nouveau_nom:
                        self.avertissement.configure(f"Le nom '{self.nouveau_nom.get()}' est déjà dans la liste d'employés. Veuillez choisir un autre nom.")
                    else:
                        ls_employes.append(self.nouveau_nom.get())
                        return f"Le nom '{self.nouveau_nom.get()}' a été ajouté."
            else:
                self.avertissement.configure(f"Le nom '{self.nouveau_nom.get()}' est un nom invalide car il n'est pas assez long.")
        except:
            self.avertissement.configure(f"Le nom entré doit être un string.")
     
    def enlever(self):
        try:
            if len(self.nouveau_nom.get()) > 2:
                for employe in ls_employes:
                    if employe != self.nouveau_nom:
                        self.avertissement.configure(f"Le nom '{self.nouveau_nom.get()}' n'est pas dans la liste d'employés. Veuillez choisir un nom présent dans la liste d'employés.")
                    else:
                        ls_employes.remove(self.nouveau_nom.get())
                        return f"Le nom '{self.nouveau_nom.get()}' a été retiré."
            else:
                return self.avertissement.configure(f"Le nom '{self.nouveau_nom.get()}' est un nom invalide car il n'est pas assez long.")
        except:
            self.avertissement.configure(f"Le nom entré doit être un string.")
            
class App(customtkinter.CTk):
    global ls_employes
    ls_employes = ['Pierre-Paul Gallant', 'Maxime Pelletier']
    global index_courant
    index_courant = 0
         
    def __init__(self):
        super().__init__()
        self.geometry("450x300")
        self.title="Liste des employés"
        self.resizable(False, False)   #On ne peut pas changer la grandeur de la fenêtre
        self.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)  # configure grid system
        self.grid_columnconfigure((0,1,2,3), weight=1)
        
        self.pour_afficher = MyFrameAfficher(master=self,width=600, corner_radius=0)
        self.pour_afficher.grid(row=0, column=0, padx=2, pady=2)
        
        self.pour_modifier = MyFrameModifier(master=self,width=600, corner_radius=0)
        self.pour_modifier.grid(row=6, column=0, padx=30, pady=2)
        
app = App()

app.mainloop()
