import json

##
# Author: BelligerentPotato
# Created: 9/26/2021
# Last Edit: 9/27/2021 12:19 PM EST
##

# research SQLite vs MySQL

barcodes = json.load(open('Barcode Database.json'))
choice = ""


def confirmation():
    a = input("\nAre you sure you want to continue? ")
    if a == "y":
        confirm = True
        return confirm
    elif a == "n":
        confirm = False
        return confirm
    else:
        print("You have made an invalid response, Please use \"y\" or \"n\" only.")


####################################################################################
#    This function is used to search for a barcode within the barcode database,    #
#     if not found allows user to to added the product if they choose to.          #
####################################################################################


def search_product():

    # find a way to only input whole numbers as a search result.

    search = input("Please enter product barcode numbers. ")
    if search in barcodes:
        print("Product Name: " + barcodes[search]["name"])
        print("Container Size: " + barcodes[search]["size"])
        print("\n#####################")
        print("# Nutritional Facts #")
        print("#####################")
        print("Servings per Container: " + barcodes[search]["nf_servings"])
        print("Serving Size: " + barcodes[search]["nf_serving_size"])
        print("Calories / serving: " + barcodes[search]["nf_calories"])
        print("Total Fat / serving: " + barcodes[search]["nf_total_fat"])
        print("Sodium / serving: " + barcodes[search]["nf_sodium"])
    else:
        confirm = input("This product barcode is not found in our database, Would you like to add it? ")
        if confirm.lower() == "y":
            add_product(search)
    return


####################################################################################
#    This function is used to add a product to the Barcode database                #
####################################################################################


def add_product(search):
    # Think of more descriptors of the product
    # Once a GUI is in place allow selection of Nutrition Fact through check boxes other then common default
    # Allow the option of available stores.
    # options like Calories, sodium, total fat,

    # Place holder for the new barcode nested dictionary data being added
    barcodes[search] = {}

    # collects input from the user for the products name and container size
    product_name = input("Please enter product name. (example: Brisk Iced Tea: Blackberry Smash) ")
    product_size = input("Please enter product size. (example: 1L or 1 Liter) ")

    # collects the Name & Size key values for the barcode being added
    barcodes[search]['name'] = product_name
    barcodes[search]['size'] = product_size

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    # Nutritional Facts portion of the function #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    # asks the user if they would like to input Nutritional facts of the product Allows them to skip this step
    nutrition_facts = input("would you like to add Nutrition Facts?(Y or N) ")
    if nutrition_facts == "y":
        product_nf_servings = input("Servings per container? ")
        print("\n Please input all of the following values by serving size, not container servings.")
        product_nf_serving_size = input("\nServing size? ")
        product_nf_calories = input("Calories? ")
        product_nf_total_fat = input("Total fat? ")
        product_nf_sodium = input("Sodium content? ")

        # Sets the values for Servings per container, Serving size, calories, total fat, sodium
        barcodes[search]['nf_servings'] = product_nf_servings
        barcodes[search]['nf_serving_size'] = product_nf_serving_size
        barcodes[search]['nf_calories'] = product_nf_calories
        barcodes[search]['nf_total_fat'] = product_nf_total_fat
        barcodes[search]['nf_sodium'] = product_nf_sodium

    # takes the new barcode &
    database = json.dumps(barcodes, indent=2)
    with open('Barcode Database.json', 'w') as barcode_database:
        barcode_database.write(database)
        barcode_database.close()

    print("\nProduct Name: " + product_name)
    print("Product Size: " + product_size)

    if nutrition_facts == "y":
        print("\n###################")
        print("# Nutrition Facts #")
        print("###################")
        print("Servings per Container: " + product_nf_servings)
        print("Serving Size: " + product_nf_serving_size)
        print("Calories: " + product_nf_calories)
        print("Total Fat: " + product_nf_total_fat)
        print("Sodium: " + product_nf_sodium)
    else:
        print("No Nutritional Facts given for this product.")
    return

####################################################################################
#        This function allows the user to add or edit product information          #
####################################################################################


def edit_product():

    product_barcode = input("Please enter the barcode of the product you would like to edit. ")
    if product_barcode in barcodes:
        print("What would you like to edit? make a selection below by entering the corresponding value.")
    else:
        print("This product does not seem to be in our database.")
    return



####################################################################################
# This function allows the user to delete a products information from the database #
####################################################################################


def del_product():
    selection = input("Please input the product barcode you would like to remove: ")
    print("Product Name: " + barcodes[selection]["name"])
    confirmation()

    if confirm is True:
        del barcodes[selection]
    else:
        print("Action canceled, Barcode was not removed.")

#####################################
#    Main code for the program.     #
#####################################


while choice != "exit":
    print("\n")
    print("Welcome to Kitchen pal, Thanks for using our program. What would you like to do? \n"
          "1. Search for a product. \n"
          "2. Add a product. \n"
          "3. Delete a product. \n"
          "4. Report a product \n")

    choice = input("Make your selection by typing the corresponding number: ")
    if choice == "1":
        search_product()
    elif choice == "2":
        add_product()
    elif choice == "3":
        del_product()
    elif choice == "4":
        print("currently being worked on!")
    else:
        print("Im sorry you have made a invalid choice please try again.")

print("\n\nend of program")
