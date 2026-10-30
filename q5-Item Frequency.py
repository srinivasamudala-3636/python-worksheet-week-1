def count_items(items_list):
    result = {}

    for item in items_list:
        result[item] = result.get(item, 0) + 1

    return result

items = ['apple', 'banana', 'apple',
         'cherry', 'banana', 'apple']

print(count_items(items))