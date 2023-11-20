list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
count_players = len(list_players)
count_players_in_group= int(count_players/2)
group_1 = list_players[0:count_players_in_group:1]
group_2 = list_players[count_players_in_group::1]
print(group_1)
print(group_2)
# TODO Разделите участников на две команды
