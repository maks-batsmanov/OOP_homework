from unittest.mock import patch

from src.data_reader import create_object_of_class


@patch("builtins.open")
def test_create_object_of_class(mock_open):

    test_json = """
    [
        {
            "name": "Электроника",
            "description": "Техника",
            "products": [
                {
                    "name": "Телевизор",
                    "description": "4K",
                    "price": 50000,
                    "quantity": 5
                }
            ]
        }
    ]
    """
    mock_open.return_value.__enter__.return_value.read.return_value = test_json
    products, categories = create_object_of_class("test.json")

    assert len(categories) == 1
    assert len(products) == 1
    assert categories[0].name == "Электроника"
    assert products[0].name == "Телевизор"
    assert products[0].price == 50000
