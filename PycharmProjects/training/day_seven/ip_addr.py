#Get the next ip address if the digit is less than 255 or else get 0 in the place and increment the prev index

#ip_addr = input("Enter the IP address :  : ")
ip_addr = '192.168.123.255'
print ("Ip address >>>", ip_addr)
ip_list = ip_addr.split('.')

print (ip_list)

#input : 192.168.255.255
#out : 192.169.0.0

'''
last_digit = ip_addr.split('.')[3]
if not last_digit == 255:
    next_digit = int(last_digit) + 1
    ip_list[3] = next_digit
print ("iplist>>>", (ip_list))

third_digit = ip_addr.split('.')[2]
if not third_digit == 255 and last_digit == 255:
    next_digit = int(third_digit) + 1
    ip_list[2] = next_digit
print ("iplist>>>", (ip_list))

last_digit = ip_addr.split('.')[3]
if not last_digit == 255:
    next_digit = int(last_digit) + 1
    ip_list[3] = next_digit
print ("iplist>>>", (ip_list))

'''
string = " "
for i in ip_list:
    string += str(i) + '.'

print ("Ip string >>>", string)