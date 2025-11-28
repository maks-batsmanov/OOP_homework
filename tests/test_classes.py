from src.classes import Category


def test_init_product(product_labubu):
    assert product_labubu.name == 'Labubu'
    assert product_labubu.description == 'toy'
    assert product_labubu.price == 100.00
    assert product_labubu.quantity == 10



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


def test_debug():
    import os
    print("Current dir:", os.getcwd())
    print("File dir:", os.path.dirname(__file__))

    # Запусти: pytest -s test_file.py