largest = None
smallest = None

while True:
    number_input = input('Enter a Number: ')
    if number_input == 'done':
        break
    try:
        number_input_casted = int(number_input)

        if largest is None:
            largest = number_input_casted
        elif number_input_casted > largest:
            largest = number_input_casted

        if smallest is None:
            smallest = number_input_casted
        elif number_input_casted < smallest:
            smallest = number_input_casted

    except ValueError:
        print('Invalid input')
        continue

print("Maximum is", largest)
print("Minimum is", smallest)
