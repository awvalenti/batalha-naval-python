import random

# import only system from os 
from os import system, name 
  
# define our clear function 
def clear():  
    # for windows 
    if name == 'nt': 
        _ = system('cls')   
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

tabuleiroJ = [['A','A','A','A'],
            ['A','A','A','A'],
            ['A','A','A','A'],
            ['A','A','A','A']]

tabuleiroM = [['A','A','A','A'],
            ['A','A','A','A'],
            ['A','A','A','A'],
            ['A','A','A','A']]

class Jogador:
    
    def __init__(self, tabuleiro):
        self.tabuleiro = tabuleiro
        self.acertos = 0
        self.erros = 0

jogador = Jogador(tabuleiroJ)

maquina = Jogador(tabuleiroM)

def preencher_tabuleiro(tab):
    listaNavios = [
        (random.randrange(4),random.randrange(4)),
        (random.randrange(4),random.randrange(4)),
        (random.randrange(4),random.randrange(4))]

    for i in listaNavios:   
        tab[i[0]][i[1]] = 'N'    

    print(listaNavios)

def atirar(tabuleiro,linha, coluna):
    if tabuleiro[linha][coluna] == 'N' or tabuleiro[linha][coluna]=='X' :
        tabuleiro[linha][coluna] ='X'
    else:
        tabuleiro[linha][coluna] ='E'


def imprimir_tabuleiro(tab):
    mapeamento = {
        'A': '~',
        'E': 'E',
        'N': '~',
        'X': 'X'
    }
    for linha in tab:
        for elemento in linha:
            print(mapeamento[elemento], end = ' ')
        print()


def calcular_pontuacao(tab):
    acertos = 0
    erros = 0
    for linha in tab:
        for elemento in linha:
            if elemento=='X':
                acertos+=1
            elif elemento=='E':
                erros+=1     
    return acertos, erros
    
def verificar_navios(tab):
    contador = 0

    for linha in tab:
        if linha.count('N') != 0:
            contador+=linha.count('N')
    #print("Número de Navios:",contador)
    #print("-----------------------------")
    return contador

def exibir_pontuacao(jogHumMaq):

    jogHumMaq.acertos, jogHumMaq.erros = calcular_pontuacao(jogHumMaq.tabuleiro)
    
    print("Pontuação: %d acerto(s), %d erro(s)" % (jogHumMaq.acertos, jogHumMaq.erros))
    return jogHumMaq.acertos

def main():
    preencher_tabuleiro(maquina.tabuleiro)
    preencher_tabuleiro(jogador.tabuleiro)
    acerto_atual = 0
    vez = 1
    while verificar_navios(maquina.tabuleiro) != 0 and verificar_navios(jogador.tabuleiro) != 0:
        clear()
        if(vez % 2):
            print("VEZ DA JOGADOR")
            imprimir_tabuleiro(maquina.tabuleiro)
            acerto_atual = exibir_pontuacao(jogador)
            print("Atirar:\n\tlinha: ", end='')
            linha = input()
            print("\tColuna: ", end='')
            coluna = input()
            try:                    
                atirar(maquina.tabuleiro,int(linha), int(coluna))
                if verificar_navios(maquina.tabuleiro) != 0:
                    print("Fim de Jogo! Jogador Venceu!!")
                    imprimir_tabuleiro(maquina.tabuleiro)


            except ValueError:
                print("Você deve digitar somente números!")
                print("Pressione Enter para continuar")
                input()
            except IndexError:
                print("Os valores vão de 0 a 3!")
                print("Pressione Enter para continuar")
                input()
            except Exception:
                print("Não sei o que deu mas deu ruim")
                input()
        else:
            print("VEZ DA MAQUINA")
            imprimir_tabuleiro(jogador.tabuleiro)
            acerto_atual = exibir_pontuacao(maquina)
            print("Atirar:\n\tlinha: ", end='')
            linha = input()
            print("\tColuna: ", end='')
            coluna = input()
            try:    
                atirar(jogador.tabuleiro,int(linha), int(coluna))
                if verificar_navios(jogador.tabuleiro) != 0:
                    print("Fim de Jogo! Máquina Venceu!!")
                    imprimir_tabuleiro(jogador.tabuleiro)
            except ValueError:
                print("Você deve digitar somente números!")
                print("Pressione Enter para continuar")
                input()
            except IndexError:
                print("Os valores vão de 0 a 3!")
                print("Pressione Enter para continuar")
                input()
            except Exception:
                print("Não sei o que deu mas deu ruim")
                input()

        # VEZ = par jogador, VEZ = impar maquina
        vez += 1       
        
    
    
    
main()