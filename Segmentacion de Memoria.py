import numpy as np

tablaSegmentos = np.array([[334, 440],
                           [320, 50],
                           [290, 739],
                           [156, 287]])

def segmentacion(nroSegmento, desplazamiento):
    try:
        if desplazamiento < tablaSegmentos[nroSegmento, 1]:
            dirFisica = tablaSegmentos[nroSegmento, 0] + desplazamiento
            print("\n", (nroSegmento, desplazamiento), "Si", desplazamiento, "<", tablaSegmentos[nroSegmento, 1], "entonces", tablaSegmentos[nroSegmento, 0], "+", desplazamiento, "=", dirFisica)
        else:
            print("\n" ,(nroSegmento, desplazamiento), "Si", desplazamiento, "<", tablaSegmentos[nroSegmento, 1], "entonces Error de Segmentacion")
    except:
        print("No hay segmento,", nroSegmento, "Error")
segmentacion(0, 444)
segmentacion(1, 23)
segmentacion(2, 738)
segmentacion(3, 287)