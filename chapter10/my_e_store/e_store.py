import csv

class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: float):
        # run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_cvs(cls):
        with open('item.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}' {self.price} {self.quantity})"

Item.instantiate_from_cvs()
print(Item.all)
# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)
# print(Item.all)

for instance in Item.all:
    print(instance.name)


# # item1 = Item("Phone", 1000, 3)
# item1.pay_rate = 0.7
# item1.apply_discount()
# print(item1.price)
# print(Item.__dict__)
# print(item1.__dict__)
# print(f'Item1 {item1.name} at this {item1.price} of this {item1.quantity}')
# print(item1.calculate_total_price())
#
# item2 = Item("Laptop", 1000, 3)
# print(f'Item1 {item2.name} at this {item2.price} of this {item2.quantity}')
# print(item2.calculate_total_price())
class Phone(Item):

    def __init__(self, name: str, price: float, quantity: float, broken_phone=0):

        #     # calling the super function gives the child's class access to the parent class attribute

        super(Phone, self).__init__(name, price, quantity)

        # run validation to the received argument
        assert broken_phone >= 0, f"Broken Phones {broken_phone} is not greater than or equal to zero!"

        self.broken_phone = broken_phone

    #  Phone.all.append(self)
    # 
    # def __init__(self, name: str, price: float, quantity: float, broken_phone=0):
    #     # calling the super function gives the child's class access to the parent class attribute
    #     super().__init__(
    #         name, price, quantity
    #     )
    # 
    #     assert broken_phone >= 0, f"Broken Phones {broken_phone} is not greater than or equal to zero!"
    # 
    #     self.broken_phone = broken_phone
    #    Phone.all.append(self)


phone1 = Phone("Iphone7", 1000, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone("Iphone6", 700, 5, 1)

print(Item.all)
# print(Phone.all)
