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

acc = Account('bob', 10)
acc.add_transaction(29)
acc.add_transaction(-10)
acc.add_transaction(50)
acc.add_transaction(-20)
acc.add_transaction(30)

acc()

# In general, the downside of having a __call__ method on your objects
# is that it can be hard to see what the purpose of calling the object is
# Most of the time it’s therefore better to add an explicit method to the class


def validate_transaction(acc, amount_to_add):
    with acc as a:
        print('Adding {} to account'.format(amount_to_add))
        a.add_transaction(amount_to_add)
        print('New balance would be: {}'.format(a.balance))
        if a.balance < 0:
            raise ValueError('sorry cannot go into debt!')


acc4 = Account('sue', 10)

print('\nBalance start: {}'.format(acc4.balance))
validate_transaction(acc4, 20)

print('\nBalance end: {}'.format(acc4.balance))

acc4 = Account('sue', 10)

print('\nBalance start: {}'.format(acc4.balance))
try:
    validate_transaction(acc4, -20)
except ValueError as exc:
    print(exc)

print('\nBalance end: {}'.format(acc4.balance))
