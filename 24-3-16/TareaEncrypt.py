import Tkinter

#Funciones encriptador
cenit = False
def sel(i):
	if i == 1:
		cenit = False
		print ("Cenit falso")
	else:
		cenit = True
		print ("cenit verd")




#Interfaz grafica

mainWindow = Tkinter.Tk()
label1 = Tkinter.Label(mainWindow,anchor="center", height="3",text="Ingrese frase a encriptar: ")
label1.pack()

inputText = Tkinter.Text(mainWindow, height="6", width="70")
inputText.pack()

label2 = Tkinter.Label(mainWindow,anchor="nw",height="2",text="Seleccione el tipo de encriptacion: ")
label2.pack()


rButton1 = Tkinter.Radiobutton(mainWindow, text = "Cenit-Polar",command=sel(2))
rButton1.pack()







mainWindow.mainloop()

def text_input():
    input = self.myText_Box.get("1.0",'end-1c')
