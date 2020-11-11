# function finds lowest price
#input weight of package
#program finds price of ground shipping and drone shipping, compares those two and Premium shipping to find lowest price


premium = 125.00

def find_ground_price(weight):
  flat_rate = 20.00
  if weight <= 2:
      rate = 1.50
      return (weight * rate) + flat_rate
  elif (weight > 2) and (weight <= 6):
      rate = 3.00
      return (weight * rate) + flat_rate
  elif (weight > 6) and (weight <= 10):
      rate = 4.00
      return (weight * rate) + flat_rate
  elif (weight > 10):
      rate = 4.75
      return (weight * rate) + flat_rate

  
def find_drone_price(weight):
  if weight <= 2:
      rate = 4.50
      return weight * rate
  elif (weight > 2) and (weight <= 6):
    rate = 9.00
    return weight * rate
  elif (weight > 6) and (weight <= 10):
    rate = 12.00
    return weight * rate
  elif (weight > 10):
    rate = 14.25
    return weight * rate
  
def find_cheapest_price(weight):
  ground = find_ground_price(weight)
  drone = find_drone_price(weight)
  if ground < (drone and premium):
    return "Ground is cheapest, and costs " + str(ground) + " dollars."
  elif drone < (ground and premium):
    return "Drone is cheapest, and costs " + str(drone) + " dollars."
  elif premium < (ground and drone):
    return "Premium is cheapest and costs 125.00 dollars."

  
print(find_ground_price(8.4))

print(find_drone_price(1.5))

print(find_cheapest_price(4.8))

print(find_cheapest_price(41.5))
  
  
  