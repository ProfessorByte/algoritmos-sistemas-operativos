import numpy as np

tablaPaginas = np.array([100, 200, 3, 8, 2])

def paginacion1(dirLogica1, tamPag):
    try:
        numPag = dirLogica1 // tamPag
        print("\n#Pagina =", dirLogica1, "/", tamPag, "=", numPag)
        desplazamiento = dirLogica1 % tamPag
        print("    Desplazamiento = ", dirLogica1, "mod", tamPag, "=", desplazamiento)
        nuevaDirLog = tablaPaginas[numPag] * tamPag + desplazamiento
        print("   ", (numPag, desplazamiento), "=", (tablaPaginas[numPag], desplazamiento), "=", tablaPaginas[numPag], "*", tamPag, "+", desplazamiento, "=", nuevaDirLog)
    except:
        print("\nError de Paginacion")

def paginacion2(dirLogica2, tamPag):
    try:
        nuevaDirLog = tablaPaginas[dirLogica2[0]] * tamPag + dirLogica2[1]
        print("\n" ,dirLogica2, "=", (tablaPaginas[dirLogica2[0]], dirLogica2[1]), "=", tablaPaginas[dirLogica2[0]], "*", tamPag, "+", dirLogica2[1], "=", nuevaDirLog)
    except:
        print("\nError de Paginacion")

paginacion1(2578, 512)
# paginacion1(31, 32)
# paginacion1(100, 32)
# paginacion2((4, 25), 32)