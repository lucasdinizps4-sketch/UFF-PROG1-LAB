# A nota final de um estudante é calculada a partir de três notas atribuídas, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três notas mencionadas obedece aos pesos
# a seguir:

# Trabalho de lab (peso 2)
# Avaliação semestral (peso 3)
# Exame final (peso 5)

# Faça um programa que receba as três notas, calcule e mostre a média ponderada e o conceito que segue a tabela:
# Media maior ou igusl que 8 e maior ou igual que 10 (Conceito A)
# Media maior ou igual que 7 e menor que 8 (Conceito B)
# Media maior ou igual 6 e menor que 7 (Conceito C)
# Media maior ou igual 5 e menor que 6 (Conceito D)
# Media maior ou igual 0 e menor que 5 (Conceito E)

trabalho_lab = float(input("Informe sua nota de lab: ")) * 2
avaliacao_s = float(input("Informe sua nota da avaliação semestral: ")) * 3
exame_f = float(input("Informe sua nota do exame final: ")) * 5

media_p = (trabalho_lab + avaliacao_s + exame_f) / 10

if media_p >= 8 and media_p == 10:
    conceito = "A"

elif media_p >= 7 and media_p < 8:
    conceito = "B"

elif media_p >= 6 and media_p < 7:
    conceito = "C" 

elif media_p >= 5 and media_p < 6:
    conceito = "D"
    
else:
    conceito = "E"

print(f"Sua média foi {media_p} e conceito {conceito}")