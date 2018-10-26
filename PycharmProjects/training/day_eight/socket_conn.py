import socket

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("datafiasco.blogspot.com", 80)) #connect 80: for all websites
#s.connect(("datafiasco.blogspot.com", 443)) #connect 443 : https:  secured port
s.send(b"GET /index.html HTTP/1.0\n\n")#send request
data = s.recv(10000)#get response#10000 is no of bytes
print(data)
s.close()

#b'HTTP/1.0 200 OK\r\nDate: Fri, 26 Oct 2018 05:24:41 GMT\r\nExpires: -1\r\nCache-Control: private, max-age=0\r\nContent-Type: text/html; charset=ISO-8859-1\r\nP3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."\r\nServer: gws\r\nX-XSS-Protection: 1; mode=block\r\nX-Frame-Options: SAMEORIGIN\r\nSet-Cookie: 1P_JAR=2018-10-26-05; expires=Sun, 25-Nov-2018 05:24:41 GMT; path=/; domain=.google.com\r\nSet-Cookie: NID=144=gU2t5vav5n26Ur1pEnsFzBe1hjxx7L2Vf5avR8-njl3_NQrXxM82WLtxk7hq5fmlD6mx32OE-Ua_6ZK6-BdLhmFKtaB3EvJDK5N9uobC3QxTp0bjtbZUem6E-wnVAI8VYjaLhrWGVFnU5-grzK3W7rrWxrR0o_CsocjW1vz4zQ8; expires=Sat, 27-Apr-2019 05:24:41 GMT; path=/; domain=.google.com; HttpOnly\r\nAccept-Ranges: none\r\nVary: Accept-Encoding\r\n\r\n<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en-IN"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="rjdN3QxKuXEA+OwKh2ojiw==">(function(){window.google={kEI:\'GaXSW-elCoqgvQSI1Ij4Cg\',kEXPI:\'0,1352961,786,57,51,1907,582,434,281,265,860,698,527,731,142,292,184,155,418,257,48,302,554,302,327,39,2337128,201,32,329294,1294,12383,4855,32691,15248,867,6692,5471,5281,1100,3335,2,2,4609,2192,363,1218,4416,3191,224,2212,266,1028,4079,575,835,284,2,205,373,728,612,1819,5'
#b'' #normally https: accepts encoded data...so returns empty set


#if you use dgram/80, connection refused since http accepts only TCP services
