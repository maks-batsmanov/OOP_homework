# Задание 1
# Создайте классы Product и Category. Для класса Product определите следующие свойства:
# название (name),описание (description),цена (
# price),количество в наличии (quantity). Для класса
# Category определите следующие свойства:название (name),
# описание (description),список товаров категории (products).
#атрибуты #типы_данных #создание_класса #class
from unicodedata import category


class Product:
    """Класс для описания продукта """
    name: str
    description: str
    price: float
    quantity: int


    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категорий """
    name: str
    description: str
    products: list


    count_of_category = 0
    count_of_products = 0


    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.count_of_category += 1
        Category.count_of_products += len(products)

# category_1 = Category('Ozon', 'marketplace', ['labubu'])
# # category_2 = Category('WB', 'marketplace', 'guitar')
#
# #
# # if __name__ == '__main__':
# #     print(category_1.name, category_1.description, category_1.products, Category.count_of_products)
# #     print()
# # # Category.count_of_category