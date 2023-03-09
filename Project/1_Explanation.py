'''
We create a parent class "Order" to represent the orders. Parent class "Order" has "id", "symbol", "quantity", "side", and "time", five attributes.

Then we create four child classes that are inherited from the parent class "Order" to represent limit orders ("LimitOrder"), market orders ("MarketOrder"), IOC orders ("IOCOrder"), and the orders that are filled through the trading processes ("FilledOrder").

We create the class "MatchingEngine" which has seven methods: "handle_limit_order", "handle_market_order", "handle_ioc_order", "handle_order", "insert_limit_order", "amend_quantity", and "cancel_order". And "MatchingEngine" also has two lists, "bid_book" and "ask_book".

"handle_limit_order" accepts a limit order ("LimitOrder" object) as a parameter and checks if the limit order's price crosses the book. If the price crosses the book, it can be filled or at least partially filled. We can use the "insert_limit_order" method to place the order into the order book if its price doesn't cross the book.

"handle_market_order" accepts a market order ("MarketOrder" object) as a parameter and immediately uses orders in the order book to fill it.

"handle_ioc_order" accepts an IOC order ("IOCOrder" object) as a parameter and checks if the IOC order's price crosses the book. If the price crosses the book, it can be filled or partially filled, and the part that cannot be filled will cancel immediately, instead of being placed into the order book.

"handle_order" can accept any one of limit orders, market orders, or IOC orders as a parameter and uses an appropriate method to handle it. It is constructed by "handle_limit_order", "handle_market_order", and "handle_ioc_order".

And we can use method "amend_quantity" to reduce the quantity of an order with a specific "id", or use method "cancel_order" to cancel an order with a specific "id".

'''