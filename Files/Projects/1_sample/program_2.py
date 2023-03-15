

with open('sample.txt', 'r') as file:

    data = file.readlines()

# print(data)

for line in data:
    text_data = line.split(',')[:2] # Grab item_name and description
    item_name, description = text_data
    print(item_name + ' - ' + description)
    with open('text_data', 'a') as file: # and store in one file
        file.write(f'{item_name}, {description}\n')
    num_data = line.split(',')[2:4] # Grab quantity and price
    print(num_data)
    quantity, price = num_data
    print(quantity + ' - ' + price)
    with open('num_data.txt', 'a') as file: # and store in one file
        file.write(f'{quantity.strip()}, {price.strip()}\n')








