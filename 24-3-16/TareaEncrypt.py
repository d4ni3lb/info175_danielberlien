import Tkinter

#Funciones encriptador


#Interfaz grafica

mainWindow = Tkinter.Tk()
label1 = Tkinter.Label(mainWindow,anchor="center", height="3",text="Ingrese frase a encriptar: ")
label1.pack()

inputText = Tkinter.Text(mainWindow, height="6", width="70")
inputText.pack()

label2 = Tkinter.Label(mainWindow,anchor="nw",height="2",text="Seleccione el tipo de encriptacion: ")
label2.pack()

radioFrame = Tkinter.Frame(mainWindow) #Creado frame para organizar los radio buttons horizontalmente
radioFrame.pack()

v = Tkinter.IntVar()

rButton1 = Tkinter.Radiobutton(radioFrame, text = "Cenit-Polar",variable = v, value = 1)
rButton1.grid(row=0,column=0)

rButton2 = Tkinter.Radiobutton(radioFrame, text = "Cesar",variable = v, value = 2)
rButton2.grid(row=0,column=2)

saltosFrame = Tkinter.Frame(mainWindow)
saltosFrame.pack()

label3 = Tkinter.Label(saltosFrame,anchor="w",height="2",text="Seleccione la cantidad de saltos para la encriptacion cesar: ")
label3.grid(row=0,column=0)

saltosEntry = Tkinter.Entry(saltosFrame,width="2")
saltosEntry.grid(row=0,column=1)





mainWindow.mainloop()

def text_input():
    input = self.myText_Box.get("1.0",'end-1c')
