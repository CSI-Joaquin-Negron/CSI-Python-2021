weapon = 'mosin'
mosinCartridge = '7.62x54mmR'
ammunition = 'single'
velocity_ms = 30

myBuilding = 'Adventureland'
Adventureland = 70
gravity = 9.81

import math
time = math.sqrt((2 * Adventureland) / gravity)
distance = velocity_ms * time


print(f'I chose the {weapon} for this experiment. The experiment requires the cartridge, {mosinCartridge}, the ammunition, {ammunition}, and the velocity, {velocity_ms}RPM.')
print(f'After gathering this information, I next needed to choose a building. After picking {myBuilding}, i found the height {Adventureland} and measured the time   which was {time}. Finally, I needed to caculate the distance by multiplying velocity and time. The Distance of the bullet was {distance}')
