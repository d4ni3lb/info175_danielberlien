import Tkinter

mainWindow = Tkinter.Tk()
label1 = Tkinter.Label(mainWindow,anchor="center",text="Ingrese frase a encriptar: ")
label1.pack()

inputText = Tkinter.Text(mainWindow)
inputText.pack()







mainWindow.mainloop()

def text_input():
    input = self.myText_Box.get("1.0",'end-1c')
