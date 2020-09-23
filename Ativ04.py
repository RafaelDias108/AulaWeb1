#Elabore um código em Python para receber do usuário:
#▪ Nome do aluno;
#▪ 03 notas;
#▪ Retorne uma mensagem para o usuário informando a média aritmética desse aluno;
nome_aluno = input("Entre com seu nome: ")
nota_01 = float(input("Entre com a P1: "))
nota_02 = float(input("Entre com a P2: "))
nota_03 = float(input("Entre com a PF: "))
media = (nota_01 + nota_02 + nota_03)/3
print("A média do aluno ",nome_aluno," é: ",media)