a=int(input("enter the no of fresh loaves purchased"))
b=int(input("enter the no of old loaves purchased"))
price=a*185
discount=price*0.6
tot_price=price+discount
print("the regular price : 185")
print(" amount of the fresh loaves",float(price))
print("amount of old loaves",float(discount))
print("total amount",float(tot_price))
