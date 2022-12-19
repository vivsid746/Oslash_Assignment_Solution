from sys import argv

# Name = "Vivek Singhal"
# Email = "viveksinghal.coder@gmail.com"
# GitHub = "vivsid746"

def main():
    # Check 'sample_input/input.txt' file is provided in command or not 
    if len(argv) != 2:
        raise Exception("Error: File path not entered")
    
    # Open the file in read
    file_path = argv[1]
    file = open(file_path, 'r')
    lines = file.readlines()

    # define pre-requisite for products
    items = {"tshirt": 1000, "jacket": 2000, "cap": 500, "notebook": 200, "pens": 300, "markers": 500}
    clothing = ["tshirt", "jacket", "cap"]
    stationery = ["notebook", "pens", "markers"]
    discount = {"tshirt": 0.1, "jacket": 0.05, "cap": 0.2, "notebook": 0.2, "pens": 0.1, "markers": 0.05}

    output = 0
    l = {}
    
    for line in lines:
        arg = line.strip().split(" ")  

        # If command is given as 'ADD_ITEM' 
        if arg[0] == "ADD_ITEM":

            # For each clothing item, the maximum quantity that can be purchased is 2.
            if arg[1].lower() in clothing:
                if int(arg[2]) > 2:
                    print("ERROR_QUANTITY_EXCEEDED")
                else:
                    output = output + items[arg[1].lower()] * int(arg[2])
                    l[arg[1]] = int(arg[2])
                    print("ITEM_ADDED")

            # For each stationery item, the maximum quantity that can be purchased is 3.
            elif arg[1].lower() in stationery:
                if int(arg[2]) > 3:
                    print("ERROR_QUANTITY_EXCEEDED")
                else:
                    output = output + items[arg[1].lower()] * int(arg[2])
                    l[arg[1]] = int(arg[2])
                    print("ITEM_ADDED")
        
        # If command is given as 'PRINT_BILL'
        if arg[0] == "PRINT_BILL":
            result = output
            discountPrice = 0

            # Discounts can be applied only if the total purchase amount is 1000 rupees or more.
            if output >= 1000:
                for i in l.items():
                    discountPrice = discountPrice + items[i[0].lower()] * i[1] * discount[i[0].lower()]
            amount = result - discountPrice
            
            # An additional discount of 5% can be applied if the total amount to pay is 3000 rupees or more.
            if amount >= 3000:
                discountPrice = discountPrice + (amount / 20)
                amount = amount - (amount / 20)

            print("TOTAL_DISCOUNT {:.2f}".format(discountPrice))
            # There is a 10% sales tax on total bill.
            print("TOTAL_AMOUNT_TO_PAY {:.2f}".format((amount) + ((amount) / 10))) 


if __name__ == "__main__":
    main()