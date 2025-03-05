import os
palavraSecreta='paralelepipedo'
palavraOculta=''
tentativas=0
valoresInteiros=['0','1','2','3','4','5','6','7','8','9']
while True:
    letra=input('Digite uma letra para descobrir a frase secreta: ')
    if letra in valoresInteiros:
        print('Digite uma letra!')
        continue

    if len(letra)>1:
        print('digite apenas uma letra')
        continue
    tentativas+=1
    if letra in palavraSecreta:
        palavraOculta+=letra


    palavraFormada=''

    for letraSecreta in palavraSecreta:
        if letraSecreta in palavraOculta:
            palavraFormada+=letraSecreta
        else:
            palavraFormada+='*'
    os.system('cls')
    if palavraFormada== palavraSecreta:
        print("Parabens!! voçê acertou a palavra secreta")
        print('palavra secreta: ',palavraSecreta)
        print(f'voce usou {tentativas} tentativas')
        saida=input('clique qualquer telca para sair.')
        break

    print(palavraFormada)


