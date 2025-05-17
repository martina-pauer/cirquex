class suscribir():
    '''
        Define como será la suscripción
        con precio y cantidad de usuarios
    '''
    def __init__(self):

        self.precio : float = 1.0

        self.usuarios : int = 1

        self.identificar : str = ''

    def duplicar(self) -> int:

        self.precio *= 2

        return self.precio

    def dividir(self, partes : int = 2) -> int:

        if (self.precio / partes) > (partes * self.precio):
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

        for objeto in self.suscriptos:
            objeto.usuarios = self.suscriptos.__len__() + 1

            if (objeto.precio * objeto.usuarios) >= self.costo:
                objeto.dividir()

            self.total = objeto.precio * objeto.usuarios

            self.ingreso = self.total - self.costo

    def quitar_usuario(self, sus):
        '''
            Retira usuario de la suscripcion actualizando cantidad y
            precio solo si no se cumplen costos con precio de 
        '''
        self.suscriptos.remove(sus)

        for objeto in self.suscriptos:
            objeto.usuarios = self.suscriptos.__len__() - 1
            self.total = objeto.precio * objeto.usuarios
            self.ingreso = self.total - self.costo