print("Aqui temos 3 jogos: A-Blackjack (Jogador vs IA), B-Blackjack (Jogador vs Jogador) e NM-Número Mágico.")
print("")
p_j = input("Que jogo deseja jogar: ")
print("")
print("")
if p_j == "A" or p_j == "a":
    import random

    baralho = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4


    def distribuir(baralho):
        mao = []
        for eu in range(2):
            random.shuffle(baralho)
            carta = baralho.pop()
            if carta == 11:
                carta = "J"
            if carta == 12:
                carta = "Q"
            if carta == 13:
                carta = "K"
            if carta == 14:
                carta = "A"
            mao.append(carta)
        return mao


    def jogar_denovo():
        print("")
        print("")
        jn = input("Deseja jogar outra vez? S/N: ")
        while jn != "S" and jn != "s" and jn != "N" and jn != "n":
            print("")
            jn = input("Deseja jogar outra vez? S/N: ")
        if jn == "S" or jn == "s":
            jogo()
        if jn == "N" or jn == "n":
            print("")
            print("Até à próxima!")
            exit()


    def total(mao):
        total = 0
        for carta in mao:
            if carta == "J" or carta == "Q" or carta == "K":
                total = total + 10
            elif carta == "A":
                if total >= 11:
                    total = total + 1
                else:
                    total = total + 11
            else:
                total = total + carta
        return total


    def pedir(mao):
        carta = baralho.pop()
        if carta == 11:
            carta = "J"
        if carta == 12:
            carta = "Q"
        if carta == 13:
            carta = "K"
        if carta == 14:
            carta = "A"
        mao.append(carta)
        return mao


    def resultados(mao_comp, mao_jogador):
        print("O computador possui {} a soma das cartas vale {}".format(mao_comp, total(mao_comp)))
        print("Tu possuis {} a soma das cartas dá {}".format(mao_jogador, total(mao_jogador)))


    def blackjack(mao_comp, mao_jogador):
        if total(mao_jogador) == 21:
            print("")
            print("**********************************")
            print("")
            resultados(mao_comp, mao_jogador)
            print("Parabéns, ganhaste o Blackjack!")
            jogar_denovo()
        if total(mao_comp) == 21:
            print("")
            print("**********************************")
            print("")
            resultados(mao_comp, mao_jogador)
            print("")
            print("Lamento, desta vez perdeste. O computador ganhou o blackjack.")
            jogar_denovo()


    def pontos(mao_comp, mao_jogador):
        if total(mao_jogador) == 21:
            resultados(mao_comp, mao_jogador)
            print("")
            print("Parabéns, ganhaste o Blackjack.")
            jogar_denovo()
        if total(mao_comp) == 21:
            resultados(mao_comp, mao_jogador)
            print("")
            print("Lamento, desta vez perdeste. O computador ganhou o blackjack!.")
            jogar_denovo()
        if total(mao_jogador) > 21:
            resultados(mao_comp, mao_jogador)
            print("")
            print("Lamento, rebentaste o jogo, perdeste.")
            jogar_denovo()
        if total(mao_comp) > 21:
            resultados(mao_comp, mao_jogador)
            print("")
            print("Ganhaste, o computador rebentou o jogo!")
            jogar_denovo()
        if total(mao_jogador) < total(mao_comp):
            resultados(mao_comp, mao_jogador)
            print("")
            print("Lamento, os teus pontos são menores do que os do computador. Perdeste.")
            jogar_denovo()
        if total(mao_jogador) > total(mao_comp):
            resultados(mao_comp, mao_jogador)
            print("")
            print("Parabéns! O teus pontos são superiores aos do computador! Ganhaste o Blackjack")
            jogar_denovo()
        if total(mao_comp) == total(mao_jogador):
            resultados(mao_comp, mao_jogador)
            print("")
            print("Houve empate.")
            jogar_denovo()


    def jogo():
        escolha = "n"
        escolha1 = "n"
        print("")
        print("******** Vamos Começar! *******")
        print("")
        mao_comp = distribuir(baralho)
        mao_jogador = distribuir(baralho)
        while escolha != "s":
            print("O computador possui {}".format(str(mao_comp[0])))
            print("Tu possuis {} a soma das cartas vale {}".format(str(mao_jogador), str(total(mao_jogador))))
            print("")
            blackjack(mao_comp, mao_jogador)
            escolha = input("Queres [P]edir ou [M]anter? ")
            if escolha == "P" or escolha == "p":
                pedir(mao_jogador)
                while total(mao_comp) < 17:
                    pedir(mao_comp)
                while escolha1 != "s":
                    if total(mao_jogador) > 21:
                        print("")
                        print("**********************************")
                        print("")
                        pontos(mao_comp, mao_jogador)
                        break
                    print("")
                    print("**********************************")
                    print("")
                    print("Tu possuis {} a soma das cartas vale {}".format(str(mao_jogador), str(total(mao_jogador))))
                    print("")
                    escolha1 = input("Queres [P]edir ou [M]anter? ")
                    if escolha1 == "P" or escolha1 == "p":
                        pedir(mao_jogador)
                        if total(mao_jogador) > 21:
                            print("")
                            print("**********************************")
                            print("")
                            pontos(mao_comp, mao_jogador)
                            break
                        if total(mao_jogador) == 21:
                            print("")
                            print("**********************************")
                            print("")
                            pontos(mao_comp, mao_jogador)
                            break
                    if escolha1 == "M" or escolha1 == "m":
                        print("")
                        print("**********************************")
                        print("")
                        pontos(mao_comp, mao_jogador)
                        break
                jogar_denovo()
            if escolha == "M" or escolha == "m":
                while total(mao_comp) < 17:
                    pedir(mao_comp)
                print("")
                print("**********************************")
                print("")
                pontos(mao_comp, mao_jogador)


    print("******* Bem-vindo ao BlackJack *******")
    print("")
    tt = input("Queres assistir ao tutorial? S/N: ")
    while tt != "S" and tt != "s" and tt != "N" and tt != "n":
        print("")
        tt = input("Queres assistir ao tutorial? S/N: ")
    if tt == "S" or tt == "s":
        print("")
        print(
            "Este jogo consiste em gerar números aleatórios entre 1 e 11, em que cada número corresponde a uma carta do baralho convencional.")
        print("As cartas J, K, Q valem 10 e o A vale 1 ou 11.")
        print(
            "Cada jogador pode pedir várias cartas e o somatório dos valores dessas cartas não pode exceder o número 21")
        print("Cada jogador tem a possibilidade de não querer mais cartas")
        print(
            "Ganha o jogador que obtiver um somatório de 21 pontos ou que tenha o somatório abaixo de 21, mas mais alto do que o do adversário.")
    jogo()

elif p_j == "B" or p_j == "b":
    import random

    baralho = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4


    def distribuir(baralho):
        mao = []
        for eu in range(2):
            random.shuffle(baralho)
            carta = baralho.pop()
            if carta == 11:
                carta = "J"
            if carta == 12:
                carta = "Q"
            if carta == 13:
                carta = "K"
            if carta == 14:
                carta = "A"
            mao.append(carta)
        return mao


    def jogar_denovo():
        print("")
        jn = input("Deseja jogar outra vez? S/N: ")
        if jn == "S" or jn == "s":
            jogo()
        if jn == "N" or jn == "n":
            print("-------------------------------")
            print("Até à próxima!")
            exit()
        while jn != "s" and jn != "S" and jn != "n" and jn != "N":
            jn = input("Deseja jogar outra vez? S/N: ")
            if jn == "S" or jn == "s":
                jogo()
            if jn == "N" or jn == "n":
                print("-------------------------------")
                print("Até à próxima!")
                exit()


    def total(mao):
        total = 0
        for carta in mao:
            if carta == "J" or carta == "Q" or carta == "K":
                total = total + 10
            elif carta == "A":
                if total >= 11:
                    total = total + 1
                else:
                    total = total + 11
            else:
                total = total + carta
        return total


    def pedir(mao):
        carta = baralho.pop()
        if carta == 11:
            carta = "J"
        if carta == 12:
            carta = "Q"
        if carta == 13:
            carta = "K"
        if carta == 14:
            carta = "A"
        mao.append(carta)
        return mao


    def resultados(mao_jogador1, mao_jogador2):
        print("{} possuis {} a soma das cartas vale {}".format(j1, mao_jogador1, total(mao_jogador1)))
        print("{} possuis {} a soma das cartas dá {}".format(j2, mao_jogador2, total(mao_jogador2)))


    def blackjack(mao_jogador1, mao_jogador2):
        if total(mao_jogador1) == 21:
            print("************************")
            resultados(mao_jogador1, mao_jogador2)
            print("-------------------------------")
            print("Parabéns {}, ganhaste o Blackjack!".format(j1))
            jogar_denovo()
        if total(mao_jogador2) == 21:
            print("************************")
            resultados(mao_jogador1, mao_jogador2)
            print("-------------------------------")
            print("Parabéns {}, ganhaste o Blackjack!".format(j2))
            jogar_denovo()


    def pontos(mao_jogador1, mao_jogador2):
        if total(mao_jogador1) == 21:
            resultados(mao_jogador1, mao_jogador2)
            print("-------------------------------")
            print("Parabéns {}, ganhaste o Blackjack!".format(j1))
        if total(mao_jogador2) == 21:
            resultados(mao_jogador1, mao_jogador2)
            print("-------------------------------")
            print("Parabéns {}, ganhaste o Blackjack!".format(j2))
        if total(mao_jogador1) > 21:
            resultados(mao_jogador1, mao_jogador2)
            print("-------------------------------")
            print("Parabéns {}! Ganhaste o jogo porque {} rebentou o jogo".format(j2, j1))
        if total(mao_jogador2) > 21:
            resultados(mao_jogador1, mao_jogador2)
            print("-------------------------------")
            print("Parabéns {}! Ganhaste o jogo porque {} rebentou o jogo".format(j1, j2))
        if total(mao_jogador2) < total(mao_jogador1) and total(mao_jogador1) < 21 and total(mao_jogador2) < 21:
            resultados(mao_jogador1, mao_jogador2)
            print("-------------------------------")
            print("Parabéns {}, os teus pontos valem mais que os pontos de {}".format(j1, j2))
        if total(mao_jogador2) > total(mao_jogador1) and total(mao_jogador1) < 21 and total(mao_jogador2) < 21:
            resultados(mao_jogador1, mao_jogador2)
            print("-------------------------------")
            print("Parabéns {}, os teus pontos valem mais que os pontos de {}".format(j2, j1))
        if total(mao_jogador1) == total(mao_jogador2):
            resultados(mao_jogador1, mao_jogador2)
            print("-------------------------------")
            print("Empataram.")


    def jogo():
        escolha = "n"
        escolha1 = "n"
        escolha3 = "n"
        escolha4 = "n"
        print("")
        print("")
        print("******** Vamos Começar! *******")
        mao_jogador1 = distribuir(baralho)
        mao_jogador2 = distribuir(baralho)
        while escolha != "s":
            print(" ")
            print("{} possuis {} a soma das cartas vale {}".format(j1, str(mao_jogador1), str(total(mao_jogador1))))
            print(" ")
            print("{} possuis {} a soma das cartas vale {}".format(j2, str(mao_jogador2), str(total(mao_jogador2))))
            print("-------------------------------")
            blackjack(mao_jogador1, mao_jogador2)
            escolha = input("{} queres [P]edir ou [M]anter? ".format(j1))
            if escolha == "P" or escolha == "p":
                pedir(mao_jogador1)
                while escolha1 != "s":
                    if total(mao_jogador1) > 21:
                        print(" ")
                        print("***************************************")
                        print(" ")
                        pontos(mao_jogador1, mao_jogador2)
                        jogar_denovo()
                        break
                    print("")
                    print("***************************************")
                    print("")
                    print("{} possuis {} a soma das cartas vale {}".format(j1, str(mao_jogador1),
                                                                           str(total(mao_jogador1))))
                    print("-------------------------------")
                    escolha1 = input("{} queres [P]edir ou [M]anter? ".format(j1))
                    if escolha1 == "P" or escolha1 == "p":
                        pedir(mao_jogador1)
                        if total(mao_jogador1) > 21:
                            print("")
                            print("***************************************")
                            print("")
                            pontos(mao_jogador1, mao_jogador2)
                            jogar_denovo()
                            break
                        if total(mao_jogador1) == 21:
                            print("")
                            print("***************************************")
                            print("")
                            pontos(mao_jogador1, mao_jogador2)
                            jogar_denovo()
                            break
                    if escolha1 == "M" or escolha1 == "m":
                        print("")
                        print("***************************************")
                        print("")
                        break
            if escolha1 == "M" or escolha1 == "m":
                break
            if escolha == "M" or escolha == "m":
                print("")
                print("***************************************")
                print("")
                break
        while escolha3 != "s":
            print("{} possuis {} a soma das cartas vale {}".format(j1, str(mao_jogador1), str(total(mao_jogador1))))
            print("{} possuis {} a soma das cartas vale {}".format(j2, str(mao_jogador2), str(total(mao_jogador2))))
            print("-------------------------------")
            escolha3 = input("{} queres [P]edir ou [M]anter? ".format(j2))
            if escolha3 == "P" or escolha3 == "p":
                pedir(mao_jogador2)
                while escolha4 != "s":
                    if total(mao_jogador2) > 21:
                        print("")
                        print("***************************************")
                        print("")
                        pontos(mao_jogador1, mao_jogador2)
                        jogar_denovo()
                        break
                    print("")
                    print("***************************************")
                    print("")
                    print("{} possuis {} a soma das cartas vale {}".format(j2, str(mao_jogador2),
                                                                           str(total(mao_jogador2))))
                    print("-------------------------------")
                    escolha4 = input("{} queres [P]edir ou [M]anter? ".format(j2))
                    if escolha4 == "P" or escolha4 == "p":
                        pedir(mao_jogador2)
                        if total(mao_jogador2) > 21:
                            print("")
                            print("***************************************")
                            print("")
                            pontos(mao_jogador1, mao_jogador2)
                            jogar_denovo()
                            break
                        if total(mao_jogador2) == 21:
                            print("")
                            pontos(mao_jogador1, mao_jogador2)
                            jogar_denovo()
                            break
                    if escolha4 == "M" or escolha4 == "m":
                        print("")
                        print("***************************************")
                        print("")
                        pontos(mao_jogador1, mao_jogador2)
                        jogar_denovo()
                        break
            if escolha4 == "M" or escolha4 == "m":
                break
            if escolha3 == "M" or escolha3 == "m":
                print("")
                print("***************************************")
                print("")
                pontos(mao_jogador1, mao_jogador2)
                jogar_denovo()
            break


    print("******* Bem-vindo ao BlackJack *******")
    print("")
    tt = input("Queres assistir ao tutorial? S/N: ")
    while tt != "n" and tt != "N" and tt != "s" and tt != "S":
        tt = input("Queres assistir ao tutorial? S/N: ")

    if tt == "S" or tt == "s":
        print("")
        print(
            "Este jogo consiste em gerar números aleatórios entre 1 e 11, em que cada número corresponde a uma carta do baralho convencional.")
        print("As cartas J, K, Q valem 10 e o A vale 1 ou 11.")
        print(
            "Cada jogador pode pedir várias cartas e o somatório dos valores dessas cartas não pode exceder o número 21")
        print("Cada jogador tem a possibilidade de não querer mais cartas")
        print(
            "Ganha o jogador que obtiver um somatório de 21 pontos ou que tenha o somatório abaixo de 21, mas mais alto do que o do adversário.")
        print("")
        print("")
    j1 = input("Jogador 1, insira o seu nome: ")
    print("--------------------------------------")
    j2 = input("Jogador 2, insira o seu nome: ")
    jogo()

elif p_j == "NM" or p_j == "nm":
    import random


    def jogardenovo():
        denovo = input("Queres jogar outravez? S/N? ")
        if denovo == "S" or denovo == "s":
            jogo()
        if denovo == "N" or denovo == "n":
            print("Até à próxima!")
            exit()
        while denovo != "S" and denovo != "s" and denovo != "N" and denovo != "n":
            print("")
            denovo = input("Queres jogar outravez? S/N? ")
            if denovo == "S" or denovo == "s":
                jogo()
            if denovo == "N" or denovo == "n":
                print("Até à próxima!")
                exit()


    def jogo():
        ptc = 0
        tnt = 0
        nvl = int(input("Que nível queres jogar? (1,2,3): "))
        if nvl == 1:
            print("")
            print("")
            print("*************** Nível 1 ***************")
            print("")
            nm = random.randint(1, 40)
            pista = input("Queres ter direito a pistas durante o jogo? S/N: ")
            if pista == "S" or pista == "s":
                n1 = nm - random.randint(0, 15)
                n2 = nm + random.randint(0, 15)
                if n1 < 1:
                    n3 = 1
                else:
                    n3 = n1
                if n2 > 40:
                    n4 = 40
                else:
                    n4 = n2
                print("")
                print("O número mágico está entre {} e {}.".format(n3, n4))
            while tnt != nm:
                print("")
                tnt = int(input("Número: "))
                ptc = ptc + 1
                if tnt < nm and pista == "S" or tnt < nm and pista == "s":
                    print("O número mágico é maior do que o número que tentaste.")
                if tnt > nm and pista == "S" or tnt > nm and pista == "s":
                    print("O número mágico é menor do que o número que tentaste.")
                if tnt != nm and pista != "S" and pista != "s":
                    print("Errado")
        elif nvl == 2:
            print("")
            print("")
            print("*************** Nível 2 ***************")
            print("")
            nm = random.randint(1, 352)
            pista = input("Queres ter direito a pistas durante o jogo? S/N: ")
            if pista == "S" or pista == "s":
                n1 = nm - random.randint(0, 35)
                n2 = nm + random.randint(0, 35)
                if n1 < 1:
                    n3 = 1
                else:
                    n3 = n1
                if n2 > 352:
                    n4 = 352
                else:
                    n4 = n2
                print("")
                print("O número mágico está entre {} e {}.".format(n3, n4))
            while tnt != nm:
                print("")
                tnt = int(input("Número: "))
                ptc = ptc + 1
                if tnt < nm and pista == "S" or tnt < nm and pista == "s":
                    print("O número mágico é maior do que o número que tentaste.")
                if tnt > nm and pista == "S" or tnt > nm and pista == "s":
                    print("O número mágico é menor do que o número que tentaste.")
                if tnt != nm and pista != "S" and pista != "s":
                    print("Errado")
        elif nvl == 3:
            print("")
            print("")
            print("*************** Nível 3 ***************")
            print("")
            nm = random.randint(1, 999)
            pista = input("Queres ter direito a pistas durante o jogo? S/N: ")
            if pista == "S" or pista == "s":
                n1 = nm - random.randint(0, 100)
                n2 = nm + random.randint(0, 100)
                if n1 < 1:
                    n3 = 1
                else:
                    n3 = n1
                if n2 > 999:
                    n4 = 999
                else:
                    n4 = n2
                print("")
                print("O número mágico está entre {} e {}.".format(n3, n4))
            while tnt != nm:
                print("")
                tnt = int(input("Número: "))
                ptc = ptc + 1
                if tnt < nm and pista == "S" or tnt < nm and pista == "s":
                    print("O número mágico é maior do que o número que tentaste.")
                if tnt > nm and pista == "S" or tnt > nm and pista == "s":
                    print("O número mágico é menor do que o número que tentaste.")
                if tnt != nm and pista != "S" and pista != "s":
                    print("Errado")
        else:
            print("")
            print("Caratér inválido")
        if ptc < 4 and ptc > 0:
            print("")
            print("Superestrela!!!")
        elif ptc < 7 and ptc > 3:
            print("")
            print("Ainda andas um bocadinho longe.")
        elif ptc < 11 and ptc > 6:
            print("")
            print("Continua assim que a tua pontuação vai parar ás piores!")
        elif ptc > 10:
            print("")
            print("Uma das piores de sempre!!!")
        else:
            print("Erro")
            print("")
        jogardenovo()


    print("********   Bem-Vindo ao jogo do Número Mágico   ************")
    print("")
    tt = str(input("Queres assistir ao tutorial? S/N: "))
    print("")
    while tt != "S" and tt != "s" and tt != "N" and tt != "n":
        tt = str(input("Queres assistir ao tutorial? S/N: "))
        print("")
    if tt == "S" or tt == "s":
        print(
            "Neste jogo, vamos escolher um número aleatório (Número Mágico) e o teu objetivo como jogador é encontrá-lo.")
        print(
            "Podes escolher entre 3 níveis diferentes de dificuldade, sendo que quanto maior o nível mais difícil o jogo se vai tornar.")
        print("No nível 1, vamos escolher um número de 1 a 40.")
        print("No nível 2, de 1 a 352.")
        print("E no nível 3, de 1 a 999.")
        print("")
        print("")
    jogo()

else:
    print("")
    print("Caractér Inválido")
    print("")
