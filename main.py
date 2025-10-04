#Linear search to find the max_number in a list of numbers

numbers = [3, 5, 2, 12, 8, 1]
max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number
print(max_number)

#Exercise: do a linear search on the same list, but we want to find the number 8

for number in numbers:
    if number == 8:
        print("We found the number 8 in your list.")
        break
