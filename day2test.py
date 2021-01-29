password = 'a123456'
time = 3

while True:
	enter = input('please input your password:')
	
	if enter == password :
		print('Logon OK!')
		break	

	time = time -1
	if time == 0 :
		print('Sorry!')
		break
	print('Error!',time,' more times')

	