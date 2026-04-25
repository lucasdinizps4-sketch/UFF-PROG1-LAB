# Escreva um programa que tenha uma senha secreta armazenada em uma variável (ex: senha_secreta = "programar"). O programa deve solicitar que o usuário digite uma senha e,
# em seguida, imprimir na tela o resultado Booleano (True ou False) da comparação que verifica se a senha digitada é exatamente igual à senha secreta

senha_secreta = "abc24"
senha = input("Informe a senha: ")

print(senha==senha_secreta)