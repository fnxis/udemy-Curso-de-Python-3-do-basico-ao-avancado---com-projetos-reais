def mult(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar=(mult(2))
triplicar=(mult(3))
quadriplicar=(mult(4))
quintuplicar=(mult(5))
sextuplicar=(mult(6))
septuplicar=(mult(7))
oito=(mult(7))
noveplicar=(mult(9))
dez=(mult(10))
onze=(mult(11))
doze=(mult(12))
treze=(mult(13))

print(duplicar(2740))
print(triplicar(2740))
print(quadriplicar(2740))
print(quintuplicar(2740))
print(sextuplicar(2740))
print(septuplicar(2740))
print(oito(2740))
print(noveplicar(2740))
print(dez(2740))
print(onze(2740))
print(doze(2740))
print(treze(2740))