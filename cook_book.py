def format_ingredient(s):
  return dict(zip(['ingredient_name', 'quantity', 'measure'], s.replace('\n','').split(' | ')))

def format_dish(dish,ingredients):
  d = {dish:[]}
  for i in ingredients:
    d[dish].append(format_ingredient(i))
  return d

cook_book = {}
with open('files/recipes.txt', encoding="utf-8") as f:
  data = f.readlines()

i = 0
while i < len(data):
  dish = data[i].replace('\n','')
  length = int(data[i+1])
  ingredients = data[(i+2):(i+2+length)]
  cook_book.update(format_dish(dish,ingredients))
  i += length + 3

print(cook_book)
