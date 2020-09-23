# Elabore um script em Python para executar o cálculo da equação do segundo grau
# ▪ Sem biblioteca math;

def raizes(a,b,c):
    delta = (b**2 - 4*a*c)

    x1 = -b + (delta**(1/2)) / 2*a
    x2 = -b - (delta**(1/2)) / 2*a
    print("\nValor de x1: {0}".format(x1))
    print("\nValor de x2: {0}".format(x2))

print('\nCalculando as raízes de uma equação de 2º grau\n')
a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))
raizes(a,b,c)    