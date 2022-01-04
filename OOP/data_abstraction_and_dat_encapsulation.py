class Product:
    def __init__(self):
        self.__product_name = " "
        self.__product_id = " "
        self.__product_price = 0

    def set_product(self, p_name, p_id, p_price):
        self.__product_name = p_name
        self.__product_id = p_id
        self.__product_price = p_price

    def show_product(self):
        print(
            f"Product Name : {self.__product_name}\nProduct Id : {self.__product_id}\nProduct Price : {self.__product_price} ")


tv = Product()
tv.set_product("LED SONY TV", "#12F45", 22000)

# tv.__product_name = "faltu tv"
# tv.__product_price = 100000

tv.show_product()
#
# print(tv.__product_name) it will give error no attribute __product_name found
print(tv.__dict__)
