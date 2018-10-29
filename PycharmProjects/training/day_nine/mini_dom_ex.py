from xml.dom import minidom

doc = minidom.parse("sample.xml")
name = doc.getElementsByTagName("name")[0]
print (name.firstChild.data)

foods = doc.getElementsByTagName("food")
for food in foods:
    fid = food.getAttribute("id")
    des = food.getElementsByTagName("description")[0]
    price = food.getElementsByTagName("price")[0]
    calorie = food.getElementsByTagName("calories")[0]
    print ("id:%s, des:%s, price:%s, calorie:%s" %(fid, des.firstChild.data, price.firstChild.data, calorie.firstChild.data))


# Belgian Waffles
# id:1, des:
#    Two of our famous Belgian Waffles with plenty of real maple syrup
#    , price:$5.95, calorie:650
# id:2, des:
#     Light Belgian waffles covered with strawberries and whipped cream
#     , price:$7.95, calorie:900
# id:3, des:
#     Belgian waffles covered with assorted fresh berries and whipped cream
#     , price:$8.95, calorie:900
# id:4, des:
#     Thick slices made from our homemade sourdough bread
#     , price:$4.50, calorie:600
# id:5, des:
#     Two eggs, bacon or sausage, toast, and our ever-popular hash browns
#     , price:$6.95, calorie:950