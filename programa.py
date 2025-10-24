from funcoes import *

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}

tamanho = 4
for i in range(1):
    while True:
        print("Insira as informações referentes ao navio porta-aviões que possui tamanho", tamanho)
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        op = int(input("[1] Vertical [2] Horizontal >"))
        if op == 1:
            orientacao = "vertical"
        else:
            orientacao = "horizontal"

        valido = posicao_valida(frota, linha, coluna, orientacao, tamanho)
        if valido == True:
            frota = preenche_frota(frota, "porta-aviões", linha, coluna, orientacao, tamanho)
            break
        else:
            print("Esta posição não está válida!")

tamanho = 3
for i in range(2):
    while True:
        print("Insira as informações referentes ao navio navio-tanque que possui tamanho", tamanho)
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        op = int(input("[1] Vertical [2] Horizontal >"))
        if op == 1:
            orientacao = "vertical"
        else:
            orientacao = "horizontal"

        valido = posicao_valida(frota, linha, coluna, orientacao, tamanho)
        if valido == True:
            frota = preenche_frota(frota, "navio-tanque", linha, coluna, orientacao, tamanho)
            break
        else:
            print("Esta posição não está válida!")

tamanho = 2
for i in range(3):
    while True:
        print("Insira as informações referentes ao navio contratorpedeiro que possui tamanho", tamanho)
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        op = int(input("[1] Vertical [2] Horizontal >"))
        if op == 1:
            orientacao = "vertical"
        else:
            orientacao = "horizontal"

        valido = posicao_valida(frota, linha, coluna, orientacao, tamanho)
        if valido == True:
            frota = preenche_frota(frota, "contratorpedeiro", linha, coluna, orientacao, tamanho)
            break
        else:
            print("Esta posição não está válida!")

tamanho = 1
for i in range(4):
    while True:
        print("Insira as informações referentes ao navio submarino que possui tamanho", tamanho)
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        orientacao = "vertical"

        valido = posicao_valida(frota, linha, coluna, orientacao, tamanho)
        if valido == True:
            frota = preenche_frota(frota, "submarino", linha, coluna, orientacao, tamanho)
            break
        else:
            print("Esta posição não está válida!")

print(frota)