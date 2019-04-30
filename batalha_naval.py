import random

tabuleiro = [['A','A','A','A'],
             ['A','A','A','A'],
             ['A','A','A','A'],
             ['A','A','A','A']]

def preencher_tabuleiro():
    listaNavios = [
        (random.randrange(4),random.randrange(4)),
        (random.randrange(4),random.randrange(4)),
        (random.randrange(4),random.randrange(4))]

    for i in listaNavios:
        tabuleiro[i[0]][i[1]] = 'N'

def atirar(linha, coluna):
    if tabuleiro[linha][coluna] == 'N':
        tabuleiro[linha][coluna] ='X'
    else:
        tabuleiro[linha][coluna] ='E'

def imprimir_tabuleiro():
    mapeamento = {
        'A': '~',
        'E': 'E',
        'N': '~',
        'X': 'X'
    }
    for linha in tabuleiro:
        for elemento in linha:
            print(mapeamento[elemento], end = ' ')
        print()


def calcular_pontuacao():
    acertos = 0
    erros = 0
    for linha in tabuleiro:
        for elemento in linha:
            if elemento=='X':
                acertos+=1
            elif elemento=='E':
                erros+=1
    return acertos, erros

def exibir_pontuacao():
    acertos, erros = calcular_pontuacao()
    print("Pontuação: %d acerto(s), %d erro(s)" % (acertos, erros))

def main():
    preencher_tabuleiro()
    while True: # TODO Mudar para: enquanto tiver navios
        imprimir_tabuleiro()
        exibir_pontuacao()
        print("Atirar:\n\tlinha: ", end='')
        linha = int(input())
        print("\tColuna: ", end='')
        coluna = int(input())
        atirar(linha, coluna)

main()