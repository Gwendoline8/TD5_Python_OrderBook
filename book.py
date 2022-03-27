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
   
    def sort_orders(self):
        sell_orders = []
        buy_orders = []
        for order in self.orders:
            if(order.buy):
                buy_orders.append(order)
            else:
                sell_orders.append(order)
        sell_orders.sort(key = lambda x: x.price)
        buy_orders.sort(key = lambda x: -x.price)
        self.orders = sell_orders + buy_orders

    def insert_buy(self, qty, price):
        buy_order = Order(order_id = self.next_order_id, qty = qty, price = price)
        self.orders.append(buy_order)
        self.next_order_id += 1
        self.sort_orders()
        print(f'--- Insert BUY {buy_order.qty}@{buy_order.price} id={buy_order.order_id} on {self.name}')
        print(self)

    def insert_sell(self, qty, price):
        sell_order = Order(order_id = self.next_order_id, qty = qty, price = price, buy = False)
        self.orders.append(sell_order)
        self.next_order_id += 1
        self.sort_orders()
        print(f'--- Insert SELL {sell_order.qty}@{sell_order.price} id={sell_order.order_id} on {self.name}')
        print(self)
