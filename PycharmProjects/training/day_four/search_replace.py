import re
p =re.compile('(blue|white|red)')
sub1 = p.sub('colour', 'blue socks and red shoes')
print ("Sub 1>>>>>", sub1)

#Replaces the num of times as specified in the count
sub2 = p.sub('colour', 'blue socks and red shoes', count = 1)
print("Sub 2>>>>>", sub2)

