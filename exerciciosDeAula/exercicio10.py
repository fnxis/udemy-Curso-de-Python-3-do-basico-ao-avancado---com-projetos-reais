def mult(*args):
    result=1 
    for number in args:
        result*=number
    return result
multplication=mult(1,4,5,7,2)  
print(multplication)

def par_impar(numero):
    return numero % 2 == 0

print(par_impar(245))
print(par_impar(2444))