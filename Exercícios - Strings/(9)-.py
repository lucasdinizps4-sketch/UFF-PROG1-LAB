data = input("Informe uma data no formato (dd/mm/aaaa): ")

if len(data) == 10:
    if data[2] != "/" or data[5] != "/":
        print("Formato incorreto")
    else:
        dia = data[0:2]
        mes = data[3:5]
        ano = data[6:9]

        if mes < 1 or mes > 12:
            print("Formato de meses está incorreto")
        else:
            if mes == 2:
                if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                    dia_mes = 29
                else:
                    dia_mes = 28
            elif mes == 4 or mes == 6 or mes ==9 or mes == 11:
                dia_mes = 30
            else:
                dia_mes = 31
        if dia < 1 or dia > dia_mes:
            print("Formato de dias está incorreto")
        else:
            print("Data válida!")
else:
    print("Formato de ")