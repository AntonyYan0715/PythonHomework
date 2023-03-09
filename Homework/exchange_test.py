import re
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

def test_exchange_add_constructor():
  sending_time = time.time()
  sequence_number = random.randint(0, 50)
  price = random.randint(100, 200)
  quantity = random.randint(1, 10)
  price_id = random.randint(1000, 9999)

  msg = ExchangeAddMessage(sending_time, sequence_number, price, quantity, price_id)
  assert(msg.getSendingTime() == sending_time)
  assert(msg.getSequenceNumber() == sequence_number)
  assert(msg.getPrice() == price)
  assert(msg.getQuantity() == quantity)
  assert(msg.getPriceId() == price_id)

def test_exchange_modify_constructor():
  sending_time = time.time()
  sequence_number = random.randint(0, 50)
  price = random.randint(100, 200)
  quantity = random.randint(1, 10)
  last_quantity = random.randint(1, 10)
  price_id = random.randint(1000, 9999)

  msg = ExchangeModifyMessage(sending_time, sequence_number, price, quantity, last_quantity, price_id)
  assert(msg.getSendingTime() == sending_time)
  assert(msg.getSequenceNumber() == sequence_number)
  assert(msg.getPrice() == price)
  assert(msg.getQuantity() == quantity)
  assert(msg.getLastQuantity() == last_quantity)
  assert(msg.getPriceId() == price_id)

def test_exchange_delete_constructor():
  sending_time = time.time()
  sequence_number = random.randint(0, 50)
  price = random.randint(100, 200)
  price_id = random.randint(1000, 9999)

  msg = ExchangeDeleteMessage(sending_time, sequence_number, price, price_id)
  assert(msg.getSendingTime() == sending_time)
  assert(msg.getSequenceNumber() == sequence_number)
  assert(msg.getPrice() == price)
  assert(msg.getPriceId() == price_id)

def test_add():
  test_add_inheritance_check()

  sending_time = time.time()
  sequence_number = random.randint(0, 50)
  price = random.randint(100, 200)
  quantity = random.randint(1, 10)
  price_id = random.randint(1000, 9999)

  strat = Strategy()
  ex = Decoder(strat)
  msg = ExchangeAddMessage(sending_time, sequence_number, price, quantity, price_id)
  ex.processExchangeAddMessage(msg)

  with redirect_stdout(io.StringIO()) as f:
    strat.printQueue()
  s = f.getvalue()

  comp = "AddMesssage sending_time {0} sequence_number {1} price {2} quantity {3}\n".format(sending_time, sequence_number, price, quantity)

  assert(s == comp)

def test_modify():
  test_modify_inheritance_check()

  sending_time = time.time()
  sequence_number = random.randint(0, 50)
  price = random.randint(100, 200)
  quantity = random.randint(1, 10)
  last_quantity = random.randint(1, 10)
  price_id = random.randint(1000, 9999)

  strat = Strategy()
  ex = Decoder(strat)
  msg = ExchangeModifyMessage(sending_time, sequence_number, price, quantity, last_quantity, price_id)
  ex.processExchangeModifyMessage(msg)

  with redirect_stdout(io.StringIO()) as f:
    strat.printQueue()
  s = f.getvalue()

  comp = "ModifyMesssage sending_time {0} sequence_number {1} price {2} quantity {3} last_quantity {4}\n".format(sending_time, sequence_number, price, quantity, last_quantity)

  assert(s == comp)

def test_delete():
  test_delete_inheritance_check()

  sending_time = time.time()
  sequence_number = random.randint(0, 50)
  price = random.randint(100, 200)
  price_id = random.randint(1000, 9999)

  strat = Strategy()
  ex = Decoder(strat)
  msg = ExchangeDeleteMessage(sending_time, sequence_number, price, price_id)
  ex.processExchangeDeleteMessage(msg)

  with redirect_stdout(io.StringIO()) as f:
    strat.printQueue()
  s = f.getvalue()

  comp = "DeleteMesssage sending_time {0} sequence_number {1} price {2}\n".format(sending_time, sequence_number, price)

  assert(s == comp)

def test_multiple():
  inheritance_check()

  sending_time = time.time()
  sequence_number = random.randint(0, 50)
  price = random.randint(100, 200)
  quantity = random.randint(1, 10)
  last_quantity = random.randint(1, 10)
  price_id = random.randint(1000, 9999)

  strat = Strategy()
  ex = Decoder(strat)
  msg = ExchangeAddMessage(sending_time, sequence_number, price, quantity, price_id)
  ex.processExchangeAddMessage(msg)
  msg = ExchangeModifyMessage(sending_time + 1, sequence_number + 1, price, quantity, last_quantity, price_id)
  ex.processExchangeModifyMessage(msg)
  msg = ExchangeDeleteMessage(sending_time + 2, sequence_number + 2, price, price_id)
  ex.processExchangeDeleteMessage(msg)

  with redirect_stdout(io.StringIO()) as f:
    strat.printQueue()
  s = f.getvalue()

  comp = "AddMesssage sending_time {0} sequence_number {1} price {2} quantity {3}\n".format(sending_time, sequence_number, price, quantity)
  comp += "ModifyMesssage sending_time {0} sequence_number {1} price {2} quantity {3} last_quantity {4}\n".format(sending_time + 1, sequence_number + 1, price, quantity, last_quantity)
  comp += "DeleteMesssage sending_time {0} sequence_number {1} price {2}\n".format(sending_time + 2, sequence_number + 2, price)

  assert(s == comp)

def get_writeable_properties(cls):
  return [attr for attr, value in vars(cls).items()
     if isinstance(value, property) and value.fset is not None]

def test_add_message():
  test_add_inheritance_check()

  sending_time = time.time()
  sequence_number = random.randint(0, 50)
  price = random.randint(100, 200)
  quantity = random.randint(1, 10)

  message = AddMessage()

  message.sending_time = sending_time
  message.sequence_number = sequence_number
  message.price = price
  message.quantity = quantity

  assert(message.sending_time == sending_time)
  assert(message.sequence_number == sequence_number)
  assert(message.price == price)
  assert(message.quantity == quantity)

def test_modify_message():
  test_modify_inheritance_check()

  sending_time = time.time()
  sequence_number = random.randint(0, 50)
  price = random.randint(100, 200)
  quantity = random.randint(1, 10)
  last_quantity = random.randint(1, 10)

  message = ModifyMessage()

  message.sending_time = sending_time
  message.sequence_number = sequence_number
  message.price = price
  message.quantity = quantity
  message.last_quantity = last_quantity

  assert(message.sending_time == sending_time)
  assert(message.sequence_number == sequence_number)
  assert(message.price == price)
  assert(message.quantity == quantity)
  assert(message.last_quantity == last_quantity)

def test_delete_message():
  test_delete_inheritance_check()

  sending_time = time.time()
  sequence_number = random.randint(0, 50)
  price = random.randint(100, 200)

  message = DeleteMessage()

  message.sending_time = sending_time
  message.sequence_number = sequence_number
  message.price = price

  assert(message.sending_time == sending_time)
  assert(message.sequence_number == sequence_number)
  assert(message.price == price)

def inheritance_check():
  test_add_inheritance_check()
  test_modify_inheritance_check()
  test_delete_inheritance_check()

def test_add_inheritance_check():
  message = AddMessage()

  assert(issubclass(AddMessage, Message))

  assert(len(get_writeable_properties(AddMessage)) > 0)

  assert(message.__dict__ == {'_AddMessage__price': 0, '_AddMessage__quantity': 0, '_Message__sending_time': 0, '_Message__sequence_number': 0, '_Message__message_type': MessageType.ADD})

  assert(message.__repr__() == "DoNotImplement")
  assert(message.__str__() == "DoNotImplement")

def test_modify_inheritance_check():
  message = ModifyMessage()

  assert(issubclass(ModifyMessage, Message))

  assert(len(get_writeable_properties(ModifyMessage)) > 0)

  assert(message.__dict__ == {'_ModifyMessage__price': 0, '_ModifyMessage__last_quantity': 0, '_ModifyMessage__quantity': 0, '_Message__sending_time': 0, '_Message__sequence_number': 0, '_Message__message_type': MessageType.MODIFY})

  assert(message.__repr__() == "DoNotImplement")
  assert(message.__str__() == "DoNotImplement")

def test_delete_inheritance_check():
  message = DeleteMessage()

  assert(issubclass(DeleteMessage, Message))

  assert(len(get_writeable_properties(DeleteMessage)) > 0)

  assert(message.__dict__ == {'_DeleteMessage__price': 0, '_Message__sending_time': 0, '_Message__sequence_number': 0, '_Message__message_type': MessageType.DELETE})

  assert(message.__repr__() == "DoNotImplement")
  assert(message.__str__() == "DoNotImplement")

def test_negative_quantity_add():
  test_add_inheritance_check()

  sending_time = time.time()
  sequence_number = random.randint(0, 50)
  price = random.randint(100, 200)
  quantity = random.randint(-10, -1)
  price_id = random.randint(1000, 9999)

  strat = Strategy()
  ex = Decoder(strat)
  msg = ExchangeAddMessage(sending_time, sequence_number, price, quantity, price_id)

  try:
    ex.processExchangeAddMessage(msg)
  except NegativeQuantityException:
    assert(True)
  else:
    assert(False)

def test_negative_quantity_modify():
  test_modify_inheritance_check()

  sending_time = time.time()
  sequence_number = random.randint(0, 50)
  price = random.randint(100, 200)
  quantity = random.randint(-10, -1)
  last_quantity = random.randint(1, 10)
  price_id = random.randint(1000, 9999)

  strat = Strategy()
  ex = Decoder(strat)
  msg = ExchangeModifyMessage(sending_time, sequence_number, price, quantity, last_quantity, price_id)

  try:
    ex.processExchangeModifyMessage(msg)
  except NegativeQuantityException:
    assert(True)
  else:
    assert(False)
    
@negative_value_checker
def test_decorator_1(var1, var2, var3, var4, var5, var6, var7):
  assert(False)

@negative_value_checker
def test_decorator_2(var1, var2, var3, var4, var5, var6):
  assert(False)

@negative_value_checker
def test_decorator_3(var1, var2, var3, var4):
  assert(True)

def test_decorator():
  sending_time = time.time()
  sequence_number = random.randint(0, 50)
  price = random.randint(100, 200)
  quantity = random.randint(1, 10)
  last_quantity = random.randint(1, 10)
  price_id = -1

  strat = Strategy()
  ex = Decoder(strat)

  try:
    test = ExchangeAddMessage(sending_time, sequence_number, price, quantity, price_id)
    assert(False)
  except:
    assert(True)

  try:
    test = ExchangeModifyMessage(sending_time, sequence_number, price, quantity, last_quantity, price_id)
    assert(False)
  except:
    assert(True)

  try:
    test = ExchangeDeleteMessage(sending_time, sequence_number, price, price_id)
    assert(False)
  except:
    assert(True)

  try:
    test_decorator_1(sending_time, sequence_number, price, quantity, price_id)
  except:
    assert(True)

  try:
    test_decorator_2(sending_time, sequence_number, price, quantity, last_quantity, price_id)
  except:
    assert(True)

  test_decorator_3(sending_time, sequence_number, price, price_id)
    
if __name__ == '__main__':
    func_name = input().strip()
    globals()[func_name]()