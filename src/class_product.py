
class Product:
    """Класс для описания продукта """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, params, list_for_check):

        for instance in list_for_check:
            if params['name'].lower() == instance.name.lower():

                new_quantity = params['quantity'] + instance.quantity
                new_price = max(params['price'], instance.__price)

                instance.quantity = new_quantity
                instance.price = new_price
                return instance

        return cls(name=params['name'],
                   description=params['description'],
                   price=params['price'],
                   quantity=params['quantity'])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        elif price < self.__price:
            print('Вы уверены, что хотите снизить цену товара?')
            print('y - да, n - нет')
            user_input = input('Ввод: ')
            if user_input.lower().strip() == 'y':
                self.__price = price
        else:
            self.__price = price
