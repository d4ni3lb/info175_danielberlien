import Tkinter
#Funciones encriptador
textoMostrado=""
def encriptar():
    text = inputText.get("1.0",'end-1c')
    radioB = v.get()
    if(radioB==1):
        print "caca polar"
    if(radioB==2):
        encriptada = ""
        palabra = text
        palabra = palabra.lower()
        for x in range(0,len(palabra)):
                temp= ord(palabra[x])
                if(temp > 96 and temp < 123):
                        if(temp+n < 123):
                                encriptada += chr(temp + n)
                        else:
                                encriptada += chr(temp + n - 26)
                else:
                        encriptada += chr(temp)

                
        textoMostrado.set(encriptada)

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

labelEncrypt = Tkinter.Label(mainWindow,anchor="center",pady="2",text=textoMostrado)
labelEncrypt.pack()

button = Tkinter.Button(mainWindow,command = encriptar)
button.pack()


mainWindow.mainloop()


