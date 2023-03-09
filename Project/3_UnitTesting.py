import time

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


from abc import ABC


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
    def __init__(self, id, symbol, quantity, price, side, time, limit = False):
        super().__init__(id, symbol, quantity, side, time)
        self.price = price
        self.limit = limit
        



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

# You need to build additional unittests for your implementation
import unittest

class TestOrderBook(unittest.TestCase):
    
    # The unittests must start with "test", change the function name to something that makes sense
    def test_handle_order_limit(self):
        # implement this unittest and three more 
        matching_engine = MatchingEngine()
        order = LimitOrder(1, "S", 10, 10, OrderSide.BUY, time.time())
        matching_engine.insert_limit_order(order)

        order_1 = LimitOrder(2, "S", 5, 10, OrderSide.BUY, time.time())
        order_2 = LimitOrder(3, "S", 10, 15, OrderSide.BUY, time.time())
        matching_engine.handle_order(order_1)
        matching_engine.handle_order(order_2)

        self.assertEqual(matching_engine.bid_book[0].price, 15)
        self.assertEqual(matching_engine.bid_book[1].quantity, 10)

        order_sell = LimitOrder(4, "S", 14, 8, OrderSide.SELL, time.time())
        filled_orders = matching_engine.handle_order(order_sell)

        self.assertEqual(matching_engine.bid_book[0].quantity, 6)
        self.assertEqual(filled_orders[0].id, 3)
        self.assertEqual(filled_orders[0].price, 15)
        self.assertEqual(filled_orders[2].id, 1)
        self.assertEqual(filled_orders[2].price, 10)
    
    def test_handle_order_market(self):
        matching_engine = MatchingEngine()
        order_1 = LimitOrder(1, "S", 6, 10, OrderSide.BUY, time.time())
        order_2 = LimitOrder(2, "S", 5, 10, OrderSide.BUY, time.time())
        matching_engine.handle_order(order_1)
        matching_engine.handle_order(order_2)

        order = MarketOrder(5, "S", 5, OrderSide.SELL, time.time())
        filled_orders = matching_engine.handle_order(order)
        self.assertEqual(matching_engine.bid_book[0].quantity, 1)
        self.assertEqual(filled_orders[0].price, 10)
    
    def test_handle_order_ioc(self):
        matching_engine = MatchingEngine()
        order_1 = LimitOrder(1, "S", 1, 10, OrderSide.BUY, time.time())
        order_2 = LimitOrder(2, "S", 5, 10, OrderSide.BUY, time.time())
        matching_engine.handle_order(order_1)
        matching_engine.handle_order(order_2)

        order = IOCOrder(6, "S", 5, 12, OrderSide.SELL, time.time())
        filled_orders = matching_engine.handle_order(order)
        self.assertEqual(matching_engine.bid_book[0].quantity, 1)
        self.assertEqual(len(filled_orders), 0)
    
    def test_amend(self):
        matching_engine = MatchingEngine()
        order_1 = LimitOrder(1, "S", 4, 12, OrderSide.BUY, time.time())
        order_2 = LimitOrder(2, "S", 15, 20, OrderSide.BUY, time.time())
        matching_engine.handle_limit_order(order_1)
        matching_engine.handle_limit_order(order_2)

        matching_engine.amend_quantity(2, 8)
        self.assertEqual(matching_engine.bid_book[0].quantity, 8)
    
# A few example unittests are provided below


    def test_insert_limit_order(self):
        matching_engine = MatchingEngine()
        order = LimitOrder(1, "S", 10, 10, OrderSide.BUY, time.time())
        matching_engine.insert_limit_order(order)

        self.assertEqual(matching_engine.bid_book[0].quantity, 10)
        self.assertEqual(matching_engine.bid_book[0].price, 10)
    
    def test_handle_limit_order(self):
        matching_engine = MatchingEngine()
        order = LimitOrder(1, "S", 10, 10, OrderSide.BUY, time.time())
        matching_engine.insert_limit_order(order)

        order_1 = LimitOrder(2, "S", 5, 10, OrderSide.BUY, time.time())
        order_2 = LimitOrder(3, "S", 10, 15, OrderSide.BUY, time.time())
        matching_engine.handle_limit_order(order_1)
        matching_engine.handle_limit_order(order_2)

        self.assertEqual(matching_engine.bid_book[0].price, 15)
        self.assertEqual(matching_engine.bid_book[1].quantity, 10)

        order_sell = LimitOrder(4, "S", 14, 8, OrderSide.SELL, time.time())
        filled_orders = matching_engine.handle_limit_order(order_sell)

        self.assertEqual(matching_engine.bid_book[0].quantity, 6)
        self.assertEqual(filled_orders[0].id, 3)
        self.assertEqual(filled_orders[0].price, 15)
        self.assertEqual(filled_orders[2].id, 1)
        self.assertEqual(filled_orders[2].price, 10)
    
    def test_handle_market_order(self):
        matching_engine = MatchingEngine()
        order_1 = LimitOrder(1, "S", 6, 10, OrderSide.BUY, time.time())
        order_2 = LimitOrder(2, "S", 5, 10, OrderSide.BUY, time.time())
        matching_engine.handle_limit_order(order_1)
        matching_engine.handle_limit_order(order_2)

        order = MarketOrder(5, "S", 5, OrderSide.SELL, time.time())
        filled_orders = matching_engine.handle_market_order(order)
        self.assertEqual(matching_engine.bid_book[0].quantity, 1)
        self.assertEqual(filled_orders[0].price, 10)

    def test_handle_ioc_order(self):
        matching_engine = MatchingEngine()
        order_1 = LimitOrder(1, "S", 1, 10, OrderSide.BUY, time.time())
        order_2 = LimitOrder(2, "S", 5, 10, OrderSide.BUY, time.time())
        matching_engine.handle_limit_order(order_1)
        matching_engine.handle_limit_order(order_2)

        order = IOCOrder(6, "S", 5, 12, OrderSide.SELL, time.time())
        filled_orders = matching_engine.handle_ioc_order(order)
        self.assertEqual(matching_engine.bid_book[0].quantity, 1)
        self.assertEqual(len(filled_orders), 0)
    
    def test_amend_quantity(self):
        matching_engine = MatchingEngine()
        order_1 = LimitOrder(1, "S", 5, 10, OrderSide.BUY, time.time())
        order_2 = LimitOrder(2, "S", 10, 15, OrderSide.BUY, time.time())
        matching_engine.handle_limit_order(order_1)
        matching_engine.handle_limit_order(order_2)

        matching_engine.amend_quantity(2, 8)
        self.assertEqual(matching_engine.bid_book[0].quantity, 8)
    
    def test_cancel_order(self):
        matching_engine = MatchingEngine()
        order_1 = LimitOrder(1, "S", 5, 10, OrderSide.BUY, time.time())
        order_2 = LimitOrder(2, "S", 10, 15, OrderSide.BUY, time.time())
        matching_engine.handle_limit_order(order_1)
        matching_engine.handle_limit_order(order_2)

        matching_engine.cancel_order(1)
        self.assertEqual(matching_engine.bid_book[0].id, 2)

import io
import __main__
suite = unittest.TestLoader().loadTestsFromModule(__main__)
buf = io.StringIO()
unittest.TextTestRunner(stream=buf, verbosity=2).run(suite)
buf = buf.getvalue().split("\n")
sum=0
for test in buf:
	if test.startswith("test"):
		sum+=1
        
print("You have %d unit tests" % (sum))

