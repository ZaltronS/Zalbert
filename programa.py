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

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'
    for linha in range(10):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)

posicoes_jogadas = []
jogando = True

while jogando == True:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    while True:
        linha = int(input("Qual linha deseja atacar? "))
        while linha < 0 or linha > 9:
            print("Linha inválida!")
            linha = int(input("Qual linha deseja atacar? "))

        coluna = int(input("Qual coluna deseja atacar? "))
        while coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            coluna = int(input("Qual coluna deseja atacar? "))

        if [linha, coluna] in posicoes_jogadas:
            print("A posição linha", linha, "e coluna", coluna, "já foi informada anteriormente!")
            continue
        else:
            posicoes_jogadas.append([linha, coluna])
            break

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False