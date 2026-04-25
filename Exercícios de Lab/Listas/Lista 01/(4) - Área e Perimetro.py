# Construa um programa para calcular a área e o perímetro do círculo.
# Exemplo de saída: “Área = xx.xx m2, Perímetro = xx.xx m.”

r = float(input("Informe raio: "))
d = 2*r
pi = 3.14

area = pi*(r**2)
perimetro = pi*d

print(f"\nÁrea = {area} m2 \nPerimetro = {perimetro} m")
