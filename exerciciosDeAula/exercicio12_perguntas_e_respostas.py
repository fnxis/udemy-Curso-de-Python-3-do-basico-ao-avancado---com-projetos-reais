perguntas= [
    {
    "pergunta": "Quanto é 2+2?",
    "opcoes": ['1','3','4','5'],
    "resposta": '4',
    },
    {
    "pergunta": "Quanto é 5*5?",
    "opcoes": ['25','55','10','51'],
    "resposta": '25',
    },
    {
    "pergunta": "Quanto é 10/2?",
    "opcoes": ['4','5','6','7'],
    "resposta": '5',
    },
]
acertos=0
for pergunta in perguntas:
    print(pergunta['pergunta'])
    print()
    
    for i,opcoes in enumerate(pergunta['opcoes']):
        print(f"{i})",opcoes)
    print()
    
    escolha= input("Escolha uma opção: ")
    print()

    escolha_int= None
    if escolha.isdigit():
        escolha_int= int(escolha)
    
    if escolha_int is not None:
        if escolha_int>=0 and escolha_int<len(pergunta['opcoes']):
            if pergunta['opcoes'][escolha_int] == pergunta["resposta"]:
                print("VOCÊ ACERTOU!")
                acertos += 1
            else:
                print("VOCÊ ERROU!")
        else:
            print("Digite um numero")
        print()
    
print(f"VOCÊ ACERTOU {acertos} PERGUNTAS")



