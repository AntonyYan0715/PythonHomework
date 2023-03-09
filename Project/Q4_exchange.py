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
        filled_orders = self.matching_engine.handle_order(order)
        results = []
        for o in filled_orders:
            results.append((o.id,(1,o)))
        # The list of results is expected to contain a tuple of the follow form:
        # (Trader id that processed the order, (action type enum, order))
        
        # The exchange must update the balance of positions of each trader involved in the trade (if any)
        
        return results

    def amend_quantity(self, id, quantity):
        # The matching engine must be able to process the 'amend' action based on the given parameters
        
        # Keep in mind of any exceptions that may be thrown by the matching engine while handling orders
        # The return must be in the form (action type enum, logical based on if order processed)
        result = self.matching_engine.amend_quantity(id,quantity)
        return (2, result)
        

    def cancel_order(self, id):
        # The matching engine must be able to process the 'cancel' action based on the given parameters
        
        # Keep in mind of any exceptions that may be thrown by the matching engine while handling orders
        # The return must be in the form (action type enum, logical based on if order processed)
        result = self.matching_engine.cancel_order(id)
        return (3, result)

    def balance_and_position(self, id):
        # The matching engine must be able to process the 'balance' action based on the given parameters
        
        # The return must be in the form (action type enum, (trader balance, trader positions))
        return (4, (self.balance[id],self.position[id]))

    def handle_request(self, request):
        # The exchange must be able to process different types of requests based on the action
        # type given using the functions implemented above
        
        # You must raise the following exception if the action given is ambiguous
        if request[0] == 1:
            result = self.place_new_order(request[2])
            exchange_to_trader[self.request[1]].appendleft(result)
        if request[0] == 2:
            result = self.amend_quantity(request[1],request[2])
            exchange_to_trader[self.request[1]].appendleft(result)
        if request[0] == 2:
            result = self.cancel_order(request[1])
            exchange_to_trader[self.request[1]].appendleft(result)
        if request[0] == 3:
            result = self.balance_and_position(request[1])
            exchange_to_trader[self.request[1]].appendleft(result)    
        raise UndefinedTraderAction("Undefined Trader Action!")

    def run_infinite_loop(self):
        # The exchange must continue handling orders as orders are issued by the traders
        # A way to do this is check if there are any orders waiting to be processed in the deque
        
        # If there are, handle the request using the functions built above and using the
        # corresponding trader's deque, return an acknowledgement based on the response
        while len(trader_to_exchange) != 0:
            request = trader_to_exchange.pop()
            self.handle_request(request)