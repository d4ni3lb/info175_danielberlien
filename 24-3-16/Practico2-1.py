lista = []
n = input("Ingrese el largo de la lista: ")
for i in range(0,n):
	if(i%3==0) & (i%7==0):
		lista.append(i)
print lista
