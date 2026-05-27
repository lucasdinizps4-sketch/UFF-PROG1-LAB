s = input("Informe 10 digitos: ")
if len(s) == 10:
    soma = 0
    pesos = "3298765432"
    for i in range(len(s)):
        soma += int(s[i])*int(pesos[i])
    resto = (soma % 11)-11
    if resto == 10 or resto == 11:
        digito = 0
    else:
        digito = resto
    pis_pasep = s + "-" + str(digito)
    print(f"PIS/PASEP: {pis_pasep}")