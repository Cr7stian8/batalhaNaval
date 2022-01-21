
import time
import random


#Função que pergunta onde a maquina quer atirar
def tiro2():

    #Pergunta e valida a linha do ataque
    while True:
        abcd = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        linha2 = abcd[random.randrange(0,7)].upper()
        print('Linha escolhida pela máquina: ',linha2)
        break

    #Pergunta e valida a coluna do ataque
    while True:
        coluna2 = random.randrange(1,8)
        print('coluna escolhida pela máquina: ',coluna2)
        break
    
    linha2 = ord(linha2) - 65
    #Diminui 1 da coluna, Assim, quando for digitado: 1 = 0; 2 = 1; 3 = 2...
    coluna2 -= 1

    return linha2, coluna2

#Função que pergunta onde o usuário quer atirar
def tiro():

    #Pergunta e valida a linha do ataque
    while True:
        linha = input('Qual linha do seu ataque? ').upper()
        if linha < 'A' or linha > 'H' or len(linha) > 1:
            print('ERRO')
            continue
        else:
            break

    #Pergunta e valida a coluna do ataque
    while True:
        coluna = int(input('Qual coluna do seu ataque? '))
        if coluna <= 0 or coluna > 8:
            print('ERRO')
            continue
        else:
            break

    linha = ord(linha) - 65

    #Diminui 1 da coluna quando a pessoa for escolher o lugar do tiro
    coluna -= 1

    return linha, coluna

def resultado_tiro2(boardTP, boardP, linha2, coluna2):

    #Testa se o local digitado já foi bombardeado, se sim, retorna False, passando a vez pro jogador
    if boardP[linha2][coluna2] == 'P' or boardP[linha2][coluna2] == 'X' or boardP[linha2][coluna2] == 'C' or boardP[linha2][coluna2] == 'N' or boardP[linha2][coluna2] == 'S':
        print('JÁ BOMBARDEADO - PERDEU A VEZ')
        time.sleep(2)
        return False

    #Testa se o local digitado é um Navio, se sim, retorna True, e a vez continua sendo do mesmo jogador
    elif boardTP[linha2][coluna2] ==  'P' or boardTP[linha2][coluna2] == 'S' or boardTP[linha2][coluna2] == 'C' or boardTP[linha2][coluna2] == 'N':

      if boardTP[linha2][coluna2]=='P':
        boardP[linha2][coluna2] = 'P'
        print('ACERTOU - SUA VEZ NOVAMENTE')
        return True

      if boardTP[linha2][coluna2]=='S':
        boardP[linha2][coluna2] = 'S'
        print('ACERTOU - SUA VEZ NOVAMENTE') 
        return True  

      if boardTP[linha2][coluna2]=='C':
        boardP[linha2][coluna2] = 'C'
        print('ACERTOU - SUA VEZ NOVAMENTE') 
        return True 

      if boardTP[linha2][coluna2]=='N':
        boardP[linha2][coluna2] = 'N'
        print('ACERTOU - SUA VEZ NOVAMENTE')           
        return True

    #Testa se o local digitado é Água, se sim, retorna False, passando a vez pro jogador
    else:
        boardP[linha2][coluna2] = 'X'
        print('X = ERROU !! - PERDEU A VEZ')
        time.sleep(2)
        return False

#Função que retorna o resultado do ataque

def resultado_tiro(boardTP2, boardP2, linha, coluna):

    #Testa se o local digitado já foi bombardeado, se sim, retorna False, passando a vez pro jogador
    if boardP2[linha][coluna] == 'P' or boardP2[linha][coluna] == 'X' or boardP2[linha][coluna] == 'C' or boardP2[linha][coluna] == 'N' or boardP2[linha][coluna] == 'S':
        print('JÁ BOMBARDEADO - PERDEU A VEZ')
        return False

    #Testa se o local digitado é um Navio, se sim, retorna True, e a vez continua sendo do mesmo jogador

    elif boardTP2[linha][coluna] ==  'P' or boardTP2[linha][coluna] == 'S' or boardTP2[linha][coluna] == 'C' or boardTP2[linha][coluna] == 'N':
      if boardTP2[linha][coluna]=='P':
        boardP2[linha][coluna] = 'P'
        print('ACERTOU - SUA VEZ NOVAMENTE')
        return True

      if boardTP2[linha][coluna]=='S':
        boardP2[linha][coluna] = 'S'
        print('ACERTOU - SUA VEZ NOVAMENTE') 
        return True  

      if boardTP2[linha][coluna]=='C':
        boardP2[linha][coluna] = 'C'
        print('ACERTOU - SUA VEZ NOVAMENTE') 
        return True 

      if boardTP2[linha][coluna]=='N':
        boardP2[linha][coluna] = 'N'
        print('ACERTOU - SUA VEZ NOVAMENTE')           
        return True

    #Testa se o local digitado é Água, se sim, retorna False, passando a vez pro jogador
    else:
        boardP2[linha][coluna] = 'X'
        print(' ERROU !!! - PERDEU A VEZ'),
        return False


#Função que cria os tabuleiros
def boards():
    brd = [['-']*10 for i in range(8)]

    return brd


def explicação():

        print('\n--> Existem QUATRO embarcações disponíveis')
        print('   -> Submarino --> Ocupa dois espaços, e devem ter dois no jogo')
        print('   -> Contratorpedeiro --> Ocupa três espaços e deve existir um no jogo ')
        print('   -> Navio tanque --> Ocupa quatro espaços no tabuleiro e deve existir um no jogo')
        print('   -> Porta aviões --> Ocupa cinco espaços e deve exir um no jogo\n')
        print('   --> As linhas e colunas começam em 0')
        print('   --> de modo que a coordenada [0,0] é a inicial e a [7,7] é a final\n')
        print('\n     --> S= Submarino ')
        print('     --> C= Contratorpedeiro ')
        print('     --> P= Porta aviões')
        print('     --> N= Navio tanque ')
        print('     --> X= Erro')

def fleets_maquina(brd):
    cont = 0
    board = brd
    l1=0
    c1=0

    # Onde os navios serão lançados
    while cont < 16:
      #Submarinos
      if cont<4:
        c1= c1+1
        l = l1
        c = c1
        board[l][c] = 'S'
        cont += 1

      if cont==4:
        c1=2

      #Contratorpedeiro
      if cont<7 and cont>3:
        l1=5
        l = l1
        c = c1
        board[l][c] = 'C'
        cont += 1
        c1=c1+1

      #Navio tanque
      if cont==7:
        l1=2
        c1=0

      if cont > 6 and cont<11:
        l = l1
        c = c1
        board[l][c] = 'N'
        cont += 1
        c1=c1+1

      if cont==11:
        l1=7
        c1=1  
      #Porta aviões  
      if cont > 10 and cont<16:
        l = l1
        c = c1
        board[l][c] = 'P'
        cont += 1      
        c1 = c1+1


    return board


#Função que distribui os navios no tabuleiro de frotas
def fleets_jogador(brd):
    cont = 0
    board = brd

    # Onde os navios serão lançados
    
    while cont < 16:
      if cont<2:

      #Submarinos
        l = int(input('\nDigite a linha que deseja posicionar o 1º Submarino '))
        while l<0 or l>7:
          print('Erro !!!')
          l = int(input('\nDigite a linha que deseja posicionar o 1º Submarino '))

        c = int(input('Digite a coluna que deseja posicionar o 1º Submarino '))
        while c<0 or c>7:
          print('Erro !!!')
          c = int(input('Digite a coluna que deseja posicionar o 1º Submarino '))
        
        board[l][c] = 'S'
        cont += 1

      if cont>1 and cont<4:  
        l = int(input('\nDigite a linha que deseja posicionar o 2º Submarino '))
        while l<0 or l>7:
          print('Erro !!!')
          l = int(input('\nDigite a linha que deseja posicionar o 2º Submarino '))

        c = int(input('Digite a coluna que deseja posicionar o 2º Submarino '))
        while c<0 or c>7:
          print('Erro !!!')
          c = int(input('Digite a coluna que deseja posicionar o 2º Submarino '))

        board[l][c] = 'S'
        cont += 1

      #Contratorpedeiro
      if cont<7 and cont>3:
        l = int(input('\nDigite a linha que deseja posicionar o contratorpedeiro'))
        while l<0 or l>7:
          print('Erro !!!')
          l = int(input('\nDigite a linha que deseja posicionar o contratorpedeiro '))

        c = int(input('Digite a coluna que deseja posicionar o contratorpedeiro '))
        while c<0 or c>7:
          print('Erro !!!')
          c = int(input('Digite a coluna que deseja posicionar o contratorpedeiro '))

        board[l][c] = 'C'
        cont += 1

      #Navio tanque
      if cont > 6 and cont<11:
        l = int(input('\nDigite a linha que deseja posicionar o navio tanque'))
        while l<0 or l>7:
          print('Erro !!!')
          l = int(input('\nDigite a linha que deseja posicionar o navio Tanque '))

        c = int(input('Digite a coluna que deseja posicionar o navio tanque'))
        while c<0 or c>7:
          print('Erro !!!')
          c = int(input('Digite a coluna que deseja posicionar o navio tanque '))

        board[l][c] = 'N'
        cont += 1

      #Porta aviões  
      if cont > 10 and cont<16:
        l = int(input('\nDigite a linha que deseja posicionar o porta aviões'))
        while l<0 or l>7:
          print('Erro !!!')
          l = int(input('\nDigite a linha que deseja posicionar o porta aviões '))

        c = int(input('Digite a coluna que deseja posicionar o porta aviões'))
        while c<0 or c>7:
          print('Erro !!!')
          c = int(input('Digite a coluna que deseja posicionar o porta aviões'))

        board[l][c] = 'P'
        cont += 1
    return board

import os


#Função que exibe o tabuleiro de frotas
def print_test(tabTP1, tabTP2):

    print()
    print_map(tabTP1, tabTP2)#Printa o tabuleiro de frota do Jogador 1 e Jogador 2

#Função que exibe os tabuleiros de jogo
def print_game(tabP1, tabP2, scoreP1, scoreP2):

    print_map(tabP1, tabP2)#Printa o tabuleiro do Jogador 1 e Jogador 2
    print()
    #Exibe a pontuação dos jogadores
    print(f'''
    Pontuação {nome}  = {scoreP1}
    Pontuação Máquina = {scoreP2}''')

#Função que printa os tabuleiros
def print_map(tab1, tab2):
    #Vetor usado para indicar qual é a linha do tabuleiro
    abcd = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    #Printa os escopos dos tabuleiros
    print(f''' 
           {nome}                              Máquina
   |1  2  3  4  5  6  7  8            |1  2  3  4  5  6  7  8
  ------------------------           --------------------------''')

    for i in range(8):
        print(f'{abcd[i]}  |', end='')
        for j in range(8):
            print(f'{tab1[i][j]:3}', end='')
        print(end='       ')

        print(f'{abcd[i]}  |', end='')
        for k in range(8):
            print(f'{tab2[i][k]:3}', end='')
        print()

# ---------------------- FUNÇÃO QUE INICIA O JOGO ----------------------------#

def new_game():
    
    #Definindo a quantidade de embarcações
    while True:
        numberShips = 16
        global nome
        nome=input('Digite seu nome: ')
        break
    
    explicação()
    #Cria o tabuleiro de frotas do jogador 1
    boardTP1 = boards()
    boardTP1 = fleets_jogador(boardTP1)
    #Cria o tabuleiro de frotas do jogador 2
    boardTP2 = boards()
    boardTP2 = fleets_maquina(boardTP2)
    #Cria o tabuleiro que vai ser exibido para os jogadores
    boardP1 = boards()
    boardP2 = boards()
    #Pontuação dos jogadores 1 e 2
    scoreP1 = 0
    scoreP2 = 0
    #Contagem para indicar de quem a vez de jogada, onde (Ímpar = Jogador 1) e (PAR = Jogador 2) 
    count = 1
    #Opção de para ativar a exibição do tabuleiro de frotas dos usuários (APENAS PARA TESTE)
    while True:
        test = input('Deseja mostrar as frotas(Função de Teste)?[Sim ou Nao] ').upper()
        if test != 'SIM' and test != 'NAO':
            print('ERRO')
            continue
        else:
            break

    while True:
        #Valida se deve ser exibido o tabuleiro de frotas ou não
        if test == 'SIM':
            print_game(boardP1, boardP2, scoreP1, scoreP2)
            print_test(boardTP1, boardTP2)
        else:
            print_game(boardP1, boardP2, scoreP1, scoreP2)
        print()

        #Testa se algum dos jogadores já ganhou a partida
        if scoreP1 == numberShips:
            print(f'{nome} GANHOU !!!')
            break
        elif scoreP2 == numberShips:
            print('A máquina venceu !!!')
            break
        
        #Verifica de quem é a vez de jogada
        if count % 2 != 0:
            print(f'{nome}')
            
            #Pega qual linha e coluna o jogador escolheu para atacar
            linha, coluna = tiro()

            #Verifica se o jogador acertou um navio
            if resultado_tiro(boardTP2, boardP2, linha, coluna):
                scoreP1 += 1
            else:
                count += 1
        else:
            print('Máquina')

            #Pega qual linha e coluna o jogador escolheu para atacar
            linha2, coluna2 = tiro2()

            #Verifica se o jogador acertou um navio
            if resultado_tiro2(boardTP1, boardP1, linha2, coluna2):
                scoreP2 += 1
            else:
                count += 1

while True:
    print('--> NOVO JOGO [1]')
    print('--> FECHAR    [2]')

    #Inicia um novo jogo ou fecha o jogo
    newG = int(input('--> DIGITE SUA ESCOLHA: '))
    if newG == 1:
        new_game()
    elif newG == 2:
        print('--> PROGRAMA ENCERRADO !!!!')
        break
    else:
        #caso seja digitado um número inválido
        print('Erro')

