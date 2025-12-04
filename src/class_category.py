
class Category:
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

    def add_product(self, product):
        self.__products.append(product)
        self.product_count += 1

    @property
    def products(self):
        result = ''
        for product in self.__products:
            result += f"{product.name}, {product.price}. руб. Остаток: {product.quantity} шт."
        return result
