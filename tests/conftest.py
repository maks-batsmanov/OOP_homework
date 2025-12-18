import pytest

from src.class_category import Category
from src.class_product import Product


@pytest.fixture
def product_labubu():
    return Product('Labubu', 'toy', 100.00, 10)


@pytest.fixture
def category_books():
    result_1 = Product('Harry Potter', 'fantasy', 100, 10)
    result_2 = Product('Lord of the Rings', 'fantasy', 120, 9)
    result_3 = Product('The Chronicles of Narnia', 'fantasy', 130, 12)
    result = Category('books', 'fantasy', [result_1, result_2, result_3])
    return result


@pytest.fixture
def list_for_comparison():
    result_1 = Product('teddy', 'toy', 50.00, 6)
    result_2 = Product('toy car', 'toy', 120.00, 9)
    result_3 = Product('Labubu', 'toy', 90, 4)
    return [result_1, result_2, result_3]


@pytest.fixture
def category_books_product_zero():
    result = Category('books', 'fantasy', [])
    return result


@pytest.fixture
def product_labubu_dict():
    return {'name': 'Labubu', 'description': 'toy', 'price': 100.00, 'quantity': 10}


@pytest.fixture
def init_product():
    result = Product('teddy', 'toy', 50.00, 6)
    return result
