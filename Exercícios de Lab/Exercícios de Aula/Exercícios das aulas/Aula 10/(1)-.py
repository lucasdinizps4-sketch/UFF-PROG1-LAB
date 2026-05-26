coord = [(1,3),(4.5,8),(7.2,1.1)]
lat = float(input("Informe latitude"))
lon = float(input("Informe longitude"))
nova_coord = (lat,lon)

if nova_coord in coord:
    print("Local registrado")

else:
    coord.append(nova_coord)
    print("Novo local adicionado")