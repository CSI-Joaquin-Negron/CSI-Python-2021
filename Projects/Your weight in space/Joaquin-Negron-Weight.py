planet = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
gms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

print('Calculate your weight in different planets')

myWeight = int(input('What is your weight(pounds)'))
myPlanet = input(f'Select a planet fron the list: {planet}')

def calculateWeight(planet, mass):
    print(f"\nEarth mass in pounds is: {mass}")

    w_kg = mass / 2.2046
    print(f"Mass in Kg: {w_kg}")

    n_lb = 4.45

    planet_index = planet.index(planet)
    print(f"Weight in {planet[planet_index]} is {(w_kg * gms2[planet_index]) / n_lb} lb")
calculateWeight(myPlanet, myWeight)