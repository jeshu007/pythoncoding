def shipping_charge(items):
    if items<=0:
        return 0
    elif items ==1:
        return 750.00
    else:
        return 750.00+200.00*(items-1)
items=int(input("enter the number of items:"))
charge=shipping_charge(items)
print("the shipping charge:$%.2f" %charge)
