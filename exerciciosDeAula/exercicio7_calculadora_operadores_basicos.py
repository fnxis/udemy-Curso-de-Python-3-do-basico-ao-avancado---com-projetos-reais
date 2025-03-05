while True:
    numero_1=input('digite um numero: ')
    numero_2=input('digite outro numero: ')
    operador=input('digite o operador (+-/*): ')

    numeros_validos=None
    operadores_permitidos='+-/*'
    num1_float=0
    num2_float=0

    try:
        num1_float=float(numero_1)
        num2_float=float(numero_2)
        numeros_validos=True        
    except:
        numeros_validos=False 
     
    if numeros_validos is None:
        print('Numero digitado invalido')
        continue   
    
    if operador not in operadores_permitidos:
        print('digite um operador valido')
        continue
    if len(operador)>1:
        print("digite apenas um operador")
        continue
    
    if operador == '+':
        print(f'{num1_float}+{num2_float}={num2_float+num1_float}')
    elif operador == '-':
        print(f'{num1_float}-{num2_float}={num2_float-num1_float}')
    elif operador == '/':
        print(f'{num1_float}/{num2_float}={num2_float/num1_float}')
    elif operador == '*':
        print(f'{num1_float}*{num2_float}={num2_float*num1_float}')






    sair=input('quer sair? [s]im:').lower().startswith('s')

    if sair is True:
        break