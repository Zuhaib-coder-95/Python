costprice=float(input("Enter the cost price:"))
sellingprice=float(input("Enter the selling price:"))

if sellingprice>costprice:
    print("It is a profit")
    profit=sellingprice-costprice
    print("The profit amount is:", profit)

if costprice>sellingprice:
    print("It is a loss")
    loss=costprice-sellingprice
    print("The loss amount is:", loss)