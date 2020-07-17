# coding: utf-8
import sys
from docplex.cp.model import CpoModel

'''
O problema da mochila é um problema de optimização combinatória.
O nome dá-se devido ao modelo de uma situação em que é necessário
preencher uma mochila com objetos de diferentes pesos e valores.
O objetivo é que se preencha a mochila com o maior valor possível,
não ultrapassando o peso máximo.

https://pt.wikipedia.org/wiki/Problema_da_mochila#0/1
'''
# Create CPO model


def knapsacCplex(mdl, k, profits, weights, n):
    # -----------------------------------------------------------------------------
    # Inicializando dados
    # -----------------------------------------------------------------------------
    zero_or_one = [mdl.integer_var(min=0, max=1, name="X{}: P {} W {}".format(i+1, profits[i], weights[i]))
                   for i in range(n)]  # varivaveis de decisao
    # -----------------------------------------------------------------------------

    # -----------------------------------------------------------------------------
    # Construindo o modelo
    # -----------------------------------------------------------------------------

    # função objetivo
    fo = mdl.sum(p*x for p, x in zip(profits, zero_or_one))
    mdl.add(mdl.maximize(fo))

    # sujeito a
    restricoes = mdl.sum(w*x for w, x in zip(weights, zero_or_one))
    mdl.add(restricoes <= k)
    # -----------------------------------------------------------------------------


def read_from(filepath):
    f = open(filepath, "r")

    n = None
    k = 0
    profits = []
    weights = []

    countline = 0

    for line in f.readlines():
        try:
            a, b = line.strip().split(' ')
            if countline == 0:
                n, k = int(a), int(b)
            else:
                profits.append(float(a))
                weights.append(float(b))

            countline += 1
        except:
            pass

    return k, profits, weights, n


if __name__ == "__main__":
    # k = 850  # capacidade da mochila
    # profits = [360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
    #            78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
    #            87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
    #            312]  # profits = lucros
    # weights = [7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
    #            42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
    #            3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13]  # weights = pesos
    # n = len(weights)
    mdl = CpoModel()

    k, profits, weights, n = read_from(sys.argv[1])
    knapsacCplex(mdl, k, profits, weights, n)

    print("\nImprimindo solução....")
    msol = mdl.solve(TimeLimit=60, Workers=1)

    if msol:
        print(msol.print_solution())
        print("Status: " + msol.get_solve_status())
    else:
        print("Nenhuma solução encontrada")
