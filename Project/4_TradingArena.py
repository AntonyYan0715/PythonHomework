from collections import deque
import time
import random
from abc import ABC



from enum import Enum
class OrderType(Enum):
    LIMIT = 1
    MARKET = 2
    IOC = 3

class OrderSide(Enum):
    BUY = 1
    SELL = 2

class NonPositiveQuantity(Exception):
    pass

class NonPositivePrice(Exception):
    pass

class InvalidSide(Exception):
    pass

class UndefinedOrderType(Exception):
    pass

class UndefinedOrderSide(Exception):
    pass

class NewQuantityNotSmaller(Exception):
    pass

class UndefinedTraderAction(Exception):
    pass

class UndefinedResponse(Exception):
    pass

class Order(ABC):
    def __init__(self, id, symbol, quantity, side, time):
        self.id = id
        self.symbol = symbol
        if quantity > 0:
            self.quantity = quantity
        else:
            raise NonPositiveQuantity("Quantity Must Be Positive!")
        if side in [OrderSide.BUY, OrderSide.SELL]:
            self.side = side
        else:
            raise InvalidSide("Side Must Be Either \"Buy\" or \"OrderSide.SELL\"!")
        self.time = time


class LimitOrder(Order):
    def __init__(self, id, symbol, quantity, price, side, time):
        super().__init__(id, symbol, quantity, side, time)
        if price > 0:
            self.price = price
        else:
            raise NonPositivePrice("Price Must Be Positive!")
        self.type = OrderType.LIMIT


class MarketOrder(Order):
    def __init__(self, id, symbol, quantity, side, time):
        super().__init__(id, symbol, quantity, side, time)
        self.type = OrderType.MARKET


class IOCOrder(Order):
    def __init__(self, id, symbol, quantity, price, side, time):
        super().__init__(id, symbol, quantity, side, time)
        if price > 0:
            self.price = price
        else:
            raise NonPositivePrice("Price Must Be Positive!")
        self.type = OrderType.IOC


class FilledOrder(Order):
    def __init__(self, id, symbol, quantity, price, side, time, limit=False):
        super().__init__(id, symbol, quantity, side, time)
        self.price = price
        self.limit = limit

        
trader_to_exchange = deque()
exchange_to_trader = [deque() for _ in range(100)]

# Above you are given two deques where the orders submitted to the exchange and back to the trader
# are expected to be populated by the trading exchange simulator
# The first is trader_to_exchange, a deque of orders to be populated for the exchange to execute
# The second is a list of 100 deques exchange_to_trader, which are acknowledgements from the exchange
# to each of the 100 traders for trades executed on their behalf

# Below you have an implementation of a simulated thread to be used where each trader is a separate thread
class MyThread:
    list_of_threads=[]
    def __init__(self,id='NoID'):
        MyThread.list_of_threads.append(self)
        self.is_started=False
        self.id = id
    def start(self):
        self.is_started = True
    def join(self):
        print('Trader ' + str(self.id) + ' will be waited')




# Paste in your implementation for the matching engine below

# ----------------------------------------------------------
# PASTE MATCHING ENGINE FROM Q2 HERE
class MatchingEngine():
    def __init__(self):
        self.bid_book = []
        self.ask_book = []
        # These are the order books you are given and expected to use for matching the orders below

    # Note: As you implement the following functions keep in mind that these enums are available:
#     class OrderType(Enum):
#         LIMIT = 1
#         MARKET = 2
#         IOC = 3

#     class OrderSide(Enum):
#         BUY = 1
#         SELL = 2

    def handle_order(self, order):
        # Implement this function
        # In this function you need to call different functions from the matching engine
        # depending on the type of order you are given
        if order.type == OrderType.LIMIT:
            handle_limit_order(order)
            
        elif order.type == OrderType.MARKET:
            handle_market_order(order)
            
        elif order.type == OrderType.IOC:
            handle_ioc_order(order)
        
        # You need to raise the following error if the type of order is ambiguous
        else:
            raise UndefinedOrderType("Undefined Order Type!")

    
    def handle_limit_order(self, order): 
        # Implement this function
        # Keep in mind what happens to the orders in the limit order books when orders get filled
        # or if there are no crosses from this order
        # in other words, handle_limit_order accepts an arbitrary limit order that can either be 
        # filled if the limit order price crosses the book, or placed in the book. If the latter, 
        # pass the order to insert_limit_order below. 
        filled_orders = []
        # The orders that are filled from the market order need to be inserted into the above list
        if order.side == OrderSide.BUY:
            target_book = self.ask_book
            
        elif order.side == OrderSide.SELL:
            target_book = self.bid_book
        
        else:
            # You need to raise the following error if the side the order is for is ambiguous
            raise UndefinedOrderSide("Undefined Order Side!")
        
        while order.quantity:
            if len(target_book) > 0:
                target = target_book[0]
                
                if (order.side == OrderSide.BUY and order.price < target.price) or (order.side == OrderSide.SELL and order.price > target.price):
                    self.insert_limit_order(order)
                    break
                
                elif order.quantity >= target.quantity:
                    del target_book[0]
                    filled_orders.append(FilledOrder(target.id, target.symbol, target.quantity, target.price, target.side, target.time, limit=True))
                    filled_orders.append(FilledOrder(order.id, order.symbol, target.quantity, order.price, order.side, order.time, limit=True))
                    order.quantity -= target.quantity
                
                else:
                    filled_orders.append(FilledOrder(target.id, target.symbol, order.quantity, target.price, target.side, target.time, limit=True))
                    filled_orders.append(FilledOrder(order.id, order.symbol, order.quantity, order.price, order.side, order.time, limit=True))
                    target_book[0].quantity -= order.quantity
                    order.quantity = 0
                    
            else:
                self.insert_limit_order(order)
                break
        
        # The filled orders are expected to be the return variable (list)
        return filled_orders
        

    def handle_market_order(self, order):
        # Implement this function
        filled_orders = []
        # The orders that are filled from the market order need to be inserted into the above list
        if order.side == OrderSide.BUY:
            target_book = self.ask_book
            
        elif order.side == OrderSide.SELL:
            target_book = self.bid_book
        
        else:
            # You need to raise the following error if the side the order is for is ambiguous
            raise UndefinedOrderSide("Undefined Order Side!")

        while order.quantity:
            if len(target_book) > 0:
                target = target_book[0]
                
                if order.quantity >= target.quantity:
                    del target_book[0]
                    filled_orders.append(FilledOrder(target.id, target.symbol, target.quantity, target.price, target.side, target.time, limit=True))
                    filled_orders.append(FilledOrder(order.id, order.symbol, target.quantity, target.price, order.side, order.time, limit=False))
                    order.quantity -= target.quantity
                
                else:
                    filled_orders.append(FilledOrder(target.id, target.symbol, order.quantity, target.price, target.side, target.time, limit=True))
                    filled_orders.append(FilledOrder(order.id, order.symbol, order.quantity, target.price, order.side, order.time, limit=False))
                    target_book[0].quantity -= order.quantity
                    order.quantity = 0
            
            else:
                break
            
        # The filled orders are expected to be the return variable (list)
        return filled_orders
        

    def handle_ioc_order(self, order):
        # Implement this function
        filled_orders = []
        # The orders that are filled from the ioc order need to be inserted into the above list
        if order.side == OrderSide.BUY:
            target_book = self.ask_book
            
        elif order.side == OrderSide.SELL:
            target_book = self.bid_book
        
        else:
            # You need to raise the following error if the side the order is for is ambiguous
            raise UndefinedOrderSide("Undefined Order Side!")
        
        while order.quantity:
            if len(target_book) > 0:
                target = target_book[0]
                
                if (order.side == OrderSide.BUY and order.price < target.price) or (order.side == OrderSide.SELL and order.price > target.price):
                    break
                
                elif order.quantity >= target.quantity:
                    del target_book[0]
                    filled_orders.append(FilledOrder(target.id, target.symbol, target.quantity, target.price, target.side, target.time, limit=True))
                    filled_orders.append(FilledOrder(order.id, order.symbol, target.quantity, order.price, order.side, order.time, limit=True))
                    order.quantity -= target.quantity
                
                else:
                    filled_orders.append(FilledOrder(target.id, target.symbol, order.quantity, target.price, target.side, target.time, limit=True))
                    filled_orders.append(FilledOrder(order.id, order.symbol, order.quantity, order.price, order.side, order.time, limit=True))
                    target_book[0].quantity -= order.quantity
                    order.quantity = 0
                    
            else:
                break
        
        # The filled orders are expected to be the return variable (list)
        return filled_orders


    def insert_limit_order(self, order):
        assert order.type == OrderType.LIMIT
        # Implement this function
        # this function's sole puporse is to place limit orders in the book that are guaranteed
        # to not immediately fill
        if order.side == OrderSide.BUY:
            target_book = self.bid_book
            
            if len(target_book) > 0:
                if order.price > target_book[0].price:
                    target_book.insert(0, order)
                    
                elif order.price <= target_book[-1].price:
                    target_book.append(order)
                
                else:
                    for i in range(len(target_book) - 1):
                        previous_order = target_book[i]
                        next_order = target_book[i + 1]
                        
                        if (order.price <= previous_order.price) and (order.price > next_order.price):
                            target_book.insert(i+1, order)
            else:
                target_book.append(order)
            
        elif order.side == OrderSide.SELL:
            target_book = self.ask_book
            
            if len(target_book) > 0:
                if order.price < target_book[0].price:
                    target_book.insert(0, order)
                    
                elif order.price >= target_book[-1].price:
                    target_book.append(order)
                
                else:
                    for i in range(len(target_book) - 1):
                        previous_order = target_book[i]
                        next_order = target_book[i + 1]
                        
                        if (order.price >= previous_order.price) and (order.price < next_order.price):
                            target_book.insert(i+1, order)
            else:
                target_book.append(order)
            
        else:
            # You need to raise the following error if the side the order is for is ambiguous
            raise UndefinedOrderSide("Undefined Order Side!")

            
    def amend_quantity(self, id, quantity):
        # Implement this function
        # Hint: Remember that there are two order books, one on the bid side and one on the ask side
        for order in self.bid_book:
            if id == order.id:
                if quantity < order.quantity:
                    order.quantity = quantity
                else:
                    # You need to raise the following error if the user attempts to modify an order
                    # with a quantity that's greater than given in the existing order
                    raise NewQuantityNotSmaller("Amendment Must Reduce Quantity!")
        
        for order in self.ask_book:
            if id == order.id:
                if quantity < order.quantity:
                    order.quantity = quantity
                else:
                    raise NewQuantityNotSmaller("Amendment Must Reduce Quantity!")

        return False
    
        
    def cancel_order(self, id):
        # Implement this function
        # Think about the changes you need to make in the order book based on the parameters given
        for i in range(len(self.bid_book)):
            if id == self.bid_book[i].id:
                del self.bid_book[i]
                break
        
        for i in range(len(self.ask_book)):
            if id == self.ask_book[i].id:
                del self.ask_book[i]
                break
#-----------------------------------------------------------

# Each trader can take a separate action chosen from the list below:

# Actions:
# 1 - Place New Order/Order Filled
# 2 - Amend Quantity Of An Existing Order
# 3 - Cancel An Existing Order
# 4 - Return Balance And Position

# request - (Action #, Trader ID, Additional Arguments)

# result - (Action #, Action Return)

# WE ASSUME 'AAPL' IS THE ONLY TRADED STOCK.


class Trader(MyThread):
    def __init__(self, id):
        super().__init__(id)
        self.book_position = 0
        self.balance_track = [1000000]
        # the traders each start with a balance of 1,000,000 and nothing on the books
        # each trader is a thread

    def place_limit_order(self, quantity=None, price=None, side=None):
        # Make sure the limit order given has the parameters necessary to construct the order
        # It's your choice how to implement the orders that do not have enough information
        
        # The 'order' returned must be of type LimitOrder
        
        # Make sure you modify the book position after the trade
        # You must return a tuple of the following:
        # (the action type enum, the id of the trader, and the order to be executed)
        pass

    def place_market_order(self, quantity=None, side=None):
        # Make sure the market order given has the parameters necessary to construct the order
        # It's your choice how to implement the orders that do not have enough information
        
        # The 'order' returned must be of type MarketOrder
        
        # Make sure you modify the book position after the trade
        # You must return a tuple of the following:
        # (the action type enum, the id of the trader, and the order to be executed)
        pass

    def place_ioc_order(self, quantity=None, price=None, side=None):
        # Make sure the ioc order given has the parameters necessary to construct the order
        # It's your choice how to implement the orders that do not have enough information
        
        # The 'order' returned must be of type IOCOrder
        
        # Make sure you modify the book position after the trade
        # You must return a tuple of the following:
        # (the action type enum, the id of the trader, and the order to be executed)
        pass

    def amend_quantity(self, quantity=None):
        # It's your choice how to implement the 'Amend' action where quantity is not given
        
        # You must return a tuple of the following:
        # (the action type enum, the id of the trader, and quantity to change the order by)
        pass

    def cancel_order(self):
        # You must return a tuple of the following:
        # (the action type enum, the id of the trader)
        pass

    def balance_and_position(self):
        # You must return a tuple of the following:
        # (the action type enum, the id of the trader)
        pass

    def process_response(self, response):
        # Implement this function
        # You need to process each order according to the type (by enum) given by the 'response' variable
        
        # If the action taken by the trader is ambiguous you need to raise the following error
        raise UndefinedResponse("Undefined Response Received!")

    def random_action(self):
        # Implement this function
        # According to the status of whether you have a position on the book and the action chosen
        # the trader needs to be able to take a separate action
        
        # The action taken can be random or deterministic, your choice

    def run_infinite_loop(self):
        # The trader needs to continue to take actions until the book balance falls to 0
        # While the trader can take actions, it chooses from a random_action and uploads the action
        # to the exchange
        
        #The trader then takes any received responses from the exchange and processes it
        


class Exchange(MyThread):
    def __init__(self):
        super().__init__()
        self.balance = [1000000 for _ in range(100)]
        self.position = [0 for _ in range(100)]
        self.matching_engine = MatchingEngine()
        # The exchange keeps track of the traders' balances
        # The exchange uses the matching engine you built previously

    def place_new_order(self, order):
        # The exchange must use the matching engine to handle orders given
        results = []
        # The list of results is expected to contain a tuple of the follow form:
        # (Trader id that processed the order, (action type enum, order))
        
        # The exchange must update the balance of positions of each trader involved in the trade (if any)
        
        return results

    def amend_quantity(self, id, quantity):
        # The matching engine must be able to process the 'amend' action based on the given parameters
        
        # Keep in mind of any exceptions that may be thrown by the matching engine while handling orders
        # The return must be in the form (action type enum, logical based on if order processed)
        pass

    def cancel_order(self, id):
        # The matching engine must be able to process the 'cancel' action based on the given parameters
        
        # Keep in mind of any exceptions that may be thrown by the matching engine while handling orders
        # The return must be in the form (action type enum, logical based on if order processed)
        pass

    def balance_and_position(self, id):
        # The matching engine must be able to process the 'balance' action based on the given parameters
        
        # The return must be in the form (action type enum, (trader balance, trader positions))
        pass

    def handle_request(self, request):
        # The exchange must be able to process different types of requests based on the action
        # type given using the functions implemented above
        
        # You must raise the following exception if the action given is ambiguous
        raise UndefinedTraderAction("Undefined Trader Action!")

    def run_infinite_loop(self):
        # The exchange must continue handling orders as orders are issued by the traders
        # A way to do this is check if there are any orders waiting to be processed in the deque
        
        # If there are, handle the request using the functions built above and using the
        # corresponding trader's deque, return an acknowledgement based on the response

if __name__ == "__main__":

    trader = [Trader(i) for i in range(100)]
    exchange = Exchange()

    exchange.start()
    for t in trader:
        t.start()

    exchange.join()
    for t in trader:
        t.join()

    sum_exch = 0
    for t in MyThread.list_of_threads:
        if t.id == "NoID":
            for b in t.balance:
                sum_exch += b

    print("Total Money Amount for All Traders before Trading Session: " + str(sum_exch))

    for i in range(10000):
        thread_active = False
        for t in MyThread.list_of_threads:
            if t.is_started:
                t.run_infinite_loop()
                thread_active = True
        if not thread_active:
            break

    sum_exch = 0
    for t in MyThread.list_of_threads:
        if t.id == "NoID":
            for b in t.balance:
                sum_exch += b

    print("Total Money Amount for All Traders after Trading Session: ", str(int(sum_exch)))
