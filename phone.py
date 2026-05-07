from item import Item

class Phone(Item):

    def __init__(self, name: str, price: float, broken_phones=0, quantity=0):
        # Call to super function to have access to all class attributes and methods
        super().__init__(name, price, quantity)

        # Run validations to the received parameters
        if isinstance(broken_phones, bool) or not isinstance(broken_phones, int):
            raise TypeError(f"broken_phones must be int, got {type(broken_phones).__name__}")
        if broken_phones > self.quantity:
            raise ValueError(f"broken_phones {broken_phones} is greater than quantity {self.quantity}")

        # Assign to self object
        self.broken_phones = broken_phones

    @property
    def effective_quantity(self):
        return self.quantity - self.broken_phones

    def calculate_total_price(self):
        return self.__price * self.effective_quantity