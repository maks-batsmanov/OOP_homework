import pytest
from src.class_category import Category
from src.class_product import Product


@pytest.fixture
def product_labubu():
    return Product('Labubu', 'toy', 100.00, 10 )


@pytest.fixture
def category_books():
    return Category('books', 'fantasy',
                    ['Harry Potter', 'Lord of the Rings', 'The Chronicles of Narnia'])