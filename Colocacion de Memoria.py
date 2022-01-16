import numpy as np

def first_fit(memoria, procesos):
    flags = np.zeros(memoria.shape[0], dtype=bool)
    memoria = np.append(memoria, np.zeros((memoria.shape[0], 2)), axis=1)
    for proc in procesos:
        for i, mem in enumerate(memoria):
            if (not flags[i]) and (mem[0] >= proc):
                mem[2] = proc
                mem[1] = mem[0] - mem[2]
                flags[i] = True
                break
    print(memoria)
    print("Fragmentacion Interna: ", sum(memoria[:,1]))
    print ("Fragmentacion Externa: ", sum(memoria[:,0][memoria[:,2] == 0]))

def next_fit(memoria, procesos):
    flags = np.zeros(memoria.shape[0], dtype=bool)
    memoria = np.append(memoria, np.zeros((memoria.shape[0], 2)), axis=1)
    for proc in procesos:
        for i, mem in enumerate(memoria):
            if i == memoria.shape[0] - 1:
                for k, mem1 in enumerate(memoria):
                    if mem1[2] == 0:
                        flags[k] = False
            if ((not flags[i]) and (mem[0] >= proc)):
                mem[2] = proc
                mem[1] = mem[0] - mem[2]
                flags[i] = True
                break
            flags[i] = True
    print(memoria)
    print("Fragmentacion Interna: ", sum(memoria[:,1]))
    print ("Fragmentacion Externa: ", sum(memoria[:,0][memoria[:,2] == 0]))

def best_fit(memoria, procesos):
    flags = np.zeros(memoria.shape[0], dtype=bool)
    memoria = np.append(memoria, np.zeros((memoria.shape[0], 2)), axis=1)
    for proc in procesos:
        menorDiferencia = (float("inf"), -1)
        for i, mem in enumerate(memoria):
            diferencia = mem[0] - proc
            if (not flags[i]) and (mem[0] >= proc) and (menorDiferencia[0] > diferencia):
                menorDiferencia = (diferencia, i)
        if menorDiferencia[1] != -1:
            memoria[menorDiferencia[1],2] = proc
            memoria[menorDiferencia[1],1] = memoria[menorDiferencia[1],0] - memoria[menorDiferencia[1],2]
            flags[menorDiferencia[1]] = True
    print(memoria)
    print("Fragmentacion Interna: ", sum(memoria[:,1]))
    print ("Fragmentacion Externa: ", sum(memoria[:,0][memoria[:,2] == 0]))

def worst_fit(memoria, procesos):
    flags = np.zeros(memoria.shape[0], dtype=bool)
    memoria = np.append(memoria, np.zeros((memoria.shape[0], 2)), axis=1)
    for proc in procesos:
        mayorDiferencia = (-1, -1)
        for i, mem in enumerate(memoria):
            diferencia = mem[0] - proc
            if (not flags[i]) and (mem[0] >= proc) and (mayorDiferencia[0] < diferencia):
                mayorDiferencia = (diferencia, i)
        if mayorDiferencia[1] != -1:
            memoria[mayorDiferencia[1],2] = proc
            memoria[mayorDiferencia[1],1] = memoria[mayorDiferencia[1],0] - memoria[mayorDiferencia[1],2]
            flags[mayorDiferencia[1]] = True
    print(memoria)
    print("Fragmentacion Interna: ", sum(memoria[:,1]))
    print ("Fragmentacion Externa: ", sum(memoria[:,0][memoria[:,2] == 0]))

def main(memoria, procesos):
    print("First Fit")
    first_fit(memoria, procesos)
    print("\nNext Fit")
    next_fit(memoria, procesos)
    print("\nBest Fit")
    best_fit(memoria, procesos)
    print("\nWorst Fit")
    worst_fit(memoria, procesos)

main(np.array([[1350], [725], [1640], [890], [1220]]),
     np.array([1200, 980, 1150, 650, 820]))

# first_fit(np.array([[12], [14], [2], [21], [5], [18], [13], [32]]),
#           np.array([5, 29, 7]))

# next_fit(np.array([[12], [14], [2], [21], [5], [18], [13], [32]]),
#          np.array([5, 29, 7]))

# best_fit(np.array([[12], [14], [2], [21], [5], [18], [13], [32]]),
#          np.array([5, 29, 7]))

# worst_fit(np.array([[12], [14], [2], [21], [5], [18], [13], [32]]),
#          np.array([5, 29, 7]))
