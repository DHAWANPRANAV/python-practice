#5. Ask the user to enter product name, quantity, and price per unit. Calculate and print the 
#total bill amount using proper type conversion.

Product_name = input( "Enter Product Name - ")
Quantity = int(input ( "Enter number of products needed : "))
ppr = float(input( "Enter Price of THe product : "))

Bill_amount = float((Quantity * ppr ))

print ("Product name :" ,Product_name)
print ( "products needed :", Quantity)
print ( "price of the product is :" , ppr) 



print ( "YOur total bill is " , Bill_amount ,"$")

