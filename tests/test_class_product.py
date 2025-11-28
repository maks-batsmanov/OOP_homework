
def test_init_product(product_labubu):
    assert product_labubu.name == 'Labubu'
    assert product_labubu.description == 'toy'
    assert product_labubu.price == 100.00
    assert product_labubu.quantity == 10
