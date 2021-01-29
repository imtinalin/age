driving = input('Do you drive? (yes/no)')
if driving != 'yes' and driving != 'no':
	print('Please input "yes" or "no"')
	raise SystemExit

	
age = input('How old are you?')
age = int(age)
if driving == 'yes':
	if age >= 18:
		print('Pass')
	else:
		print('IMPOSSIBLE!!')
elif driving == "no":
	if age >= 18 :
		print('去考吧！')
	else:
		print('再等幾年吧！')