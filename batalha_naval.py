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


class Jogador:
    
    def __init__(self):
        self.tabuleiro = [['A' for x in range(4)] for y in range(4)]
        self.acertos = 0
        self.erros = 0

humano = Jogador()

maquina = Jogador()

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
    
    acertos = sum(map(lambda a: 1 if a=='X' else 0, [item for sublist in tab for item in sublist]))
    erros = sum(map(lambda a: 1 if a=='E' else 0, [item for sublist in tab for item in sublist]))
        
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
    preencher_tabuleiro(humano.tabuleiro)
    acerto_atual = 0
    vez = 1
    while verificar_navios(maquina.tabuleiro) != 0 and verificar_navios(humano.tabuleiro) != 0:
        clear()
        print('maquina: ')
        acerto_atual = exibir_pontuacao(humano)
        print('humano: ')
        acerto_atual = exibir_pontuacao(maquina)

        if(vez % 2):
            print("VEZ DO JOGADOR")
            imprimir_tabuleiro(maquina.tabuleiro)
            #acerto_atual = exibir_pontuacao(maquina)
            print('')
            imprimir_tabuleiro(humano.tabuleiro)
            #acerto_atual = exibir_pontuacao(humano)
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
            imprimir_tabuleiro(humano.tabuleiro)
            #acerto_atual = exibir_pontuacao(humano)
            print('')
            imprimir_tabuleiro(maquina.tabuleiro)   
            #acerto_atual = exibir_pontuacao(maquina)
       
            print("Atirar:\n\tlinha: ", end='')
            linha = input()
            print("\tColuna: ", end='')
            coluna = input()
            try:    
                atirar(humano.tabuleiro,int(linha), int(coluna))
                if verificar_navios(humano.tabuleiro) != 0:
                    print("Fim de Jogo! Máquina Venceu!!")
                    imprimir_tabuleiro(humano.tabuleiro)
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
        

        # VEZ = par humano, VEZ = impar maquina
        vez += 1       
        
    
    
    
main()