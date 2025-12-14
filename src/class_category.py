from src.base_category import BaseCategory
from src.class_product import Product


class Category(BaseCategory):
    """Класс для представления категорий """
    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f'{self.name}, количество продуктов: {total_quantity} шт.'

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            self.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        return '\n'.join(str(product) for product in self.__products)

    @property
    def total_quantity(self):
        """Возвращает количество всех товаров в категории"""
        return sum(product.quantity for product in self.__products)

    @property
    def total_cost(self):
        """Возвращает сумму всех товаров в категории"""
        return sum(product.price * product.quantity for product in self.__products)

    def middle_price(self):
        """Возвращает среднюю цену всех товаров"""
        try:
            total_cost = self.total_cost
            result = total_cost / len(self.__products)
        except ZeroDivisionError:
            return 0
        else:
            return result
