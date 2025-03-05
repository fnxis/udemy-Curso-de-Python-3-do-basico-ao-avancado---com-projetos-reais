"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numeroInteiro=(input('Digite seu numero aqui:'))
try:    
        if int(numeroInteiro) %2 ==0:
            print('seu numero é par')
        elif int(numeroInteiro) %2 ==1:
            print('Seu numero é impar')
except ValueError:
        print('Digite um numero inteiro')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

nome=input('Digite seu nome:')
horario=input('Digite o horario:')

try:
    if int(horario) >=0 and int(horario)<=11:
          print(f'Bom dia {nome}')
    if int(horario) >=12 and int(horario)<=17:
          print(f'Boa tarde {nome}')
    if int(horario) >=18 and int(horario)<=23:
          print(f'Boa noite {nome}')
    else:
          print('digite um horario valido.')
except ValueError:
        print('digite um horario valido')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome=input('Digite seu nome:')
nomeSeparado=len(nome)

if nomeSeparado >2:
    if nomeSeparado <=4:
        print('Seu nome é curto')
    elif nomeSeparado >4 and  nomeSeparado<=6:
        print('Seu nome é normal')
    elif nomeSeparado >=7:
        print('Seu nome é muito grande')
else:
     print('Digite um nome valido')        