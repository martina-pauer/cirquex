#!/usr/bin/python3

from cirquex import Suscription

import time
# Test for cirquex.Suscription class
user = Suscription()
user.price = float(input('\nType initial suscription price: '))
user.ID = 'Family Group'
user.users = 3
# Show data
print(f'\nsuscription\n\n\tPrice: {user.price.__str__()}\n\tUser: {user.ID.__str__()}\n\tTotal: {user.users.__str__()} users.\n')

persons = [user]

for added in range(1, 5):

    suscript = Suscription()

    suscript.users = 4

    suscript.price = (user.price / suscript.users)

    persons.append(suscript)
# Test for cirquex.FinancialCirq class
from cirquex import FinancialCirq

def show_circuit(showed : FinancialCirq):

    if showed.incomes >= 0:

        print(f'\tThe cost is of ${showed.costs.__str__()} and the income is ${showed.incomes.__str__()}\n\nTotal: {showed.suscripts[0].users.__str__()} users.\n')
    else:
        print(f'Economic Crash when the price is ${showed.suscripts[0].price} with {showed.suscripts[0].users} users.')

paths = FinancialCirq()

paths.costs = 5

seconds = 1

for person in persons:

    paths.add_user(person)

    print(f'\nsuscription\n\n\tprice: ${person.price.__str__()}\n')

    show_circuit(paths)

    time.sleep(seconds)

paths.quit_user(user)

for suscript in paths.suscripts:

    print(f'\nsuscription\n\n\tprice: ${suscript.price.__str__()}\n')
    show_circuit(paths)
    time.sleep(seconds)

show_circuit(paths)
