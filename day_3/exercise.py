import os
import requests
import json
import openpyxl


response = requests.get("https://rickandmortyapi.com/api/character")
# print(response)

# json.loads() - takes text string and converts it to dict (clean_data)
clean_data = json.loads(response.text)

# grab only results list from clean_data dict
# 'results' is list of character dicts
results = clean_data['results']

############## Rick & Morty API exercise ################
# go through results for each row in an excel spreadsheet
# grab the name, species, gender, location name

# create workbook
wb = openpyxl.Workbook()

# name of output file/workbook
output_file = 'RickNMortyOutput.xlsx'

# grab sheet; randomly grabbing active sheet
sheet = wb.active

# create headers/column titles on 1st row of sheet
sheet['A1'] = "Name"
sheet['B1'] = "Species"
sheet['C1'] = "Gender"
sheet['D1'] = "Location"


################## FOR SELF ONLY ######################
# clear terminal for better readabilty of output/errors
# when running script
os.system('clear')  
#######################################################

# initialize counter to 2 (2nd row; "1st row" after header row)
# loop through each Rick and Morty character, populating 1 row
# per show character.
# increment 'counter' as each character is processed.
counter = 2
for character in results:
    sheet['A' + str(counter)] = character['name']
    sheet['B' + str(counter)] = character['species']
    sheet['C' + str(counter)] = character['gender']
    sheet['D' + str(counter)] = character['location']['name']
    counter += 1

# delete existing output file before save
# try-except in case file doesn't exist.
try:
    os.remove('./' + output_file)
except:
    pass

# save workbook to file.
wb.save(filename = './' + output_file)
        