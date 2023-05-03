vegetable = {}

while True:
    vegetable = input("vegetable name: ")
    if vegetable == 'done':
        break
    price = input("Item price: ")
    vegetable[vegetable] = price

vegetable_list = {}

while True:
    vegetable = input("vegetable name: ")
    if vegetable == 'done':
        break
    qty = input("How many: ")
    vegetable_list[vegetable] = qty
class Vegetable:
  def __init__(self):
    self.items = {}
  def run(self):
    while True:
      x = input('enter item: ')
      if x =='done':
          break
      y = float(input('enter price: '))
      self.items[x] = {"Price": y}
    def get_totals(self):
     for j in self.items.keys():
      self.items[j]["Quantity"] = int(input('enter how many {} you want: '.format(j)))
      self.items[j]["Total"] = self.items[j]["Quantity"] * self.items[j]["Price"]
vegetable = Vegetable()

vegetable.run()