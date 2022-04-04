

# Prompt the user for the filename with item details
filename = input('Enter the filename: ')

def file_handler():

    '''
        Function opens a file specified by the user
        Processes the file and creates two lists
            One with text data: item_name and description
            The other with numeric data: quantity and price
    '''

    # Open the file specified for reading
    with open(filename, 'r') as file:

        # Read all the lines in the file
        data = file.readlines()

        # Initialize two empty lists
        item_desc = []  # Stores text data: name and description
        quant_price = [] # Stores numeric data: quantity and price

        # Loop through all the lines
        for line in data[1:]:

            item_name = line.split(',')[0] # Grab the item name
            description = line.split(',')[1] # Description
            quantity = line.split(',')[2] # Quantity
            price = line.split(',')[3]  # Price

            # Append text data to text list created earlier 
            item_desc.append((item_name, description))
            # Append numeric data to numeric list 
            quant_price.append((quantity, price))

    return (item_desc, quant_price) # Return the two lists


def output_files():

    '''
        Function takes the two lists returned by the file_handler function
        Creates two files
            One for the text data: Item_name and Description
            Second for the numeric data: Quantity and Price
    '''

    # Set the two lists created by the file_handler function
    item_desc, quant_price = file_handler()

    # Create the file to store text data
    with open('text_data.txt', 'a') as file:

        file.write('Item, Description\n') # File headers

        for item in item_desc:

            # Write the item name and description
            file.write(f'{item[0].strip()}, {item[1].strip()}\n')
    
    # Create the file to store numeric data
    with open('numeric_data.txt', 'a') as file:

            file.write('Quantity, Price\n') # File headers

            for qp in quant_price:

                # Write the quantity and price
                file.write(f'{qp[0].strip()}, {qp[1].strip()} \n')

    print('Output files created...')

if __name__ == '__main__':

    output_files()
    print('Thank you for running the program!')   





