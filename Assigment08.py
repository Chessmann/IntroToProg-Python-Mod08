# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Chris Messmann,12.6.20,Modified code to update class: Product(object), FileProcessor
# Chris Messmann,12.7.20,Modified code to update class: lstProcessor, IO
# Chris Messmann,12.8.20,Modified code to update Main Body of Script

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
strChoice = ""
strItem = ""
strPrice = ""
strStatus = ""

class Product(object):
    """Stores data about a product:

    properties:
        product_name: (string) with the products's name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Chris Messmann,12.6.20,Modified code to complete class
    """

    # -- Constructor --
    def __init__(self, product_name, product_price):

        # -- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price

    # -- Properties --
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self,value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Product names cannot be numbers")

    @property
    def product_price(self):
        return str(self.__product_price).title()

    @product_price.setter
    def product_price(self, value):
        if str(value).isalpha() == False:
            self.__product_price = value
        else:
            raise Exception("Prices cannot be text")
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Chris Messmann,12.6.20,Added methods to read and write data to a file
    """


    # Code to save data to a file
    @staticmethod
    def save_data_to_file(file_name, lstOfProducts):
        file = open(file_name, "w")
        for line in lstOfProducts:
            file.write(line.product_name + "," + str(line.product_price) + "\n")
        file.close()
        print("Your data has been saved to the file 'products.txt'")
        return 'Success'

    # Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name, lstOfProducts):
        lstOfProducts.clear
        file = open(file_name, 'r')
        for line in file:
            product, price = line.split(",")
            lstOfProducts.append(Product(product.strip(),float(price.strip())))
        file.close()
        return lstOfProducts, 'Success'

# Processing  ------------------------------------------------------------- #
class lstProcessor:

    @staticmethod
    def add_data_to_list(product, price, lstOfProducts):
        lstOfProducts.append(Product(product.strip(), price.strip()))
        return 'Success'

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # Add docstring
    '''Presents user a menu and receives users menus choice.  Will also
     display current data is that menu option is selected.
     properties

     changeLog
        Chris Messmann, 12.7.20, updated IO to complete Assignment08'''

# Add code to show menu to user
    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Display Current List 
        2) Add a new Item, Price
        3) Save Data to File  
        4) Exit Program      
        ''')
        print()  # Add an extra line for looks

        # Add code to get user's choice
    @staticmethod
    def input_menu_choice():       #Need a try-except block here!!!!
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

        # Add code to show the current data from the file to user
    @staticmethod
    def print_current_Items_in_list(lstOfProducts):
        """ Shows the current Items in the list of rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Items are: *******")
        for row in lstOfProducts:
            print(row.product_name + " (" + str(row.product_price) + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

        # Add code to get product data from user
    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_item_and_price():
        print("Enter a new Item and Price")
        product = input("Product: ").lower()
        price = input("Price: ").lower()
        return product, price
# Presentation (Input/Output)  -------------------------------------------- #
# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)

while (True):
    # Show user a menu of options
    IO.print_menu_Tasks()  # Shows menu
    # Get user's menu option choice
    strChoice = IO.input_menu_choice()  # Get menu option

    # Show user current data in the list of product objects
    if strChoice.strip() == '1':
        IO.print_current_Items_in_list(lstOfProductObjects)
        IO.input_press_to_continue()
        continue  # to show the menu

    # Let user add data to the list of product objects
    elif strChoice.strip() == '2':
        strItem, strPrice = IO.input_new_item_and_price()
        strStatus = lstProcessor.add_data_to_list(strItem, strPrice, lstOfProductObjects)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    # let user save current data to file and exit program
    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            IO.input_press_to_continue(strStatus)
            break  # and Exit

    elif strChoice == '4':  # Exit Program
        print("Goodbye!")
        input("Enter to Exit", )
        break  # and Exit


