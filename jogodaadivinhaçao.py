from random import randint

jogo = randint(1,100)

print ("Olá, bem vindo ao jogo da adivinhação")
print ("Tente acetar um número entre 1 e 100")
print ("Boa Sorte!!!")

acertou = False
tentativas = 0


while not acertou:
    participante = int(input("Escolha um número"))
    tentativas += 1
    if participante == jogo:
        acertou = True
    else:
            if participante < jogo:
                print ("Que pena você errou, tente MAIS ALTO!")
            elif participante > jogo:
                print ("Que pena você errou, tente MAIS BAIXO!")

print ("PARABÉNS VOCÊ ACERTOU!!!")
print ("Só teve que tentar {} vezes!".format(tentativas))

