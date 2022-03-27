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
        self.next_order_id = 1
    
    def __str__(self):
        return(f"\nBook on {self.name}\n" + '\n'.join(list(map(str, self.orders))) + "\n------------------------")
    
    def insert_buy(self, qty, price):
        buy_order = Order(order_id = self.next_order_id, qty = qty, price = price)
        self.orders.append(buy_order)
        self.next_order_id += 1
        print(f'--- Insert BUY {buy_order.qty}@{buy_order.price} id={buy_order.order_id} on {self.name}')
        print(self)

    def insert_sell(self, qty, price):
        sell_order = Order(order_id = self.next_order_id, qty = qty, price = price, buy = False)
        self.orders.append(sell_order)
        self.next_order_id += 1
        print(f'--- Insert SELL {sell_order.qty}@{sell_order.price} id={sell_order.order_id} on {self.name}')
        print(self)
