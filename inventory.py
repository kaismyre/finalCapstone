from tabulate import tabulate
class Shoe:
    '''This is the base class for a shoes store 
        software to retrieve stock data
        '''
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    # method to return the cost of the shoe
    def get_cost(self):
        return self.cost
    # method to return the quantity of the shoe
    def get_quantity(self):
        return self.quantity
    # string representation method of the class using tabulate to display data
    def __str__(self):
        return tabulate([['Country:', self.country], ['Code:', self.code],
                         ['Product:', self.product], ['Cost:', self.cost], ['Quantity:', self.quantity]])

shoe_list = [] # empty list for later use
# Function to read that from a file and assign them to class attributes
def read_shoe_data():
    try: 
        with open("inventory.txt", "r") as file:
            next(file) # skip the first line
            for line in file:
                country, code, product, cost, quantity = line.strip().split(",")
                cost = float(cost)
                quantity = int(quantity)
                shoe_list.append(Shoe(country, code, product, cost, quantity))
    except FileNotFoundError:
        print('File does not exist!')    
# Function to add shoes to the store
def capture_shoe():
    country = input("Enter the country of origin: ")
    code = input("Enter the code of the shoe: ")
    product = input("Enter the name of the shoe: ")
    cost = float(input("Enter the cost of the shoe: "))
    quantity = int(input("Enter the quantity of the shoe: "))
    shoe_list.append(Shoe(country, code, product, cost, quantity))
# Function to view shoes from the store stock
def view_all():
    for shoe in shoe_list:
        print(shoe)
# Function to add stock to the store
def re_stock():
    # find the shoe with the lowest quantity
    lowest_quantity = float('inf')
    shoes = None
    for shoe in shoe_list:
        if shoe.quantity < lowest_quantity:
            lowest_quantity = shoe.quantity
            shoes = shoe

    # ask the user if they want to add more of this shoe
    add_more = input(f"Would you like to add more of the shoe '{shoes.product}'? (y/n) ")
    if add_more.lower() == "y":
        additional_quantity = int(input("Enter the additional quantity: "))
        shoes.quantity += additional_quantity
        # update the inventory file
        with open("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
# Function to look for shoe in the store
def search_shoe(code):
    for shoe in shoe_list:
        if shoe.code == code:
            return shoe
    return 'This does not exist!'
# Function to view total value per shoe
def value_per_item():
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"Value of {shoe.product} is {value} ")
# Function to view the shoe with the largest stock
def highest_qty():
    shoe_qty = [] 
    for shoe in shoe_list:
        shoe_qty.append(shoe.quantity)
    for shoe in shoe_list:
        if shoe.quantity == max(shoe_qty):
            print(f"{shoe.product} is ON FOR SALE!")
   
# Main Function to start the software 
def main():
    read_shoe_data()  # read the data from the inventory file and create shoe objects
    while True:   
        user_choice = input('Choice one of the options below:\n\
    c - Capture Shoes\n\
    v - View All\n\
    r - Restock\n\
    s - Search Shoe\n\
    t - Total Value Per Item\n\
    f - For Sale\n\
    q - Quit\n').lower()
        if user_choice == 'c':
            capture_shoe()
        elif user_choice == 'v':
            view_all()
        elif user_choice == 'r':
            re_stock()
        elif user_choice == 's':
            code = input('Enter the shoe code you want to search! ')
            shoe = search_shoe(code)
            try:
                print(shoe)
            except FileExistsError:
                print('Does not exist!')
        elif user_choice == 't':
            value_per_item()
        elif user_choice == 'f':
            highest_qty()
        elif user_choice == 'q':
            break
        else:
            print('Check your entry and try again!')
            continue

if __name__ == '__main__':
    main()