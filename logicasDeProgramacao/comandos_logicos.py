#sep -->é o separador que o interpretador usara no lugar do espaço
#end -->é oque ira sair no final do meu print, que por padrao é o \n
pass #pode ser usado para colocar o valor da variavel para colocar posteriormente
... #pode ser usado para colocar o valor da variavel para colocar posteriormente

print(1, 2, sep="-", end="##") 
print(3, 4, sep="-",end ="\n##") 
print(5, 6, sep="-", end="\n") 

# Escape
print("Ana \"Beatriz\"")
print('Ana "Beatriz"')

# r
print(r"Ana \"Beatriz\"")

#type
print(type("Porto"))
print(type(1))
print(type(1.1),type(-1.1),type(0.0))

# sim (True) ou não (False).
print(10 == 10)  # Sim => True (Verdadeiro)
print(10 == 11)  # Não => False (Falso)
print(type(True))  #bool
print(type(False)) #bool
print(type(10 == 10)) #bool
print(type(10 == 11)) #bool

adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

#f-strings é usado pra delimitar quantas casas decimais tera a saida
divisao = 10 / 3  # float
print(f"a divisao é {divisao:.2f}")
divisao = 10 / 3  # float
print('Divisão', divisao)

divisao_inteira = 10 // 3
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)

concatenacao = 'Guilherme' + ' ' + 'Porto'
print(concatenacao)

a_dez_vezes = 'G' * 10
tres_vezes_Ana = 3 * 'Ana'
print(a_dez_vezes)
print(tres_vezes_Ana)