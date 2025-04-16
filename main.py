#MapPlot.py
#Name:
#Date:
#Assignment:

import coffee
coffee = coffee.get_coffee()

num_items = item(coffee)

for spot in range(num_items):
    total_score = coffee[spot]["Data"]["Score"]["Total"]

    print(total_score)