import random, time
print('Jogo de Advinhação')
joga = int(input('''Jogar?
1- Sim
2- Não\n'''))
tentativa = 3
while(joga == 1):	
	modo = int(input('''Escolha o modo
1- Facil
2- Normal
3- Dificil\n'''))

	if(modo == 1):
		numero_secreto = random.randint(0,10)
		while tentativa > 0:
			chute = int(input('Chute um numero de 0 a 10:\n'))
			if chute > 10: print('''\nNumero que você digitou é maior que o numero maximo do modo
Assim você não vai acerta nunca, seu babaca
Digite um numero entre 0 e 10\n''')
			print('Comparando os numeros...')
			time.sleep(1)
			acertou = chute == numero_secreto
			maior = chute > numero_secreto
			menor = chute < numero_secreto
			if(acertou):
				print('Acertou mizeravi')
				break
			elif(maior):
				print('Errou Otario! Seu chute foi maior que o numero secreto')
			elif(menor):
				print('Errou Otario! Seu chute foi menor que o numero secreto')
			tentativa -= 1
			print('Você tem {} tentativa(s)'.format(tentativa))
	elif(modo == 2):
		numero_secreto = random.randint(0,40)
		while tentativa > 0:
			chute = int(input('Chute um numero de 0 a 40:\n'))
			if chute > 40: print('''\nNumero que você digitou é maior que o numero maximo do modo
Assim você não vai acerta nunca, seu babaca
Digite um numero entre 0 e 40\n''')
			print('Comparando os numeros...')
			time.sleep(1)
			acertou = chute == numero_secreto
			maior = chute > numero_secreto     
			menor = chute < numero_secreto

			if(acertou):
			    print('Acertou mizeravi')
			    break
			elif(maior):
			    print('Errou Otario! Seu chute foi maior que o numero secreto')
			elif(menor):
			    print('Errou Otario! Seu chute foi menor que o numero secreto')
			tentativa -= 1
			print('Você tem {} tentativa(s)'.format(tentativa))
	elif(modo == 3):
		numero_secreto = random.randint(0,100)
		print('Duvido você acerta!!')
		while tentativa > 0:
			chute = int(input('Chute um numero de 0 a 100:\n'))
			if chute > 100: print('''\nNumero que você digitou é maior que o numero maximo do modo
Assim você não vai acerta nunca, seu babaca
Digite um numero entre 0 e 100\n''')
			print('Comparando os numeros...')
			time.sleep(1)
			acertou = chute == numero_secreto
			maior = chute > numero_secreto 
			menor = chute < numero_secreto

			if(acertou):
			    print('Acertou mizeravi')
			    break
			elif(maior):
			    print('Errou Otario! Seu chute foi maior que o numero secreto')
			elif(menor):
			    print('Errou Otario! Seu chute foi menor que o numero secreto')
			tentativa -= 1
			print('Você tem {} tentativa(s)'.format(tentativa))
     

    
	joga = int(input('''Jogar novamente?
1- Sim
2- Não\n'''))
	tentativa = 3
