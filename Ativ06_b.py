# Elabore um script em Python para executar o cálculo da equação do segundo grau
# ▪ Com biblioteca math:
# ▪ import math;
# ▪ >>> math.sqrt(9)
# ▪ >>> 3
import math
def raizes(a,b,c):
    delta = (b**2 - 4*a*c)
    h = math.sqrt(delta)
    x1 = (-b + h) / 2*a
    x2 = (-b - h) / 2*a
    print("\nValor de x1: {0}".format(x1))
    print("\nValor de x2: {0}".format(x2))

print('\nCalculando as raízes de uma equação de 2º grau\n')
a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))
raizes(a,b,c)  