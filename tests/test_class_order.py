from src.class_order import Order


def test_order(product_labubu):
    result = Order(product_labubu, 10)
    assert str(result) == 'Labubu, количество проданных продуктов: 10, итоговая цена: 1000.0 руб.'
    assert result.total_cost == 1000.0
    assert result.total_quantity == 10