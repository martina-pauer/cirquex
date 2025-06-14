class Suscription():
    '''
        Define the suscription data with economy and users.
    '''
    def __init__(self):

        self.price : float = 1.00

        self.cost : float = 1.00

        self.users : int = 1

        self.ID : str = ''

    def duplicate(self, mult : float = 2) -> floa
        '''
            Duplicate the price always that between
            all the users can't pay the cost.
        '''
        if (self.price * self.users) < self.cost:
            self.price *= mult

        self.price = self.price.__round_(2)

        return self.price

    def divide(self, pieces : float = 2) -> float:
        '''
            Reduce price always that between all
            the users pay the cost.
        '''
        if (self.price * self.users) >= self.cost:
            self.price /= pieces

        self.price = self.price.__round__(2)

        return self.price

class FinancialCirq():
    '''
        Define suscription circuit with costs and incomes fixing 
        all to a reasonable and maintainable price.
    '''
    def __init__(self):

        self.suscripts : list = []

        self.costs : float = 1.00    

        self.incomes : float = 0.00

        self.total : float = 0.00

    def update(self):
        '''
            Keep the current and right values for all
            properties and objects
        '''
        minor = self.suscripts[0].price.__round__(2)

        for suscript in self.suscripts:
            suscript.users = self.suscripts.__len__()
            suscript.cost = self.costs.__round__(2)
            if ((suscript.price < minor) and ((suscript.price * suscript.users) >= suscript.cost)):
                minor = suscript.price.__round__(2)
        # Later of find the minor price change all prices to same value        
        for change in self.suscripts:
            change.price = minor

        self.total = (self.suscripts[0].price * self.suscripts[0].users).__round__(2)

        self.incomes = (self.total - self.costs).__round__(2)        

    def add_user(self, sus : Suscription):
        '''
           Add new suscription and increase users number
           lowing price to all circuit suscriptions.
        '''

        self.suscripts.append(sus)
        
        self.update()
        
        for added in self.suscripts:
          self.update()
          if (added.price * added.users) >= self.costs:
              added.divide(added.users)
          self.update()    

        self.update()      
         
    def quit_user(self, sus : Suscription):
        '''
            Retire user from the suscription list updating only if
            the costs are covered the price and always the users
            quantity.
        '''
        
        self.suscripts.remove(sus)
        
        self.update()
        
        for quit in self.suscripts:
            
            self.update()

            quit.duplicate(quit.users)

            self.update()

        self.update()
        
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
        copy = copy.replace('#2', 'Financial Circuits View')
        copy = copy.replace('#3', css_text.__str__() + 'header, footer {padding: -98%; text-align: center;} .rect, .circle {transition: 1.8s ease; display: inline-grid; border: 0.3em solid #000000; margin: 2%; padding: 1em;} .circle {border-radius: 1.4em;} .circle:hover, .rect:hover {background: #dddddd; z-index: 1; padding-top: 4%; padding: -2%; font-size: 1.2em; text-align: center; height: 4em; width: 7em;} * .circle:hover, * rect:hover {background: #000000; color: #ffffff;}')
        copy = copy.replace('#4', 'Financial Circuits for Suscriptions')
        
        suscription_price = ''
        for suscript in self.suscripts:
            self.update()
            suscript.divide(self.suscripts.__len__())
            suscript.duplicate(self.suscripts.__len__(
            suscription_price += f'<p class = "circle">{suscript.price.__str__()}</p>'
            self.update()    
        copy = copy.replace('#5', f'<div class = "rect">{suscription_price}</div><div class = "rect">{self.total.__str__()}</div><div class = "rect"><p class = "rect">{self.incomes.__str__()}</p><p class = "rect">{self.costs.__str__()}</p></div>')
        del suscription_price
        copy = copy.replace('#6', author.__str__())
        file = open(file_name, 'x')
        file.write(copy)
        del copy
        file.close()
        del file
