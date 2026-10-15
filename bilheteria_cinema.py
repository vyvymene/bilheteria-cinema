nome = input("Informe seu nome: ")
idade = int(input("Informe a sua idade: "))
print("Você tem documento: (Sim/Não): ")
resposta = input() 

if idade >= 18 and resposta == "sim":
   print(nome, "Entrada permitida! ")
else:
   print(nome, "Entrada não permitida! ")    