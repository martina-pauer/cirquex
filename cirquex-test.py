#!/usr/bin/python3

from cirquex import suscribir

import time
# Prueba para clase suscribir
usuario = suscribir()
usuario.precio = float(input('\nIngrese precio: '))
usuario.identificar = 'familia'
usuario.usuarios = 3
# Muestro datos
print(f'\nsuscripcion\n\n\tPrecio: {usuario.precio.__str__()}\n\tUsuario: {usuario.identificar.__str__()}\n\tTotal: {usuario.usuarios.__str__()} usuarios.\n')
# Prueba para clase circuito financiero
personas = [usuario]

for agregado in range(1, 5):

    suscripto = suscribir()

    suscripto.usuarios = 4

    suscripto.precio = (usuario.precio / suscripto.usuarios)

    personas.append(suscripto)

from cirquex import circuito_financiero

def mostrar_circuito(circuito_mostrado : circuito_financiero):

    if circuito_mostrado.ingreso >= 0:

        print(f'\tEl costo es de ${circuito_mostrado.costo.__str__()} y el ingreso de ${circuito_mostrado.ingreso.__str__()}\n\nTotal: {circuito_mostrado.suscriptos[0].usuarios.__str__()} usuarios.\n')
    else:
        print(f'Hay perdidas a precio ${circuito_mostrado.suscriptos[0].precio} con {circuito_mostrado.suscriptos[0].usuarios} usuarios.')

caminos = circuito_financiero()

caminos.costo = 5

segundos = 1

for persona in personas:

    caminos.agregar_usuario(persona)

    print(f'\nsuscripcion\n\n\tPrecio: {persona.precio.__str__()}.\n')

    mostrar_circuito(caminos)

    time.sleep(segundos)

caminos.quitar_usuario(usuario)

for objeto in caminos.suscriptos:

    print(f'\nsuscripcion\n\n\tPrecio: {persona.precio.__str__()}\n')
    mostrar_circuito(caminos)
    time.sleep(segundos)

mostrar_circuito(caminos)
