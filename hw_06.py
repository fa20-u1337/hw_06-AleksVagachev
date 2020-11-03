class Fib():
    """Число Фибоначчи.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Проверка, что start не изменился
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        "*** ТВОЙ КОД ЗДЕСЬ ***"

    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """Торговый автомат, продающий некоторый товар по некоторой цене.
    
    >>> v = VendingMachine('яблоко', 10)
    >>> v.vend()
    'Товара нет в наличии.'
    >>> v.restock(2)
    'Количество товара «яблоко»: 2'
    >>> v.vend()
    'Нужно дополнительно внести 10 ₽.'
    >>> v.deposit(7)
    'Доступно: 7 ₽'
    >>> v.vend()
    'Нужно дополнительно внести 3 ₽.'
    >>> v.deposit(5)
    'Доступно: 12 ₽'
    >>> v.vend()
    'Получите яблоко и сдачу 2 ₽.'
    >>> v.deposit(10)
    'Доступно: 10 ₽'
    >>> v.vend()
    'Получите яблоко.'
    >>> v.deposit(15)
    'Товара нет в наличии. Вот твои деньги — 15 ₽.'

    >>> w = VendingMachine('лимонад', 2)
    >>> w.restock(3)
    'Количество товара «лимонад»: 3'
    >>> w.restock(3)
    'Количество товара «лимонад»: 6'
    >>> w.deposit(2)
    'Доступно: 2 ₽'
    >>> w.vend()
    'Получите лимонад.'
    """
    "*** ТВОЙ КОД ЗДЕСЬ ***"
    def __init__(self, prod, price):
        self.prod = prod
        self.price = price
        self.quan = None
        self.balance = None

    def restock(self, quan):
        if self.quan is None:
            self.quan = quan
        else:
            self.quan += quan
        return 'Количество товара «{}»: {}'.format(self.prod, self.quan)

    def deposit(self, balance):
        if self.balance is None:
            self.balance = balance
        elif self.quan == 0 or self.quan is None:
            return 'Товара нет в наличии. Вот твои деньги — {} ₽.'.format(balance)
        else:
            self.balance += balance
        return 'Доступно: {} ₽'.format(self.balance)

    def vend(self):
        if self.quan is None:
            return 'Товара нет в наличии.'
        elif self.balance is None:
            return 'Нужно дополнительно внести {} ₽.'.format(self.price)
        elif self.balance > self.price:
            change = self.balance - self.price
            self.quan -= 1
            self.balance = 0
            return 'Получите {} и сдачу {} ₽.'.format(self.prod, change)
        elif self.balance == self.price:
            self.balance = 0
            self.quan -= 1
            return 'Получите {}.'.format(self.prod)
        elif self.balance < self.price:
            change = self.price - self.balance
            return 'Нужно дополнительно внести {} ₽.'.format(change)
