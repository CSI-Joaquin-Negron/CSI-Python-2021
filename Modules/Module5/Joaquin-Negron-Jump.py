planet = "mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"
gravity = [2.6, 1.11, 1, 2.64, 0.40, 0.94, 1.13, 0.88]
print('Calculate the legnth of your jump on all planets.')

jumplength = float(input('What is your jump lenght in meters?'))
planetgravity = input(f'select a planet from the list: {planet} ')

print(('Your jump length  on Earth is: ') + str(jumplength))
planet_index = planet.index(planetgravity)
print(f'The length of your jump in {planet[planet_index]} is {((jumplength) * (gravity[planet_index]))} meters.')