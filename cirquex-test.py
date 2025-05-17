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
    objeto = suscribir()
    objeto.usuarios = 4
<<<<<<< HEAD
    objeto.precio = (objeto.precio / objeto.usuarios)
=======
>>>>>>> 5b33f4d (Sigue mejorando)
    personas.append(objeto)

from cirquex import circuito_financiero

def mostrar_circuito(objeto : circuito_financiero):
    if objeto.ingreso >= 0:
        print(f'\tEl costo es de ${objeto.costo.__str__()} y el ingreso de ${objeto.ingreso.__str__()}\n\nTotal: {objeto.suscriptos[0].usuarios.__str__()} usuarios.\n')
    else:
        print(f'Hay perdidas a precio ${objeto.suscriptos[0].precio} con {objeto.suscriptos[0].usuarios} usuarios.')    

caminos = circuito_financiero()
caminos.costo = 5

segundos = 3
for objeto in personas:
    caminos.agregar_usuario(objeto)
    print(f'\nsuscripcion\n\n\tPrecio: {objeto.precio.__str__()}.\n')
    mostrar_circuito(caminos)
    time.sleep(segundos)
caminos.quitar_usuario(usuario)
for objeto in caminos.suscriptos:
    print(f'\nsuscripcion\n\n\tPrecio: {objeto.precio.__str__()}\n')
    mostrar_circuito(caminos)
    time.sleep(segundos)

mostrar_circuito(caminos)
