nome = input("Informe seu nome: ")
idade = int(input("Informe a sua idade: "))
resposta = input("Você tem documento: (Sim/Não): ") 

if idade >= 18 and resposta == "sim":
   print(nome, "Entrada permitida! ")
else:
   print(nome, "Entrada não permitida! ")    