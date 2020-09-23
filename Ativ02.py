#Elabore um código em Python para calcular a média aritmética de 2 números inteiros;
nota_1 = float(input("Entre com a sua nota P1: "))
nota_2 = float(input("Entre com a sua nota P2: "))
media = (nota_1 + nota_2) / 2
if(media < 60):
    print("\nA sua média: ", media)
    print("\nVocê não foi aprovado.")
else:
    print("\nA sua média: ", media)
    print("Você foi aprovado.")

