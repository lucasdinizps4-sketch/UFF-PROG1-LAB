def adicional_hora_extra(salario,hora_extra):
    valor_hora = salario/170
    adicional = valor_hora * hora_extra * 0.5
    return adicional

def desconto_inss(valor_total):
    desconto = valor_total * 0.10
    if desconto > 150:
        desconto = 150
    return desconto