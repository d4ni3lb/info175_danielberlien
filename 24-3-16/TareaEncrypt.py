import Tkinter
#Funciones encriptador

def encriptar():
    text = inputText.get("1.0",'end-1c') #Guardar texto del textBox
    saltos = saltosEntry.get() #Guardar numero de saltos de encriptacion cesar
    saltos = int(saltos)
    radioB = v.get() #Saber que radiobutton fue seleccionado

    if(radioB==1): #Encriptacion cenit-polar
        encriptado = []
        palabra = text
        palabra = palabra.lower()
        for x in range(0,len(palabra)):
                if(palabra[x] == "c"): encriptado.append("p")
                elif(palabra[x] == "e"): encriptado.append("o")
                elif(palabra[x] == "n"): encriptado.append("l")
                elif(palabra[x] == "i"): encriptado.append("a") 
                elif(palabra[x] == "t"): encriptado.append("r")
                elif(palabra[x] == "p"): encriptado.append("c") 
                elif(palabra[x] == "o"): encriptado.append("e") 
                elif(palabra[x] == "l"): encriptado.append("n") 
                elif(palabra[x] == "a"): encriptado.append("i")
                elif(palabra[x] == "r"): encriptado.append("t")
                else: encriptado.append(palabra[x])
        final = "".join(encriptado)
        labelEncrypt["text"] = final

    if(radioB==2): #Encriptacion cesar
        encriptada = ""
        palabra = text
        palabra = palabra.lower()
        for x in range(0,len(palabra)):
                temp= ord(palabra[x])
                if(temp > 96 and temp < 123):
                        if(temp+saltos < 123):
                                encriptada += chr(temp + saltos)
                        else:
                                encriptada += chr(temp + saltos - 26)
                else:
                        encriptada += chr(temp)

                
        labelEncrypt["text"] = encriptada


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
#Creado frame para organizar el label y el entry de los saltos de la encript cesar

label3 = Tkinter.Label(saltosFrame,anchor="w",height="2",text="Seleccione la cantidad de saltos para la encriptacion cesar: ")
label3.grid(row=0,column=0)

saltosEntry = Tkinter.Entry(saltosFrame,width="2")
saltosEntry.grid(row=0,column=1)


labelEncrypt = Tkinter.Label(mainWindow,anchor="center",pady="2",text="")
labelEncrypt.pack()

button = Tkinter.Button(mainWindow,command = encriptar,text="Encriptar")
button.pack()


mainWindow.mainloop()


