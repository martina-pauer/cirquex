class suscribir():
    '''
        Define como será la suscripción
        con precio y cantidad de usuarios
    '''
    def __init__(self):

        self.precio : float = 1.0

        self.costo : float = 1.0

        self.usuarios : int = 1

        self.identificar : str = ''

    def duplicar(self) -> int:
        '''
            Duplica el precio siempre que entre
            todos los usuarios no cubran el costo
            para dar el servicio.
        '''
        if (self.precio * self.usuarios) < self.costo:
            self.precio *= 2

        return self.precio

    def dividir(self, partes : int = 2) -> int:
        '''
            Reduce precio siempre que entre todos
            los usuarios cumplan el costo.
        '''
        if (self.precio * self.usuarios) >= self.costo:
            self.precio /= partes

        return self.precio

class circuito_financiero():
    '''
        Define circuito de suscripciones con
        unos costos y unos ingresos ajustando
        todo a un precio razonable y sostenible
    '''
    def __init__(self):

        self.suscriptos : list = []

        self.costo : float = 1.0    

        self.ingreso : float = 0.0

        self.total : float = 0.0

    def agregar_usuario(self, sus : suscribir):
        '''
           Agregar nueva suscripcion y actualiza
           numero de usuarios y precio a todas las suscripciones
           del circuito.
        '''

        self.suscriptos.append(sus)

        for agregar in self.suscriptos:

            agregar.usuarios = self.suscriptos.__len__() + 1

            agregar.costo = self.costo

            if (agregar.precio * agregar.usuarios) >= self.costo:
                agregar.dividir()

            self.total = agregar.precio * agregar.usuarios

            self.ingreso = self.total - self.costo

    def quitar_usuario(self, sus):
        '''
            Retira usuario de la suscripcion actualizando cantidad y
            precio solo si no se cumplen costos con precio de 
        '''

        self.suscriptos.remove(sus)

        for quitar in self.suscriptos:

            quitar.usuarios = self.suscriptos.__len__() - 1

            quitar.costo = self.costo

            quitar.duplicar()

            self.total = quitar.precio * quitar.usuarios

            self.ingreso = self.total - self.costo