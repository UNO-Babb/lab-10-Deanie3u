#MapPlot.py
#Name:
#Date:
#Assignment:

import hospitals
hospitals = hospitals.get_hospitals()

num_items = len(hospitals)

ratings = []
procedures =[]

for spot in range(num_items):
    rating = hospitals[spot]["Rating"]["Overall"]
    total_procedure = hospitals[spot]["Procedure"]["Pneumonia"]["Cost"]
    print(rating, total_procedure)
    if rating <3:
        procedures.append(total_procedure)
        ratings.append(rating)

import matplotlib.pyplot as plt
plt.plot(ratings, procedures, 'ro')
plt.plot('Total Procedures')
plt.ylabel('Rating')
plt.savefig("output")