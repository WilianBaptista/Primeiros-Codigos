from random import randint
import time
computador = randint(0, 5)
print('~^~' * 20)
print('\033[1;44m Estou pensando em um número de 0 a 5. Tente descobrir qual é... \033[m')
print('~^~' * 20)
jogador = int(input('Em que número estou pensando? '))
print('\033[1;40mPROCESSANDO...')
time.sleep(2)
if jogador == computador:
    print('\033[m \033[7;1;44m Parabéns, você acertou !! \033[mO número pensado foi {}'.format(computador))
else:
    print('\033[1;31;40m Você errou!! \033[m O número pensado foi {}'.format(computador))
