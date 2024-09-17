def busqueda_lineal(data, a_buscar):
    n = len(data) # T(n) = 1
    i= 0        # T(n) = 1
    while i<n and data[i]!=a_buscar: # T(n) = n
        i = i+1 
    if i==n: # T(n) = 1
        return -1 
    else:
        return i 

arr = [1,3,4,5,2,0,3,9,20] # T(n) = 1
x= 0                       # T(n) = 1
r = busqueda_lineal(arr,x) # T(n) = 1

if r == -1: # T(n) = 1
    print(f"El elemento {x} no está en la lista.") 
else:
    print(f"El elemento {x} se encuentra en el índice {r}.")

#O(1+1+1+n+1+1+1+1) = 6+n
#O = n
