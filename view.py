#!/usr/bin/python3

from cirquex import Suscription, FinancialCirq

user1 = Suscription()
user2 = Suscription()
user3 = Suscription()
user4 = Suscription()

users = [user1, user2, user3, user4]

cirq = FinancialCirq()

cont = open('cont.txt', 'r+')
test_number = int(cont.readline().replace('\n', ''))
cont.close()
del cont

for user in users:
    cirq.add_user(user)
    print(f'Testing test-{test_number.__str__()} with {cirq.suscripts.__len__()}:\n')
    print(f'\tsuscription ${user.price.__str__()}\n')
    print(f'\tin ${cirq.incomes.__str__()}, out ${cirq.costs.__str__()}\n')

print(f'Suscription ${users[users.__len__() - 1].price.__str__()}\n')
print(f'In ${cirq.incomes.__str__()}, out ${cirq.costs.__str__()}\n')

cirq.cirq_view(f'tests/test-{test_number.__str__()}.html', 'Martina Pauer', '')

test_number += 1

save = open('cont.txt', 'w') 
save.write(f'{test_number.__str__()}')
save.close()
del save, users, user1, user2, user3, user4, cirq, test_number

