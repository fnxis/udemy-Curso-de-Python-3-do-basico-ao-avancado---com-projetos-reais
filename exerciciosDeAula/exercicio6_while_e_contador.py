         # 0123456789    
nome='Guilherme Porto'
contador=0
tamanho_nome=len(nome)
nome_novo=' '
while contador <=tamanho_nome-1:
    print(nome[contador],'*')
   
    nome_novo+=nome[contador]
    contador+=1
   
print(nome_novo)   


