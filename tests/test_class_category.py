from src.classes import Category


def test_init_category(category_books):
    assert category_books.name == 'books'
    assert category_books.description == 'fantasy'
    assert category_books.products == ['Harry Potter', 'Lord of the Rings', 'The Chronicles of Narnia']


def test_count_product(category_books):
    Category.category_count = 0
    Category.product_count = 0

    Category.category_count += 1
    Category.product_count += len(category_books.products)

    assert Category.product_count == 3
    assert Category.category_count == 1
