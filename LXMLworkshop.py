# Create a python program that reads the food.xml file then using XPath it prints the following information,
# (please use separate XPath queries for each):

from lxml import etree

tree = etree.parse('food.xml')
root = tree.getroot()

# The price of all foods (as a list)
prices = tree.xpath('//price/text()')
for p in prices:
    print(p)

# The sum of all the calories
calories = tree.xpath('//food/calories/text()')
cal_sum = 0
for i in calories:
    cal_sum += int(i)
print(cal_sum)

# The description of the food with the id: 3
by_id = tree.xpath('//*[@id = "3"]')[0]
print(by_id.find('description').text.strip())

# The price of "French Toast"
french_toast = tree.xpath('//food[name = "French Toast"]/price/text()')
print(*french_toast)

# The concatenated descriptions of all the "savoury" foods
savoury = root.xpath('//*[@type = "savoury"]/description')
concat = ''
for i in savoury:
    concat = f'{concat}-{i.text.strip()}'
print(concat)

# The count of ingredients of the food with id: 2
ing_count = tree.xpath('//food[@id = "2"]')[0]
print(len(ing_count.xpath('ingredients/ingredient')))

# The second ingredient of "Homestyle Breakfast"
sec_ing = tree.xpath('//food[name = "Homestyle Breakfast"]')[0]
sec_ing_list = sec_ing.xpath('ingredients/ingredient/type/text()')
print(sec_ing_list[1])

# The count of foods that has "milk" in the ingredients
milk = tree.xpath('//food/ingredients/ingredient[type="milk"]')
print(len(milk))

# The count of ingredients of all "sweet" foods
sweets = tree.xpath('//food[@type="sweet"]/ingredients/ingredient')
print(len(sweets))