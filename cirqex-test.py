#!/usr/bin/python3

from cirquex import suscribir
import time
# Prueba para clase suscribir
usuario = suscribir()
usuario.precio = float(input('\nIngrese precio: '))
usuario.identificar = 'familia'
usuario.usuarios = 3
# Doble del precio
usuario.duplicar()
usuario.duplicar()
usuario.dividir()
# Muestro datos
print(f'\nsuscripcion\n\n\tPrecio: {usuario.precio.__str__()}\n\tUsuario: {usuario.identificar.__str__()}\n\tTotal: {usuario.usuarios.__str__()} usuarios.\n')
# Prueba para clase circuito financiero
personas = [usuario]

for agregado in range(1, 5):
    objeto = suscribir()
    objeto.usuarios = 4
    objeto.precio = (objeto.usuarios / usuario.precio)
    personas.append(objeto)

from cirquex import circuito_financiero

caminos = circuito_financiero()
caminos.costo = 5
for objeto in personas:
    caminos.agregar_usuario(objeto)
    print(f'\nsuscripcion\n\n\tPrecio: {objeto.precio.__str__()}.\n')
    print(f'\tEl costo es de ${caminos.costo.__str__()} y el ingreso de ${caminos.ingreso.__str__()}\n\nTotal: {caminos.suscriptos[0].usuarios.__str__()} usuarios.\n')
    time.sleep(1)
caminos.quitar_usuario(usuario)
for objeto in caminos.suscriptos:
    print(f'\nsuscripcion\n\n\tPrecio: {objeto.precio.__str__()}\n')
    print(f'\tEl costo es de ${caminos.costo.__str__()} y el ingreso de ${caminos.ingreso.__str__()}\n\nTotal: {caminos.suscriptos[0].usuarios.__str__()} usuarios.\n')
    time.sleep(1)

print(f'\tEl costo es de ${caminos.costo.__str__()} y el ingreso de ${caminos.ingreso.__str__()}\n\nTotal: {caminos.suscriptos[0].usuarios.__str__()} usuarios.\n')
