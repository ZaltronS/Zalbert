def define_posicoes (linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == "vertical":
        for i in range(tamanho):  #tamanho do navio recebido na funcao
            posicoes.append([linha + i, coluna]) 
    elif orientacao == "horizontal":
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])

    return posicoes
