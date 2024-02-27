#Weight of package
#weight is in lbs
weight = 30

#Ground shipping

#this is the flat charge amount for ground shipping packages
#this is in dollars 
flat_charge_ground_shipping = 20
#Conditional for how much package will cost based on weight for ground shipping
if weight <= 2:
  print(flat_charge_ground_shipping + 1.50)
elif weight > 2 and weight <= 6:
  print(flat_charge_ground_shipping + 3.00)
elif weight > 6 and weight <= 10:
  print(flat_charge_ground_shipping + 4.00)
elif weight > 10:
  print(flat_charge_ground_shipping + 4.75)
