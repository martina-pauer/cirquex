#!/usr/bin/python3

from cirquex import Suscription, FinancialCirq

user1 = Suscription()
user2 = Suscription()
user3 = Suscription()
user4 = Suscription()

users = [user1, user2, user3, user4]

cirq = FinancialCirq()

for user in users:
    cirq.add_user(user)

cirq.cirq_view('tests/test-14.html', 'Martina Pauer', '')    
