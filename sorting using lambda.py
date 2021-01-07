items = [('product1', 30), ('product2', 20), ('product3', 79)]
items.sort(key=lambda item: item[1], reverse=True)
print(items[0])
