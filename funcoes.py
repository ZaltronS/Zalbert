def define_posicoes (linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == "vertical":
        for i in range(tamanho):  #tamanho do navio recebido na funcao
            posicoes.append([linha + i, coluna]) 
    elif orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])

    return posicoes


def preenche_frota (dic_frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in dic_frota: 
        dic_frota[nome_navio] = []
    dic_frota[nome_navio].append(posicoes)
    return dic_frota


def faz_jogada (tabuleiro, linha, coluna):
    celula = tabuleiro[linha][coluna]
    if celula == 1:
        tabuleiro[linha][coluna] = "X"
    elif celula == 0:
        tabuleiro[linha][coluna] = "-"

    return tabuleiro

def posiciona_frota (dic_frota):
    tabuleiro = []
    for i in range(10):
        linha = [0] * 10
        tabuleiro.append(linha)

    for navio in dic_frota:
        for um_navio in dic_frota[navio]:
            for posicao in um_navio:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1

    return tabuleiro

def afundados (dic_frota, tabuleiro):
    afundados = 0
    for navios in dic_frota.values():
        for posicoes_navio in navios:
            afundado = True
            for linha, coluna in posicoes_navio:
                if tabuleiro[linha][coluna] != "X":
                    afundado = False
                    break
            if afundado == True:
                afundados += 1

    return afundados

    