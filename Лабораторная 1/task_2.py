# TODO Найдите количество книг, которое можно разместить на дискете
symbol = 4;
str = 25;
page = 50;
count_page = 100;
memory = 1.44*1024*1024;
count_book = memory/(symbol*str*page*count_page)
print("Количество книг, помещающихся на дискету:", round(count_book))
