

def cenitpolar():
        encriptado = []
        palabra = raw_input("Ingrese la frase a encriptar con cenit-polar: ")
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
        print final

        
if __name__ == "__main__":
        cenitpolar()
