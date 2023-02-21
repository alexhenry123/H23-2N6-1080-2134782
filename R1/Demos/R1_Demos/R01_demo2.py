# Assigner des valeurs aux variables afin qu'elles soient du type désiré, la changer si nécessaire.

variable_int = 32
variable_float = 32.5      # initialiser avec une valeur float
variable_boolean = True    # initialiser avec une valeur boolean
variable_string = "eeee"     # initialiser avec un string

variable_list = [2,8,7,6]       # initialiser avec une liste
variable_dictionnaire = {"deux"}   # initialiser avec une pair clef-valeur afin d'avoir un dictionnaire

print(f"""\n \n Les types des variables sont : 
        variable_int est : {type(variable_int)}
        variable_float est : {type(variable_float)}
        variable_boolean est : {type(variable_boolean)}
        variable_string est : {type(variable_string)}
        variable_list est : {type(variable_list)}
        variable_dictionnaire est : {type(variable_dictionnaire)}
        """)
        