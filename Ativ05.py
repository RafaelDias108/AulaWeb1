# Elabore um código em Python para receber do usuário:
# ▪ Nome do aluno;
# ▪ 02 notas;
# ▪ 02 pesos, respectivamente para cada nota;
# ▪ Retorne uma mensagem para o usuário informando a média ponderada desse aluno;
# ▪ Utilize o método split para separar a entrada do usuário em nota e peso. Exemplo: Digite a nota e peso: 9.5,3

nome_aluno = input("Entre com seu nome: ")
nota_01,peso_01 = input("Entre com a nota P1 e o peso: ").split(",",2)
nota_02, peso_02= input("Entre com a nota P2 e o peso: ").split(",",2)
p1 = int(nota_01)
p2 = int(nota_02)
peso1 = int(peso_01)
peso2 = int(peso_02)
media_pond = ((p1*peso1)+(p2*peso2))/(peso1+peso2)
print("A média Ponderado do aluno ",nome_aluno," é: ",media_pond)