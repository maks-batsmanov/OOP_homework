import pytest

from src.class_category import Category
from src.class_product import Product


def test_init_category(category_books):
    assert category_books.name == "books"
    assert category_books.description == "fantasy"
    assert category_books.products == (
        "Harry Potter, 100 руб. Остаток: 10 шт.\n"
        "Lord of the Rings, 120 руб. Остаток: 9 шт.\n"
        "The Chronicles of Narnia, 130 руб. Остаток: 12 шт."
    )


def test_count_product(category_books):
    Category.category_count = 0
    Category.product_count = 0

    Category.category_count += 1
    Category.product_count += len(category_books._Category__products)

    assert Category.product_count == 3
    assert Category.category_count == 1


def test_add_product(category_books):
    new_product = Product("Twenty thousand leagues under the sea", "fantasy", 300, 2)
    category_books.add_product(new_product)
    assert category_books.products == (
        "Harry Potter, 100 руб. Остаток: 10 шт.\n"
        "Lord of the Rings, 120 руб. Остаток: 9 шт.\n"
        "The Chronicles of Narnia, 130 руб. Остаток: 12 шт.\n"
        "Twenty thousand leagues under the sea, 300 руб. Остаток: 2 шт."
    )
    error_product = 'Not product'
    with pytest.raises(TypeError):
        category_books.add_product(error_product)


def test_category_str(category_books):
    result = str(category_books)
    assert result == 'books, количество продуктов: 31 шт.'
