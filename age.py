driving = input('請問你有沒有開過車:')
if driving !='yes' and  driving !='nope':
	print('只能輸入yes/nope')
	raise SystemExit

age = input('請問你的年齡是:')
age = int(age)
if driving == 'yes':
	if age >= 18:
		print ('ok')
	else:
		print ('ohoh, its illegal')
elif driving == 'nope':
	if age >=18:
		print('Go getting license ,right now!')
	else:
		print('Fine, you will get it soon')




