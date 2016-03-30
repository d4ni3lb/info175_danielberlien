

def encrypt(n):
        encriptada = ""
        palabra = raw_input("Ingrese la frase a encriptar: ")
        palabra = palabra.lower()
        for x in range(0,len(palabra)):
                temp= ord(palabra[x])
                if(temp > 96 and temp < 123):
                        print("1.5")
                        if(temp+n < 123):
                                encriptada += chr(temp + n)
                                print ("2")
                        else:
                                encriptada += chr(temp + n - 26)
                                print ("3")
                else:
                        encriptada += chr(temp)

                
        print encriptada


        
if __name__ == "__main__":
        n = input("Ingrese el numero de posiciones que se desea mover cada caracter: ")
        encrypt(n)
