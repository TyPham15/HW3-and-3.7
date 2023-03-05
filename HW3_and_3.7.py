#HW 3 and HW 3.7 on the same github link


#HW 3.7 on line: 54


#HW 3
def Project_1():
	speed = float(input('How fast is the vehicle in mph? '))
	time = int(input('How many hours does the vehicle travel? '))
	n = 0

	for n in range(time):
		n += 1
		distance = speed * n
		print(f'At hour {n} the distance is {distance} mph.')

	return str


def Project_2():
	years = int(input('Enter the amount of years: '))
	months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	n = 0
	total = 0

	for year_loop in range(years):
		for month_loop in (months):
			n += 1
			rain_month = float(input(f'How much rain was in {month_loop}: '))
			total += rain_month
	average = total / n
	print(f'Calculated number of months: {n}')
	print(f'The total rainfall for {years} years was {total}.')
	print(f'The average rainfall for {n} months was {average} rainfall per month.')
	
	return str


def Project_3():
	n = 0
	total = 0

	while n >= 0:
		n = float(input('Enter any number: '))
		if n >= 0:
			total += n

	print(f'The total of all the positive numbers you have entered is {total}.')

	return str


#HW 3.7
def Project_1_lists():
	test_scores = []
	again = 'y'
	while again == 'y':
		value = float(input('Enter a test score: '))
		test_scores.append(value)

		print('Do you want to add another score?')
		again = input('y = yes, anything else = no: ')
		print()

	f = open("output.txt", "w")
	f.writelines(str(test_scores))
	f.close()
	
	return test_scores


def Project_2_lists():
	number_list = []
	total = 0.0

	for numbers in range(20):
		num = float(input('Enter any number you want: '))
		number_list.append(num)
		total += num

	average = total / 20

	print(f'The lowest number in the list is {min(number_list)}.')
	print(f'The highest number in the list is {max(number_list)}.')
	print(f'The total of the numbers you entered is {total}.')
	print(f'The average of the numbers you entered is {average}.')

	return str
