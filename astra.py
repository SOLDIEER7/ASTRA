import socket
import pyfiglet


# = = = = = = = = = = = = 

Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
B = '\033[2;36m'
Y = '\033[1;34m' 

# = = = = = = = = = = = =

sol = pyfiglet.figlet_format('ASTRA')
print (Y+sol)
print('# port check tool ')
print(Y+'''
                                                  INSTA:@__so1dier
''')
print((((((((((((Y+'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ '))))))))))))
print()
target = str ( input (( B+'[+]' ) + (((( F+ ' Enter your ip : ' ))))))
print((((((((((((Y+'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ '))))))))))))
print()
port = int ( input (( B+'[+]' ) + (((( F+ ' Enter port to scan : ' ))))))
print((((((((((((Y+'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ '))))))))))))
print()
s = socket.socket ( socket.AF_INET ,socket .SOCK_STREAM)

r = s.connect_ex ((target,port))

if r == 0 :
	service = socket.getservbyport(p)
	print(F+"[+]_ _ [ * {} * is open _ _>> {} ] ".format(p_service))
else:
		print(Z+'[+] port is clos !!! . ')
		print((((((((((((Y+'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ '))))))))))))
		print ()
f = input (Z+'[+] Enter to exit :')
s.close()