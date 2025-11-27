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
    assert Category.count_of_products == 3
    assert Category.count_of_category == 1