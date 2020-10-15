cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Мед', 'quantity': 2, 'measure': 'ст.л'},
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }

shop_list = {}

def get_ingredients(dish, person_count):
  d = {}
  for i in cook_book[dish]:
    key = i.pop('ingredient_name')
    i['quantity'] *= person_count
    d.update({key:i})
  return d

def get_shop_list_by_dishes(dishes, person_count):
  att = 'quantity'
  for dish in dishes:
    res = get_ingredients(dish, person_count)
    for key in res:
      test = shop_list.get(key)
      if test == None:
        shop_list.update({key:res[key]})
      else:
        shop_list[key][att] += res[key][att]

def check_user(dishes, person_count):
  user = dishes
  for dish in user:
    print(dish)
    if cook_book.get(dish) == None:
      print(f'{dish} does not exist, so was deleted')
      dishes.pop(dishes.index(dish))

dishes = input().split('/')
person_count = int(input())

check_user(dishes, person_count)
get_shop_list_by_dishes(dishes, person_count)
print(shop_list)
