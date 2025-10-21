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

