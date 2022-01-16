import numpy as np

# paginas = np.array([1, 2, 3, 4, 1, 2, 5, 6, 1, 3, 1, 2, 5], dtype=int)
# nroMarcos = 5

# paginas = np.array([1, 2, 3, 2, 4, 1, 4, 2, 3, 6, 3, 2, 1, 4, 3], dtype=int)
# nroMarcos = 3

paginas = np.array([0,2,1,3,1,3,0,2], dtype=int)
nroMarcos = 4

def FIFO():
    tabla = np.zeros((nroMarcos, len(paginas)), dtype=int)
    tabla[:,:] = -1

    fallosPagina = np.zeros(len(paginas), dtype=str)
    fallosPagina[:] = "_"
    for i, pag in enumerate(paginas):
        if i == 0:
            tabla[0, 0] = pag
            fallosPagina[0] = "X"
        elif pag in tabla[:, i - 1]:
            tabla[:, i] = tabla[:, i - 1].copy()
        else:
            aux = np.append(np.array([pag]), tabla[:, i - 1].copy())
            tabla[:, i] = aux[:-1].copy()
            fallosPagina[i] = "X"
    print("\nFIFO\n", paginas)
    print(tabla)
    print(fallosPagina)
    print("Cantidad de fallos de pagina:", np.sum(fallosPagina == "X"))

def LRU():
    tabla = np.zeros((nroMarcos, len(paginas)), dtype=int)
    tabla[:,:] = -1

    fallosPagina = np.zeros(len(paginas), dtype=str)
    fallosPagina[:] = "_"
    for i, pag in enumerate(paginas):
        if i == 0:
            tabla[0, 0] = pag
            fallosPagina[0] = "X"
        elif pag in tabla[:, i - 1]:
            aux = np.delete(tabla[:, i - 1], np.where(tabla[:, i - 1] == pag)[0])
            tabla[:, i] = np.append(np.array([pag]), aux.copy())
        else:
            aux = np.append(np.array([pag]), tabla[:, i - 1].copy())
            tabla[:, i] = aux[:-1].copy()
            fallosPagina[i] = "X"
    print("\nLRU\n", paginas)
    print(tabla)
    print(fallosPagina)
    print("Cantidad de fallos de pagina:", np.sum(fallosPagina == "X"))

def optimo():
    tabla = np.zeros((nroMarcos, len(paginas)), dtype=int)
    tabla[:,:] = -1

    fallosPagina = np.zeros(len(paginas), dtype=str)
    fallosPagina[:] = "_"
    for i, pag in enumerate(paginas):
        if i == 0:
            tabla[0, 0] = pag
            fallosPagina[0] = "X"
        elif pag in tabla[:, i - 1]:
            tabla[:, i] = tabla[:, i - 1].copy()
        elif -1 in tabla[:, i - 1]:
            tabla[:, i] = tabla[:, i - 1].copy()
            for k, pag1 in enumerate(tabla[:, i]):
                if pag1 == -1:
                    tabla[k, i] = pag
                    fallosPagina[i] = "X"
                    break
        else:
            futuro = np.zeros(nroMarcos)
            futuro[:] = -1
            futuroAux = futuro.copy()
            for k, pagIn in enumerate(tabla[:, i - 1]):
                for g, pag1 in enumerate(paginas[i:]):
                    if pagIn == pag1:
                        futuro[k] = g
                        break
            flags = futuro == futuroAux
            if True in flags:
                cont = np.zeros(nroMarcos)
                tabla[:, i] = tabla[:, i - 1].copy()
                for k, pag1 in enumerate(tabla[:, i - 1]):
                    if flags[k]:
                        j = i
                        while (tabla[k, j] == pag1) and (j >= 0):
                            cont[k] = cont[k] + 1
                            j = j - 1
                maximo = max(cont)
                for k, cant in enumerate(cont):
                    if cant == maximo:
                        tabla[:, i][k] = pag
                        fallosPagina[i] = "X"
                        break
            else:
                maximo = max(futuro)
                for k, pos in enumerate(futuro):
                    if pos == maximo:
                        tabla[:, i] = tabla[:, i - 1].copy()
                        tabla[:, i][k] = pag
                        fallosPagina[i] = "X"
                        break
    print("\nOPTIMO\n", paginas)
    print(tabla)
    print(fallosPagina)
    print("Cantidad de fallos de pagina:", np.sum(fallosPagina == "X"))

FIFO()
LRU()
optimo()