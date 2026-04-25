# Construa um programa que solicite a idade de um usuário e imprima na tela o valor Booleano (True ou False) que responde à pergunta: "A idade informada é maior ou igual a 18?".

idade = int(input("Informe sua idade: "))

if idade >= 18: 
    verificacao = True
    print(verificacao)
else:
    verificacao = False
    print(verificacao)

# Outro modo

idade = int(input("Informe sua idade: "))
print(idade>=18)