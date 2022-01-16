import numpy as np

tablaSegmentos = np.array([[0, 600],
                           [2, 14]])

tablaPaginas = np.array([50, 22, 145, 29, 21, 83, 210])

tamPag = 256

def paginacionSegmentacion(nroSegmento, desplazamiento):
    try:
        if desplazamiento < tablaSegmentos[nroSegmento, 1]:
            print("\n" ,(nroSegmento, desplazamiento), "Si", desplazamiento, "<", tablaSegmentos[nroSegmento, 1], "entonces")
            numPag = desplazamiento // tamPag
            print("    #Pagina =", desplazamiento, "/", tamPag, "=", numPag)
            desplazamiento1 = desplazamiento % tamPag
            print("    Desplazamiento =", desplazamiento, "mod", tamPag, "=", desplazamiento1)
            dirFisica = tablaSegmentos[nroSegmento, 0] + numPag
            print("   ", (numPag, desplazamiento1), "base + #Pagina =", tablaSegmentos[nroSegmento, 0], "+", numPag, "=", dirFisica)
            dirLogica = tablaPaginas[dirFisica] * tamPag + desplazamiento1
            print("   ", (tablaPaginas[dirFisica], desplazamiento1), "=", tablaPaginas[dirFisica], "*", tamPag, "+",desplazamiento1, "=", dirLogica)
        else:
            print("\n" ,(nroSegmento, desplazamiento), "Si", desplazamiento, "<", tablaSegmentos[nroSegmento, 1], "entonces Error de Segmentacion")
    except:
        print("\n", (nroSegmento, desplazamiento), "No hay segmento", nroSegmento, "Error")

paginacionSegmentacion(0, 259)
paginacionSegmentacion(0, 518)
paginacionSegmentacion(1, 10)
paginacionSegmentacion(0, 600)
paginacionSegmentacion(3, 150)