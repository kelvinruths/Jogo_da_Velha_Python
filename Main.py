def menu():
    comeco = 1
    while comeco:
        comeco = int(input(
            "\nBem vindo ao Jogo da Velha!"
            "\n Selecione uma opção"
            "\n 1. Jogar"
            "\n 0. Sair"
            "\n - "))

        if comeco != 1: #Tudo que for diferente de 1 fará com que o programa feche
            print("Jogo Encerrando!")
            exit()
        if comeco == 1: #Se for igual a 1 chamará a função jogar()
            jogar()


def jogar(): #Função que define o jogo e suas jogadas
    jogada = 0 # variável acumulada para verificar quantas jogadas foram feitas ou está sendo feita

    while ganhou() == 0: #Enquanto ninguém ganhou o jogo, verificado pela função ganhou() fará:
        print("\n Jogador ", jogada % 2 + 1) #jogada % 2 + 1 : o resto da divisão será a definição do jogador que está jogando aquela rodada
        exibir() #Função que mostra o tabuleiro
        linha = int(input("\n Linha: ")) #Escolha da linha
        coluna = int(input("\n Coluna: ")) #Escolah da coluna

        if mesa[linha-1][coluna-1] == 0:
            if(jogada % 2 + 1) == 1:
                mesa[linha - 1][coluna - 1] = 1
            else:
                mesa[linha - 1][coluna - 1] = - 1
        else:
            print("Não está vazio")
            jogada -= 1

        if ganhou():
            print("\nJogador ", jogada % 2 + 1, " Ganhou após ", jogada + 1, " rodadas")

        jogada += 1


def ganhou():
    for i in range(3):
        soma = mesa[i][0] + mesa[i][1] + mesa[i][2]
        if soma == 3 or soma == - 3:
            return 1

    for i in range(3):
        soma = mesa[0][i] + mesa[1][i] + mesa[2][i]
        if soma == 3 or soma == - 3:
            return 1

    diagonal1 = mesa[0][0] + mesa[1][1] + mesa[2][2]
    diagonal2 = mesa[0][2] + mesa[1][1] + mesa[2][0]
    if diagonal1 == 3 or diagonal1 == - 3 or diagonal2 == 3 or diagonal2 == - 3:
        return 1

    return 0


def exibir():
    for i in range(3):
        linha = ""
        for j in range(3):
            if mesa[i][j] == 0:
                linha += "| - "
            elif mesa[i][j] == 1:
                linha += "| X "
            elif mesa[i][j] == -1:
                linha += "| O "
        linha += "|"
        print(linha)

    print()


mesa = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

menu()
