from item import Item

class Phone(Item):

    def __init__(self, name: str, price: float, quantity: float, broken_phone=0):
        #     # calling the super function gives the child's class access to the parent class attribute

        super(Phone, self).__init__(name, price, quantity)

        # run validation to the received argument
        assert broken_phone >= 0, f"Broken Phones {broken_phone} is not greater than or equal to zero!"

        self.broken_phone = broken_phone