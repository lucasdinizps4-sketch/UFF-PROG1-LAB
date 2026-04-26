senha_verdadeira = "abcd"
senha = ""

while senha != senha_verdadeira:
    senha = input("Informe a senha: ")
    if senha != senha_verdadeira: 
        print("Senha errada!")

print("Logado!")