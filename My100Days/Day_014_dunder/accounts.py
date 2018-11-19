# https://dbader.org/blog/python-dunder-methods
# Bob Belderbos guest article

from functools import total_ordering

class Account:
    """A simple account class"""

    def __init__(self, owner, amount=0):
        """
        This is the constructor that lets us create
        objects from this class
        """
        self.owner = owner
        self.amount = amount
        self._transactions = []

# Instead of account you can use self.__class__.__name__
# If you only implement one, implement __repr__
# %s and %r would apply str() and repr() respectively
# from repr you are supposed to be able to recreate the object
# repr should have proper python syntax
# ! is a conversion flag that forces type to formate as a string

    def __repr__(self):
        return 'Account({!r}, {!r})'.format(self.owner, self.amount)


    def __str__(self):
        return ('{} of {} with starting amount: {}'
                .format(__class__.__name__, self.owner, self.amount))

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use value of type int for amount')
        self._transactions.append(amount)


    @property
    def balance(self):
        return self.amount + sum(self._transactions)


# why is sublime behaving so funny when you type property or class
    def __len__(self):
        return len(self._transactions)


    def __getitem__(self, position):
        return self._transactions[position]


# in the past I used __iter__ for iteration rather than __get_item__
    def __reversed__(self):
        return self[::-1]


# need to read on functools total_ordering decorator
    @total_ordering
    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance


# use addition to represent accounts merging
    def __add__(self, other):
        owner = self.owner + other.owner
        start_amount = self.balance + other.balance
        acc =  Account(owner, start_amount)
        for t in list(self) + list(other):
            acc.add_transaction(t)
        return acc

# In general, if you would add your object to a 
# builtin (int, str, …) the __add__ method of the 
# builtin wouldn’t know anything about your object. 
# In that case you need to implement the reverse 
# add method (__radd__) as well.  
# http://www.marinamele.com/2014/04/modifying-add-method-of-python-class.html      

