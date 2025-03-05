nome=input('digite seu Nome: ')
idade=input('digite sua idade: ')
nomeInvertido=nome[::-1]
espaco= ' 'in nome
letras=len(nome)
primeiraLetra=nome[0]
ultimaLetra=nome[-1]

if nome and idade:
        print(f"Seu nome é {nome}.")
        print(f'Seu nome invertido é {nomeInvertido}.')
        print(f'Seu nome contem {letras} letras.')
        print(f'A primeira letra do seu nome é {primeiraLetra}.')
        print(f'a ultima letra do seu nome é {ultimaLetra}.')
        if espaco:
                print('Seu nome contem espaço.')
        else:
                print('Seu nome não contem espaço.')                


else:
        print("Desculpe,voçê deixou campos vazios.")
