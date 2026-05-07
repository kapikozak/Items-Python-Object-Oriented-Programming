import csv

class Item:

    pay_rate = 0.8 # The pay rate to apply the 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity: int=0):
        # Run validations to the received arguments
        if isinstance(price, bool) or not isinstance(price, (int, float)):
            raise TypeError(f"price must be int or float, got {type(price).__name__}")
        if price < 0:
            raise ValueError(f"price {price} is lower than zero")
        if isinstance(quantity, bool) or not isinstance(quantity, int):
            raise TypeError(f"quantity must be int, got {type(quantity).__name__}")
        if quantity < 0:
            raise ValueError(f"quantity {quantity} is lower than zero")

        # Assign to self object
        self.__name = name
        self.__price = float(price)
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: 'str'):
        if len(value) > 10:
            raise ValueError(f"name {value} is too long, name length has to be lower than or equal to 10")
        self.__name = value

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price * (1 + increment_value)

    def calculate_total_price(self):
        return self.__price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                Item(
                    name=row.get('name'),
                    price=float(row.get('price')),
                    quantity=int(row.get('quantity'))
                )

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"