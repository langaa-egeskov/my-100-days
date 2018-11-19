from accounts import Account

acc = Account('bob', 10)
print(acc)

print(str(acc))

print((repr(acc)))

acc.add_transaction(29)
acc.add_transaction(-10)
acc.add_transaction(50)
acc.add_transaction(-20)
acc.add_transaction(30)

print(f'{acc.balance}')

print(list(reversed(acc)))

acc2 = Account('tim', 100)
acc2.add_transaction(20)
acc2.add_transaction(40)
print(acc2.balance)

print(f'acc2 > acc = {acc2 > acc}')
print(f'acc2 < acc = {acc2 < acc}')
print(f'acc2 == acc = {acc2 == acc}')

acc3 = acc2 + acc
print(acc3)
print(f'acc3.amount = {acc3.amount}')
print(f'acc3.balance = {acc3.balance}')
print(f'acc3._transactions = {acc3._transactions}')