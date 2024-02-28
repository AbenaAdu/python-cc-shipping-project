#Weight of package
#weight is in lbs
weight = 50

#Error message for if user enters weight below zero
error_message = "ERROR: Invalid weight"

#Ground shipping

#this is the flat charge amount for ground shipping packages
#in dollars 
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
  print(error_message)

#Ground Shipping Premium
#flat charge for ground shipping premium
#in dollars
flat_charge_ground_shipping_premium = 125
greeting_for_ground_premium_shipping_cost = "Amount Due for Ground Shipping Premium: "
if weight > 0:
  print(greeting_for_ground_premium_shipping_cost)
  print(flat_charge_ground_shipping_premium)
else:
  print(error_message)


#Drone Shipping
greeting_for_drone_shipping_cost = "Amount Due for Drone Shipping: "
#Conditional for how much package will cost based on weight for drone shipping
if weight > 0 and weight <= 2:
  print(greeting_for_drone_shipping_cost)
  print(weight * 4.50)
elif weight > 2 and weight <= 6:
  print(greeting_for_drone_shipping_cost)
  print(weight * 9.00)
elif weight > 6 and weight <= 10:
  print(greeting_for_drone_shipping_cost)
  print(weight * 12)
elif weight > 10:
  print(greeting_for_drone_shipping_cost)
  print(weight * 14.25)
else:
  print(error_message)
