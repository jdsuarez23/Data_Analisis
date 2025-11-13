#variables en listas

vendedores = ['juan', 'pedro', 'maria']
print(vendedores)
vendedores[1] = 'carlos'
print(vendedores)

meses = []
ventas = []

cantidad_meses = int(input("ingrese la cantidad de meses a registrar: "))

for i in range(cantidad_meses):
    mes = input("ingrese el nombre del mes: ")
    venta = float(input(f"ingrese el total  de ventas del [{mes}: "))
    meses.append(mes)
    ventas.append(venta)

n = len(meses)

print('\nRegistro de Ventas Mensuales')
for i in range(n):
    print(f'{meses[i]}: ${ventas[i]:,.2f}')    #el .2f es para que muestre 2 decimales


