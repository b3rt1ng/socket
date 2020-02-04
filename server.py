from tkinter import *
import os


def ipfinder():
	return str(os.popen('ifconfig | grep -E "([0-9]{1,3}[\.]){3}[0-9]{1,3}"').readlines())[15:-100]


def multi():
	multijoueur = Tk()
	multijoueur.geometry("300x300")
	multijoueur.resizable(0,0)
	multijoueur.title("Multijoueur")
	try:
		pseudo
		existance_pseudo = 1
	except:
		existance_pseudo = 0
	if existance_pseudo == 0:
		pseudotexte = Label(multijoueur, text="vous n'avez pas de pseudo")
		pseudo = Entry(multijoueur, width=10)



	iptexte = Label(multijoueur, text="votre ip locale est: "+ipfinder())
	iptexte.pack()
	pseudo.pack()
	bouton_quitter = Button(multijoueur, text="Quitter", command=multijoueur.quit)
	bouton_quitter.pack()

	multijoueur.mainloop()

multi()

