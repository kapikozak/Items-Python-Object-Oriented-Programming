from item import Item

class Keyboard(Item):
    pay_rate = 0.6 # 40% discount for all keyboards

    def __init__(self, name: str, price: float, quantity: int=0):
        # Call to super function to have access to all class attributes and methods
        super().__init__(name, price, quantity)