from src.base_category import BaseCategory
from src.class_product import Product


class Order(BaseCategory):

    def __init__(self, product, sold):
        self.product = product
        self.sold = sold

    def __str__(self):
        """Выводит название продукта, его количества, итоговую стоимость"""
        return f'{self.product.name}, количество проданных продуктов: {self.sold}, итоговая цена: {self.total_cost} руб.'

    @property
    def total_cost(self):
        """Возвращает итоговую стоимость продукта"""
        return self.product.price * self.sold

    @property
    def total_quantity(self):
        """Возвращает количество купленного товара"""
        return self.sold
