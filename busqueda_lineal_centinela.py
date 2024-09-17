info = [5,8,4,7,1,8,25,98,7,32,14,65] #T(n) = 1
tamano = len(info) #T(n) = 1
a_buscar = 15 #T(n) = 1

def busqueda_centinela(data, size, elemento):
 
    centinela = data[size - 1] #T(n) = 1

    data[size - 1] = elemento #T(n) = 1
    i = 0 #T(n) = 1
 
    while (data[i] != elemento): #T(n) = n
        i += 1
 
    data[size - 1] = centinela #T(n) = 1
 
    if ((i < size - 1) or (data[size - 1] == elemento)): #T(n) = 1
        print(f"El elemento {elemento} está en la lista en posicion: ", i)
    else:
        print(f"El elemento {elemento} no se encuentra en la lista")


busqueda_centinela(info, tamano, a_buscar) #T(n) = 1
