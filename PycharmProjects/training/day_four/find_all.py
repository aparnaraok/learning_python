import re
p = re.compile('\d+')
lis = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
print (lis)