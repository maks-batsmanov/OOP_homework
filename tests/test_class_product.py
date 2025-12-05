from unittest.mock import patch

from src.class_product import Product


def test_init_product(product_labubu):
    assert product_labubu.name == 'Labubu'
    assert product_labubu.description == 'toy'
    assert product_labubu.price == 100.00
    assert product_labubu.quantity == 10


def test_new_product(product_labubu_dict, list_for_comparison):
    result = Product.new_product(product_labubu_dict, list_for_comparison)
    assert result.name == 'Labubu'
    assert result.description == 'toy'
    assert result.price == 100
    assert result.quantity == 14


def test_price(init_product):
    result = init_product.price
    assert result == 50.00


def test_price_setter(init_product):
    init_product.price = 60.00
    assert init_product.price == 60.00


def test_price_setter_negative_price(capsys, init_product):
    init_product.price = -120.00
    result = init_product.price
    captured = capsys.readouterr()
    assert 'Цена не должна быть нулевая или отрицательная' in captured.out
    assert result == 50.00


@patch('builtins.input', side_effect=['y', 'n'])
def test_price_setter_low_price(mock_input, init_product):
    init_product.price = 30.00
    assert init_product.price == 30.00
    init_product.price = 20.00
    assert init_product.price == 30.00


def test_product_str(product_labubu):
    obj_str = str(product_labubu)
    assert obj_str == 'Labubu, 100.0 руб. Остаток: 10 шт.'


def test_product_add(product_labubu, init_product):
    result = product_labubu + init_product
    assert result == 1300


def