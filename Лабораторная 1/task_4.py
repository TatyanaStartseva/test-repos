from typing import Dict

users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
Di = {'Общее количество': len(users), 'Уникальные посещения': 0}
unique_users = set(users)
Di['Уникальные посещения'] = len(unique_users)
print(Di)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
