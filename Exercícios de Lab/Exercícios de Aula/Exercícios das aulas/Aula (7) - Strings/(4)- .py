
texto = input("Digite o texto")
hu = ""

for i in texto: 
    if texto[i].isupper():
        hu += texto[i]

print(hu)


