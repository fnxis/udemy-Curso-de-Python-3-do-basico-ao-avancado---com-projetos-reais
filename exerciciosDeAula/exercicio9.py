import os
palavraSecreta='voleibol'
palavraOculta=''
tentativas=0
while True:
    letra=input('Digite uma letra para descobrir a frase secreta: ')
    if letra =='0' or letra =='1' or letra =='2' or letra =='3' or letra =='4' or letra =='5' or letra =='6' or letra =='7' or letra =='8' or letra =='9':
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


