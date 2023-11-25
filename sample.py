
class ShoppingCart:
  
  def __init__(self):
    self.hmap={}
  def addProduct(self,name,price,gst,quantity):
    if price>=500:
      price=price-(price*(5/100))
      self.hmap[name]=[price,gst,quantity]
    else:
      self.hmap[name]=[price,gst,quantity]
  
  def findmaximum(self):
    maxx=0
    name=""
    for i,j in self.hmap.items():
      price,gst,quantity=j
      val=(price+(price*(gst/100)))*quantity
      if val>maxx:
        maxx=val
        name=i
    return name
  def total(self):
    val=0
    for i,j in self.hmap.items():
      
      price,gst,quantity=j
      val=val+((price+(price*(gst/100)))*quantity)
    return val


ob=ShoppingCart()
ob.addProduct('leather_wallet',1100,18,1)
ob.addProduct('umbrella',900,12,4)
ob.addProduct('cigarette',200,28,3)
ob.addProduct('honey',100,0,2)
name=ob.findmaximum()
print(name)
total_amount=ob.total()
print(total_amount)