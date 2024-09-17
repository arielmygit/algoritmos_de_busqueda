info = [1, 3, 5, 7, 9, 11, 14, 16, 17, 20, 25, 30, 33]
a_encontrar = 25 # T(n) = 1
begin = 0 # T(n) = 1

def busqueda_binaria(data, elemento, inicio, final):
    if inicio > final: # T(n) = 1
        return False

    medio = (inicio + final) // 2 # T(n) = log n

    if data[medio] == elemento: # T(n) = 1
        return True
    elif data[medio] < elemento: 
        return busqueda_binaria(data, elemento, medio + 1, final)
    else: 
        return busqueda_binaria(data, elemento, inicio, medio - 1)

res = print(busqueda_binaria(info, a_encontrar, begin, len(info) - 1)) # T(n) = 1
# O(1+1+log n+1+1) = 4 +log n
# O = log n
