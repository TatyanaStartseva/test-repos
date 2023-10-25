# TODO Напишите функцию для поиска индекса товара

def index_item_(list_items, product):
    y=0
    for i in list_items:
        if i == product:
            return y
        else:
            y += 1
    return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = index_item_(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
