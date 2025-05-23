class Suscription():
    '''
        Define the suscription data with economy and users.
    '''
    def __init__(self):

        self.price : float = 1.0

        self.cost : float = 1.0

        self.users : int = 1

        self.ID : str = ''

    def duplicate(self) -> float:
        '''
            Duplicate the price always that between
            all the users can't pay the cost.
        '''
        if (self.price * self.users) < self.cost:
            self.price *= 2

        return self.price

    def divide(self, pieces : int = 2) -> float:
        '''
            Reduce price always that between all
            the users pay the cost.
        '''
        if (self.price * self.users) >= self.cost:
            self.price /= pieces

        return self.price

class FinancialCirq():
    '''
        Define suscription circuit with costs and incomes fixing 
        all to a reasonable and maintainable price.
    '''
    def __init__(self):

        self.suscripts : list = []

        self.costs : float = 1.0    

        self.incomes : float = 0.0

        self.total : float = 0.0

    def add_user(self, sus : Suscription):
        '''
           Add new suscription and increase users number
           lowing price to all circuit suscriptions.
        '''

        self.suscripts.append(sus)
        
        for added in self.suscripts:

            added.users = self.suscripts.__len__() + 1

            added.cost = self.costs

            if (added.price * added.users) >= self.costs:
                added.divide()

            self.total = added.price * added.users

            self.incomes = self.total - self.costs

    def quit_user(self, sus : Suscription):
        '''
            Retire user from the suscription list updating only if
            the costs are covered the price and always the users
            quantity.
        '''

        self.suscripts.remove(sus)

        for quit in self.suscripts:

            quit.users = self.suscripts.__len__() - 1

            quit.cost = self.costs

            quit.duplicate()

            self.total = quit.price * quit.users

            self.incomes = self.total - self.costs

    def cirq_view(self, file_name : str, author : str, css_text : str):
        '''
            Create a HTML file from template.html with a
            fila name, author and CSS style for visualize
            state of the object in circuit view planner-like.
        '''
        # Delete unnecesary lines on copy from template
        file = open('template.html', 'r')

        copy = ''

        cont = 1

        for line in file.readlines():
            if ((cont < 4) or (cont > 20)):
                copy += line
            cont += 1
        # Delete extra vars
        file.close()
        del file, cont
        # Replace text in copy later write new HTML file with output for this object
        copy = copy.replace('#1', f'<meta name = "author" content = "{author.__str__()}"/>')


        file = open(file_name, 'x')
        file.write(copy)
        file.close()
        del file, copy