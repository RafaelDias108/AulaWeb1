media_bio = float(input("Entre com a media da matéria Biologia: "))
peso_bio = 3
media_mat = float(input("Entre com a media da matéria Matemática: "))
peso_mat = 9
media_port = float(input("Entre com a media da matéria Portuguêss: "))
peso_port = 6
media_ing = float(input("Entre com a media da matéria Inglês: "))
peso_ing = 5
med_pond = ((media_bio*peso_bio)+(media_mat*peso_mat)+(media_port*peso_port)+(media_ing*peso_ing))/(peso_bio+peso_mat+peso_port+peso_ing)
print("A média Ponderada das notas é: ",med_pond)