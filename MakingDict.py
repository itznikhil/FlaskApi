import pandas as pd
import csv

df = pd.read_csv('FilteredStars.csv')

Name = df['Name']
Mass = df['Mass']
Distance = df['Distance']
Radius = df['Radius']
Gravity = df['Gravity']

data = []
for i,name in enumerate(Name):
    star = {
        'Name':Name[i],
        'Mass':Mass[i],
        'Radius':Radius[i],
        'Distance':Distance[i],
        'Gravity':Gravity[i]
    }
    data.append(star)

print(data)