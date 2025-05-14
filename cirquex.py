class suscribir():
    '''
        Define como será la suscripción
        con precio y cantidad de usuarios
    '''
    def __init__(self):

        self.precio : int = 1

        self.usuarios : int = 1

        self.identificar : str = ''

    def duplicar(self) -> int:

        self.precio *= 2

        return self.precio

    def dividir(self, partes : int = 2) -> int:

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

        self.costo : int = 1    

        self.ingreso : int = 0

    def agregar_usuario(self, sus : suscribir):
        '''
           Agregar nueva suscripcion y actualiza
           numero de usuarios y precio a todas las suscripciones
           del circuito.
        '''
        self.suscriptos.append(sus)

        for objeto in self.suscriptos:
            objeto.usuarios = self.suscriptos.__len__()

            if ((objeto.precio / 2) * objeto.usuarios) > self.costo:
                objeto.dividir()
                self.ingreso = self.precio - self.costo

    def quitar_usuario(self, sus):
        '''
            Retira usuario de la suscripcion actualizando cantidad y
            precio solo si no se cumplen costos con precio de 
        '''
        self.suscriptos.remove(sus)

        for objeto in self.suscriptos:
            objeto.usuarios = self.suscriptos.__len__()

            while objeto.precio <= self.costo:
                objeto.precio.duplicar()