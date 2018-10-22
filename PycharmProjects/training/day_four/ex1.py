
import re
pat1 = re.compile('[bwhjggjihk]?x')#CHECKS FOR X REPITITION AS ZERO OR ONE TIME AND PRINTS MATCHED
#X IS OPTIONAL ...IT CHECKS WHETHER ANY CHAR IN THE GIVEN STRING IS PRESENT IN THE [] GIVEN ANAD MATCHES IF PRESENT
if pat1.search('bwhjggjihk'):
    print ("Char a  matched")
else:
    print ("Char a not matched")


###a should be either 0 / 1 time occurring between b and b
pat2 = re.compile('ba?b')
lis1 = ['baa', 'bab', 'bb', 'baaba']
for ele in lis1:
    if pat2.search(ele):
        print ("Matched :  : ", ele)
    else:
        print ("Not matched : : ", ele)
print (" ")
###a should be either 0 / 1 time occurring between b and b
pat2 = re.compile('[ghijab]?abc')
lis1 = ['baaxabc', 'baxgbc', 'bbabc', 'baaba']
for ele in lis1:
    if pat2.search(ele):
        print ("Matched :  : ", ele)
    else:
        print ("Not matched : : ", ele)
