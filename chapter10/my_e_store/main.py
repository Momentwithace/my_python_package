from item import Item
# from phone import Phone

Item.instantiate_from_cvs()

print(Item.all)

item1 = Item("Charger", 700)
print(item1)

item1.name = "fan"
print(item1.name)

item1.__price = 900
print(item1.price)

