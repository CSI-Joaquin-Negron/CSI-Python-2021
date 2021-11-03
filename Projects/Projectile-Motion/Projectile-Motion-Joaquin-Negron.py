import math
from ExpetimentalData import ExperimentalData

# weapon = 'mosin'
# mosinCartridge = '7.62x54R LPS gzh'
# ammunition = 'single'
# velocity_ms = 865

# myBuilding = 'Adventureland'
# Adventureland = 70
# gravity = 9.81

# convert your variables into parameters

def projectile_function(experimentalData:ExperimentalData):
    time = math.sqrt((2 * Adventureland) / gravity)
    # distance = (experimentalData[velocity_ms] * time)

    print(f'I chose the {weapon} for this experiment. The experiment requires the cartridge, {mosinCartridge}, the ammunition, {ammunition}, and the velocity, {velocity_ms}RPM.')
    print(f'After gathering this information, I next needed to choose a building. After picking {myBuilding}, i found the height {Adventureland} and measured the time   which was {time}. Finally, I needed to caculate the distance by multiplying velocity and time. The Distance of the bullet was {distance}')

# convert your script parameter into a json object.

# experimentalData = {

# "weapon": 'mosin',
# "mosinCartridge": '7.62x54R LPS gzh',
# 'ammunition': 'single',
# 'velocity_ms': 865,

# 'myBuilding': 'Adventureland',
# 'Adventureland': 70,
# 'gravity': 9.81
    
# }

experimentalData = ExperimentalData('mosin', '7.62x54R LPS gzh', 'single', 865, 'Adventureland', 70, 9.81)

projectile_function(experimentalData)
