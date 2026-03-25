menu={
    "clothes":{"jeans":250,
               "t-shirt":200,
               "shirt":300,
               "pant":400,
               "hoodie":500,
               "sweatshirt":450
    },
    "makeup":{
        "fondation":3000,
        "primer":1500,
        "counciler":2500,
        "eyeliner":700,
        "kajal":500
    },
    "watches":{
        "sonata":4000,
        "tata":5000
    },
    "mobile":{
        "iphone":170000,
        "motorola":78000,
        "samsung":23000,
        "vivo":45000
    }
}

username=input("Enter your name: ")
cart=[]
while True:
    print("----------MENU----------")
    print("1.View page")
    print("2.Add to cart")
    print("3.Delete from cart")
    print("4.Generate bill")
    print("5.Exit")
    n=int(input("Enter your choice: "))
    match n:
        case 1:
            print("This is view page")
            print(menu)
            print(" ")
        case 2:
            n1=input("Enter category (cloths/watches/makeup/mobile): ")
            if n1 in menu:
                print("Product is available")
                for product,price in menu[n1].items():
                    print(product,":",price)
                p_name=input("Enter product name you want to add: ")
                
                if p_name in menu[n1]:
                    cart.append((n1,p_name))
                    print("Added succesfully!!")
                else:
                    print("Product not found in this category")
            else:
                print("Category not found")
        case 3:
            if not cart:
                print("Cart is empty.")
            else:
                print("Items in Cart:")
                for item in cart:
                    print(item[0], "->", item[1])

                category = input("Enter category of product to remove: ")
                product_name = input("Enter product name to remove: ")

            if (category, product_name) in cart:
                cart.remove((category, product_name))
                print("Item removed successfully!!")
            else:
                print("Item not found in cart.")
        case 4:
            if not cart:
                print("Cart is empty.Nothing to bill")
            else:
                print("------------EKART BILL------------")
                print("Username: ",username)
                print("Items purchased: ")
                
                total=0
                gst=18
                for n1,p_name in cart:
                    price=menu[n1][p_name]
                    gst_amount = (price * gst)/100
                    final_price = price + gst_amount
                    total += final_price
                    print(p_name,":",price)
                    print("GST is: ",gst_amount)
                print("Total Amount is: ",total)
                print("Thank you for shopping!!!")
        case 5:
            print("Thank you!!!") 
            break
        case _:
            print("Invalid input...try again") 
            break