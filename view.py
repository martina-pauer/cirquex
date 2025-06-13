#!/usr/bin/python3

from cirquex import Suscription, FinancialCirq
import os

user1 = Suscription()
user2 = Suscription()
user3 = Suscription()
user4 = Suscription()

users = [user1, user2, user3, user4]

cirq = FinancialCirq()

cont = open('cont.txt', 'r')
test_number = int(cont.readline().replace('\n', ''))
cont.close()
del cont

for user in users:
    cirq.add_user(user)
    cirq.update()
    print(f'Testing test-{test_number.__str__()} with {cirq.suscripts.__len__()}:\n')
    print(f'\tsuscription ${cirq.suscripts[cirq.suscripts.index(user)].price.__str__()}\n')
    print(f'\tin ${cirq.incomes.__str__()}, out ${cirq.costs.__str__()}\n')

cirq.update()

print(f'Suscription ${cirq.suscripts[cirq.suscripts.__len__() - 1].price.__str__()}\n')
print(f'In ${cirq.incomes.__str__()}, out ${cirq.costs.__str__()}\n')

cirq.cirq_view(f'tests/test-{test_number.__str__()}.html', 'Martina Pauer', '* {cursor: grab; overflow: revert-layer; z-index: 0;} * > * {cursor: grab; overflow: revert-layer; z-index: 0;}')

save = open('index.html', 'r')
lines = save.readlines()

save.close()
del save

copy = open('index.html', 'w')
save = ''
for line in lines:
    save += line.__str__().replace(f'start = "{test_number - 1}"', f'start = "{test_number}"')
copy.write(save)    

copy.close()
del copy, save

test_number += 1

save = open('cont.txt', 'w')
save.write(f'{test_number.__str__()}')
save.close()
del save, users, user1, user2, user3, user4, cirq, test_number
os.system('rm -R __pycache__')

