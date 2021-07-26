#  Example 1
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

#  Example 2
print('-----------------------------')
friends = ['Joseph', 'Ali', 'Mehdi', 'Kumar', 'Ahti']
for friend in friends:
    print('Happy birthday ! ', friend)

print('Done !')

#  Example 3 - Finding largest number
print('-----------------------------')
largest_so_far = -1
print('Before', largest_so_far)  # Before -1

for num in [9, 47, 58, 125, 6964, 8456, 14, 123457, 56, 7777777, 8479, 965417, 9451, 874, 8954, 12, 1789]:
    if num > largest_so_far:
        largest_so_far = num
    print(largest_so_far, num)

print('After, ', largest_so_far)  # After,  7777777

#  Example 4 - Counting in Loop
print('-----------------------------')
counter = 0
print('Before', counter)  # Before 0
for thing in [9, 47, 58, 125, 6964, 8456, 14, 123457]:
    counter = counter + 1
    print(counter, thing)

print('After, ', counter)  # After, 8

#  Example 5 - Total
print('-----------------------------')

total = 0
print('Before', total)  # Before 0
for thing in [9, 47, 58, 125, 6964, 8456, 14, 123457]:
    total = total + thing
    print(counter, thing)

print('After, ', total)  # After, 139130

#  Example 6 - Average
print('-----------------------------')
count = 0
total = 0
print('Before', count, total)  # Before 0
for thing in [9, 47, 58, 125, 6964, 8456, 14, 123457]:
    count = count + 1
    total = total + thing

print('Avg, ', total / count)  # Avg, 17391.25
