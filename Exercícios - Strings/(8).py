n = input("Informe 9 algarismos: ")
if range(len(n)) == 9:
    soma1 = 0
    soma2 = 0
    p_dv1 = 10
    p_dv2 = 11

    for i in range(n):
        soma1 += int(n[i]) * p_dv1
        p_dv1 -= 1
        soma2 += int(n[i]) * p_dv2
    resto1 = (soma1*10)%11
    if resto1 == 10:
        div1 = 0
    else: 
        div1 = resto1
    soma2 = (soma2 + div1*2)*10
    resto2 = soma2%11

    if resto2 == 10:
        div2 = 0
    else:
        div2 = resto2

    n_controle = div1*10+div2
    
    cpf = n + "-" + str(n_controle)