# This program creates the class file and the program file together
# NOTE: wherever you see 'xxxx', that means there is code missing and
# is to be completed by you.


#Class definition (part 1) 

class RetailItem():
    def __init__(self,desc,units,price):
        self.__desc = desc
        self.__units = units
        self.__price = price

    def get_desc(self):
        return self.__desc
    
    def get_units(self):
        return self.__units
    
    def get_price(self):
        return self.__price

    def set_desc(self, desc):
        self.__desc = desc
        
    def set_units(self,units):
        self.__units = units


    def set_price(self,price):
        self.__price = price


# program (part 2)

# create instances
item1 = RetailItem('Jacket',12,59.95)
item2 = RetailItem('Designer Jeans',40,34.95)
item3 = RetailItem('Shirt',20,24.95)



# print out desc and price

print(f"{item1.get_desc()}: ${item1.get_price()}")
print(f"{item2.get_desc()}: ${item2.get_price()}")
print(f"{item3.get_desc()}: ${item3.get_price()}")

        



    
