class Order:
    def __init__(self, order_id, qty, price, buy = True):
        self.order_id = order_id
        self.buy = buy
        self.qty = qty
        self.price = price

    def __str__(self):
        if(self.buy):
            return(f'\tBUY {self.qty}@{self.price} id={self.order_id}')
        else:
            return(f'\tSELL {self.qty}@{self.price} id={self.order_id}')

class Book:
    def __init__(self, name):
        self.name = name
        self.orders = []
        self.order_count = 1

    def insert_buy(self, qty, price):
        buy_order = Order(order_id = self.order_count, side = "BUY", qty = qty, price = price)
        self.orders.append(buy_order)
        self.order_count += 1
        print(f'--- Insert {buy_order.side} {buy_order.qty}@{buy_order.price} id={buy_order.order_id} on {self.name}\nBook on {self.name}')
        #self.print_insertion(buy_order)
        self.print_book()

    def insert_sell(self, qty, price):
        sell_order = Order(order_id = self.order_count, side = "SELL", qty = qty, price = price)
        self.orders.append(sell_order)
        self.order_count += 1
        print(f'--- Insert {sell_order.side} {sell_order.qty}@{sell_order.price} id={sell_order.order_id} on {self.name}\nBook on {self.name}')
        #self.print_insertion(sell_order)
        self.print_book()

    def print_book(self):
        self.orders.sort(key = lambda x: x.price, reverse = True)
        for order in self.orders:
            if (order.qty > 0):
                print(f'\t{order.side} {order.qty}@{order.price} id={order.order_id}')
        print("-----------------------")
