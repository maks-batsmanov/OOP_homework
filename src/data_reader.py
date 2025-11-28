import json
import os

from src.classes import Category, Product


def create_object_of_class(file_name):
    """Функция принимает имя json-файла из папки data
     и возвращает объект класса"""

    current_dir = os.path.dirname(__file__)
    project_root = os.path.dirname(current_dir)
    file_path = os.path.join(project_root, 'data', file_name)

    with open(file_path, 'r', encoding='utf-8') as file:
        content = json.load(file)

    list_of_products = []
    for category_ in content:
        for dict_ in category_['products']:
            new_obj = Product(dict_['name'], dict_['description'], dict_['price'], dict_['quantity'])
            list_of_products.append(new_obj)

    list_of_categories = []
    for category_ in content:
        new_obj = Category(category_['name'], category_['description'], category_['products'])
        list_of_categories.append(new_obj)

    return list_of_products, list_of_categories
