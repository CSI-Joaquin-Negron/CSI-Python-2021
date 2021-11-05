import math
from ExperimentalData import ExperimentalData
from pathlib import Path
import json
import os
# weapon = 'mosin'
# mosinCartridge = '7.62x54R LPS gzh'
# ammunition = 'single'
# velocity_ms = 865

# myBuilding = 'Adventureland'
# height = 70
# gravity = 9.81

# convert your variables into parameters

def projectile_function(experimentalData:ExperimentalData):
    time = math.sqrt((2 * experimentalData.height) / experimentalData.gravity)
    distance = (experimentalData.velocity_ms * time)

    print(f'I chose the {experimentalData.weapon} for this experiment. The experiment requires the cartridge, {experimentalData.mosinCartridge}, the ammunition, {experimentalData.ammunition}, and the velocity, {experimentalData.velocity_ms}RPM.')
    print(f'After gathering this information, I next needed to choose a building. After picking {experimentalData.myBuilding}, i found the height {experimentalData.height} and measured the time   which was {time}. Finally, I needed to caculate the distance by multiplying velocity and time. The Distance of the bullet was {distance}')

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

myDataSet = [
    ExperimentalData('mosin', '7.62x54R LPS gzh', 'single', 865, 'Adventureland', 70, 9.81),
    ExperimentalData('mosin', '7.62x54R LPS gzh', 'single', 865, 'World Trade Center', 415, 9.81),
    ExperimentalData('mosin', '7.62x54R LPS gzh', 'single', 865, 'Panorama', 258, 9.81),
    ExperimentalData('mosin', '7.62x54R LPS gzh', 'single', 865, 'Aura', 271, 9.81),
    ExperimentalData('mosin', '7.62x54R LPS gzh', 'single', 865, 'Shanghai Tower', 632, 9.81)
    ]

for data in myDataSet:
    print('\n---------------------------------------------------------\n')
    projectile_function(data)

myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'Projectile-Motion.json')

with open(myOutputFilePath, 'w') as outfile:
    json.dump([data.__dict__ for data in myDataSet], outfile)

# projectile_function(experimentalData)
