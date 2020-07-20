#IMPORTATTION DES LIBRAIRIES

import re
import xlwt
from xlwt import Workbook
from tkinter import *
from PIL import ImageTk, Image
import os
import time

numero=""
wb = Workbook()
fenetre = Tk()

#FENETRE (CONFIG)
couleur_fond = "Blue"
couleur = "White"

fenetre.geometry("600x500")
fenetre.minsize(width = "600", height = "500")
fenetre.title("App by Berachem")
fenetre.configure(bg=couleur_fond)
fenetre.iconbitmap("C:/Users/berac/Desktop/Python app bdd telephone/database.ico")

historique_affiché = False
nombre_de_clique_sur_historique = 0

"""                     AMELIORATION DU DESIGN A FAIRE (Images, ....)

# Image téléphone

img = Image.open("C:/Users/berac/Desktop/numéro tel dans bdd tkinter/call.png")
panel = Label(fenetre, image = img)
panel.pack(side = "Right", fill = "both", expand = "yes")
"""
 #FICHIER

sheet1 = wb.add_sheet('numéros', cell_overwrite_ok=True)
sheet1.write(0, 0, "MOBILE")
sheet1.write(0, 1, "FIXE")

# FONCTION QUI ECRIT DANS LE FICHIER EXCEL
ligne_excel_fixe = 1
ligne_excel_mobile = 1
liste_numero_conforme = []
liste_numero_non_conforme = []


def check(numero, nom_fichier):
    global ligne_excel_fixe
    global ligne_excel_mobile
    global liste_numero_conforme
    global liste_numero_non_conforme

    expression = r"^0[0-9]([ .-]?[0-9]{2}){4}$"
    
    numero_texte = numero.get()

    if len(nom_fichier.get()) == 0 :
        information["foreground"] = "Red"
        information["text"] = "Vous n'avez pas entré de nom de fichier, veuillez en entrer un !"
        fenetre.after(5000, cacher_le_text_information, information)

    else:
        #Numero conforme ?????
        if re.search(expression,numero_texte) is not None and numero_texte not in liste_numero_conforme :
            

            #Numero mobile ???
            if list(numero_texte)[1]=="6" or list(numero_texte)[1]=="7":
                ligne_excel_mobile +=1
                sheet1.write(ligne_excel_mobile, 0, numero_texte)
                liste_numero_conforme.append(numero_texte)
                wb.save(nom_fichier.get() + ".xls")
                print("Le numéro a été enregistré")
                information["foreground"] = "Green"
                information["text"] = f"Parfait ! Le numéro {numero.get()} a été ajouté au fichier :)"
                fenetre.after(5000, cacher_le_text_information, information)

            #Numero fixe ???
            elif list(numero_texte)[1]=="1":
                ligne_excel_fixe +=1
                sheet1.write(ligne_excel_fixe, 1, numero_texte)
                liste_numero_conforme.append(numero_texte)
                wb.save(nom_fichier.get() + ".xls")
                print("Le numéro a été enregistré")
                information["foreground"] = "Green"
                information["text"] = f"Parfait ! Le numéro {numero.get()} a été ajouté au fichier :)"
                fenetre.after(5000, cacher_le_text_information, information)

            #Numero non conforme
            else : 
                liste_numero_non_conforme.append(numero_texte)
                print("Désolé mais le numéro n'est pas un 06, 07 ou 01")
                information["foreground"] = "Red"
                information["text"] = "Vous n'avez pas entré un numéro conforme :( !"
                fenetre.after(5000, cacher_le_text_information, information)

        #Numero non conforme
        else :
            liste_numero_non_conforme.append(numero_texte)
            print("Le numero n'est pas conforme")
            information["foreground"] = "Red"
            information["text"] = "Vous n'avez pas entré un numéro conforme :( !"
            fenetre.after(5000, cacher_le_text_information, information)
        

    numero.delete(0, END)


def cacher_le_text_information(label):
    label["text"] =""
    


# MODULES TKINTER
titre = Label(fenetre, text = "Bienvenue sur une application créée par Berachem et qui permet\n de lister dans un fichier excel les numéros de téléphones\n (Fixes ou Mobiles) que vous entrez",background=couleur_fond,foreground=couleur, font = "Nexabold")
titre.pack(pady = 30)

text = Label(fenetre,background=couleur_fond, text = "Nom à donner au fichier 📁 (.xls)", foreground=couleur, font = "Nexabold")
text.pack(pady = 9)

nom_fichier = Entry(fenetre, background=couleur_fond, foreground=couleur, width = 35,font = "Nexabold", bd = 2)
nom_fichier.pack(pady = 5)

txt = Label(fenetre,background=couleur_fond, text = "Veuillez entrer le numéro de téléphone 📞", foreground=couleur, font = "Nexabold")
txt.pack(pady = 9)

numero = Entry(fenetre, background=couleur_fond, foreground=couleur, width = 35,font = "Nexabold", bd = 2)
numero.pack(pady = 5)

information = Label(fenetre,background = couleur_fond, foreground ="Red", font = "Nexabold")
information.pack()

boutton = Button(fenetre, text="Ajouter le numéro ➕", command = lambda : check(numero, nom_fichier), background=couleur_fond,foreground=couleur, font = "Nexabold", borderwidth = 2)
boutton.pack(pady = 1)

# MAINTIEN DE LA FENETRE A L'INFINI

fenetre.mainloop()