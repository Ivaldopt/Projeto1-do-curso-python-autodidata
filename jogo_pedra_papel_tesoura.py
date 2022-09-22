from random import randint

# criar uma lista de opçao do jogo
opcao = ["pedra", "papel", "tesoura"]

# reproduz uma opcao aleatoria do computador
computador = opcao[randint(0, 2)]

# definir jogador para falso
jogador = False

while jogador == False:

    jogador = input("pedra, papel, tesoura? ")
    if jogador == computador:
        print("empate")
    elif jogador == "pedra":
        if computador == "papel":
            print("Você perdeu!", computador, "cobriu", jogador)
        else:
            print("Você Ganhou!", jogador, "Esmaguei", computador)
    elif jogador == "papel":
        if computador == "tesoura":
            print("Você perdeu!", computador, "corte", jogador)
        else:
            print("Você Ganhou!", jogador, "cobriu", computador)
    elif jogador == "tesoura":
        if computador == "pedra":
            print("Você perdeu...", computador, "esmaga", jogador)
        else:
            print("Você Venceu!", jogador, "corte", computador)
    else:
        print("Essa nao é uma jogada válida, veja sua ortografia!")
    jogador = False
    computador = opcao[randint(0, 2)]
