total = 0
avg = 0
count = 0
choice = ''

while True:
    choice = input('Enter a Number: ')
    if choice == 'done':
        break
    try:
        casted_choice = int(choice)
        count = count + 1
        total = total + casted_choice
        avg = total / count
    except ValueError:
        print('Only Numbers are allowed')
        continue

print('Total = ', total, 'count = ', count, 'Average =  ', avg)
