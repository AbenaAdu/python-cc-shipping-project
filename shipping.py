#Weight of package
#weight is in lbs
weight = 1

#Ground shipping

#this is the flat charge amount for ground shipping packages
#this is in dollars 
flat_charge_ground_shipping = 20
greeting_for_ground_shipping_cost = "Amount Due for Ground Shipping: "
#Conditional for how much package will cost based on weight for ground shipping
if weight > 0 and weight <= 2:
  print(greeting_for_ground_shipping_cost)
  print(flat_charge_ground_shipping + (weight * 1.50))
elif weight > 2 and weight <= 6:
  print(greeting_for_ground_shipping_cost)
  print(flat_charge_ground_shipping + (weight * 3.00))
elif weight > 6 and weight <= 10:
  print(greeting_for_ground_shipping_cost)
  print(flat_charge_ground_shipping + (weight * 4.00))
elif weight > 10:
  print(greeting_for_ground_shipping_cost)
  print(flat_charge_ground_shipping + (weight * 4.75))
else:
  print("ERROR")

#Ground Shipping Premium
#flat charge for ground shipping premium
flat_charge_ground_shipping_premium = 125
print("Amount Due for Ground Shipping Premium: ")
print(flat_charge_ground_shipping_premium)