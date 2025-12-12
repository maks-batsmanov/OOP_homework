def test_mixinlog(capsys, product_labubu):
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Labubu, toy, 100.0, 10)"
