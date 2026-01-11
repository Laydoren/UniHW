class Product:
    def __init__(self, name, price, weight):
        self.__name = name
        self.__price = price
        self.__weight = weight

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight


class Buy(Product):
    def __init__(self, name, price, weight, count):
        super().__init__(name, price, weight)
        self.__count = count
        self.__total_cost = price * count
        self.__total_weight = weight * count

    def get_count(self):
        return self.__count

    def set_count(self, value):
        self.__count = value
        self.__total_cost = self.get_price() * value
        self.__total_weight = self.get_weight() * value

    def get_total_cost(self):
        return self.__total_cost

    def get_total_weight(self):
        return self.__total_weight


class Check(Buy):
    def display_info(self):
        print(f"Наименование: {self.get_name()}")
        print(f"Цена: {self.get_price()}")
        print(f"Вес за ед.: {self.get_weight()}")
        print(f"Количество: {self.get_count()}")
        print(f"Итоговая цена: {self.get_total_cost()}")
        print(f"Итоговый вес: {self.get_total_weight()}")


receipt = Check("Груши", 150, 2, 5)
receipt.display_info()