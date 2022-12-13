from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input('\nFirst name: ')
    if first == 'q':
        break
    last = input('\nLast name: ')
    if last == 'q':
        break

    formattted_name = get_formatted_name(first, last)
    print(f'\tFormatted name: {formattted_name}.')