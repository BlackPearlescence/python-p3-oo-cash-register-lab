#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.itemdict = {}

  def add_item(self,item,price,qty = 1):
    for i in range(qty):
      self.items.append(item)
      self.itemdict[item] = [price,qty]
    self.total += price * qty
  def apply_discount(self):
    if(self.discount == 0):
      print("There is no discount to apply.")
    else:
      self.total -= (self.discount * self.total) // 100
      print(f"After the discount, the total comes to ${self.total}.")
  def get_purchases(self):
    return {*self.items}

  def get_all_purchases(self):
    return self.items

  # def void_last_transaction(self):
  #   lastitem = self.items[-1]
  #   lastprice = self.itemdict[lastitem][0]
  #   self.total -= lastprice
  #   self.items.pop(-1)

  def void_last_transaction(self):
      lastitem = self.items[-1]
      lastprice = self.itemdict[lastitem][0]
      print(lastprice)
      lastqty = self.itemdict[lastitem][1]
      print(lastqty)
      self.total -= (lastprice * lastqty)
      for i in range(lastqty):
        self.items.pop(-1)
      if(self.items == []):
        self.total = 0.0
    

cash = CashRegister()
cash.add_item("tomato",1.76,2)
cash.void_last_transaction()
print(cash.total)
    # lastitems = self.items[:self.itemdict[lastitem][1]]

