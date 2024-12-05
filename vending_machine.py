print("Welcome to Shakti’s vending machine\n")

print("Product Price Code")

print("KitKat       $2   1001")

print("Coke         $4   1002")
    
print("Dairy Milk   $1   1003")

print("Lays         $3   1004")

#homework - add two more products of your choice

#List of all variables

kitkat_Price = 2
coke_Price = 4
dairyMilk_Price = 2
lays_Price = 3

kitkat_Code = "1001"
coke_Code = "1002"
dairyMilk_Code = "1003"
lays_Code = "1004"

print ("Type a code to continue:")

customer_Code = input()

#checking what the customer wants - KitKat
if customer_Code==kitkat_Code:
#START OF KITKAT CODE

  
  print("You have selected KitKat! Please pay $",kitkat_Price)

#checking for payment from customer
  customer_Payment = float(input())

#if customer payment is equal to kitkat price
  if customer_Payment == kitkat_Price:
    print("Paid! Kitkat is dispensing...")
      
#if customer payment is less than the kitkat price:
  elif customer_Payment<kitkat_Price:
    required_Money = kitkat_Price - customer_Payment
    print("Sorry, you did not pay enough! Please insert another $",required_Money ," to get your KitKat!")
      
#if customer payment is more than the kitkat price:
  elif customer_Payment>kitkat_Price:
    change_ammount = customer_Payment - kitkat_Price
    print("Paid! KitKat and your change:",change_ammount ," are despensing")
      



#END OF KITKAT CODE
    


#checking what the customer wants - Coke
elif customer_Code==coke_Code:
#START OF COKE CODE


  print("You have selected Coke! Please pay $",coke_Price)

#checking for payment from customer
  customer_Payment = float(input())

#if customer payment is equal to coke price:
  if customer_Payment == coke_Price:
    print("Paid! Coke is dispensing...")
       
#if customer payment is less than the coke price:
  elif customer_Payment<coke_Price:
    required_Money = coke_Price - customer_Payment
    print("Sorry, you did not pay enough! Please insert another $",required_Money ," to get your Coke!")

#if customer payment is more than the coke price:
  elif customer_Payment>coke_Price:
    change_ammount = customer_Payment - coke_Price
    print("Paid! Coke and your change:",change_ammount ," are despensing")
       



#END OF COKE CODE
    

#checking what the customer wants - Dairy Milk
elif customer_Code==dairyMilk_Code:
#START OF DAIRY MILK CODE


  print("You have selected Dairy Milk! Please pay $",dairyMilk_Price)

#checking for payment from customer
  customer_Payment = float(input())
  
#if customer payment is equal to dairy milk price:
  if customer_Payment == dairyMilk_Price:
    print("Paid! Dairy Milk is dispensing...")

#if customer payment is less than the dairy milk price:
  elif customer_Payment<dairyMilk_Price:
    required_Money = dairyMilk_Price - customer_Payment
    print("Sorry, you did not pay enough! Please insert another $",required_Money ," to get your Dairy Milk!")
         

#if customer payment is more than the dairy milk price:
  elif customer_Payment>dairyMilk_Price:
    change_ammount = customer_Payment - dairyMilk_Price
    print("Paid! Dairy Milk and your change:",change_ammount ," are despensing")



#END OF DAIRY MILK CODE

#checking what the customer wants - Lays
elif customer_Code==lays_Code:
#START OF LAYS CODE


  print("You have selected Lays! Please pay $",lays_Price)
#checking for payment from customer
  customer_Payment = float(input())

#if customer payment is equal to lays price:
  if customer_Payment == lays_Price:
    print("Paid! Lays is dispensing...")

#if customer payment is less than the lays price:
  elif customer_Payment<lays_Price:
    required_Money = lays_Price - customer_Payment
    print("Sorry, you did not pay enough! Please insert another $",required_Money ," to get your Lays!")

#if customer payment is more than the lays price:
  elif customer_Payment>lays_Price:
    change_ammount = customer_Payment - lays_Price
    print("Paid! Lays and your change:",change_ammount ," are despensing")


#END OF LAYS CODE

else:
  print("Invalid Code. Please try again")







#code ends here
