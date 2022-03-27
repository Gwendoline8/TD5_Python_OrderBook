class Order:
    def __init__(self, order_id, qty, price, buy = True):
        self.order_id = order_id
        self.buy = buy
        self.qty = qty
        self.price = price

    def __str__(self):
        """Display the order"""
        if(self.buy):
            return(f'\tBUY {self.qty}@{self.price} id={self.order_id}')
        else:
            return(f'\tSELL {self.qty}@{self.price} id={self.order_id}')

class Book:
    def __init__(self, name):
        self.name = name
        self.orders = []
        self.executions = []
        self.next_order_id = 1
    
    def __str__(self):
        """Display the current state of the book"""
        return('\n'.join(self.executions) + f"\nBook on {self.name}\n" + '\n'.join(list(map(str, self.orders))) + "\n------------------------")
    
    def sort_orders(self):
        """Sorts the orders by side and by price : SELL orders are sorted in ascending prices and BUY orders in descending prices"""
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
        """Inserts a new BUY order in the book"""
        buy_order = Order(order_id = self.next_order_id, qty = qty, price = price)
        self.orders.append(buy_order)
        self.next_order_id += 1
        self.sort_orders()
        print(f'--- Insert BUY {buy_order.qty}@{buy_order.price} id={buy_order.order_id} on {self.name}')
        self.execute_order(buy_order)
        print(self)

    def insert_sell(self, qty, price):
        """Inserts a new SELL order in the book""" 
        sell_order = Order(order_id = self.next_order_id, qty = qty, price = price, buy = False)
        self.orders.append(sell_order)
        self.next_order_id += 1
        self.sort_orders()
        print(f'--- Insert SELL {sell_order.qty}@{sell_order.price} id={sell_order.order_id} on {self.name}')
        self.execute_order(sell_order)
        print(self)

    def execute_order(self, new_order):
        """Check if the added order can be executed"""
        for order in self.orders:
            if(new_order.buy != order.buy and new_order.price == order.price):
                if(new_order.qty < order.qty):
                    self.orders = [x for x in self.orders if x.order_id != new_order.order_id]
                    self.executions.append(f"Execute {order.qty - new_order.qty} at {order.price} on {self.name}")
                    order.qty -= new_order.qty
                    break # The new order can't be executed again
                elif(new_order.qty > order.qty):
                    self.orders = [x for x in self.orders if x.order_id != order.order_id]
                    self.executions.append(f"Execute {new_order.qty - order.qty} at {order.price} on {self.name}")
                    new_order.qty -= order.qty
                    # No break because the order might be executed again
                else:
                    self.orders = [x for x in self.orders if x.order_id != new_order.order_id and x.order_id != order.order_id]
                    self.executions.append(f"Execute {order.qty} at {order.price} on {self.name}")
                    break # The new order can't be executed again
