class MaxBasketSize:
    def __init__(self, lst, basket):
        self.lst = lst
        self.basket = []

    def buy_item(self, item: str) -> None:
        self.lst = 3
        self.basket.append(item)
        if len(self.basket) > self.lst:
            self.basket.pop(0)


def basket_menu(item: list):
    print("""
       Welcome to Ace Store
   1 -> Purchase an item
   2 -> 
    """)
