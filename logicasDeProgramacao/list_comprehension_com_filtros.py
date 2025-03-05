import pprint
def printis(valor):
    pprint.pprint(valor,sort_dicts=False,width=50)
# lista= []
# def listinha():
#     for numero in range(10):
#         lista.append(numero)
#         if numero==0:
#             lista.pop(0)

# listinha()
    
# print(lista)

lista = [numero * 2 for numero in range(10)]
# print(list(range(10)))
# print(lista)

# Mapeamento de dados em list comprehension
# lista=[n for n in range(10) if n <5]
produtos = [
    {'nome': 'alface', 'preco': 20, },
    {'nome': 'beterraba', 'preco': 10, },
    {'nome': 'pepino', 'preco': 30, },
]
novos_produtos=[
    {**produto,"preco": produto["preco"]*1.05}
    if produto['preco']>=20 else{**produto}
    for produto in produtos 
    if produto['preco']>10
    ]
print(*novos_produtos,sep='\n')

