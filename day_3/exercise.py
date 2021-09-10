import requests
import json
import pprint


response = requests.get("https://rickandmortyapi.com/api/character")
# print(response)

# json.loads() - takes text string and converts it to dict (clean_data)
clean_data = json.loads(response.text)
# print(response.text)
# print(type(response.text))

# print type of clean_data to confirm it is dict
#print(type(clean_data))

# test print and get "info"
#print(clean_data)
############## Rick & Morty API exercise ################
#pprint.pprint(clean_data)
## go through results for each row in an excel spreadsheet
## grab the name, species, gender, location name

print()
for key in clean_data.keys():
    if key == 'results':
        for result_dict in clean_data[key]:
            #print(type(result_dict)) #dict
            print(f"Name: {result_dict['name']}")
            print(f"Species: {result_dict['species']}")
            print(f"Gender: {result_dict['gender']}")
            print(f"Location: {result_dict['location']['name']}\n")    

## [results list]

# darren@iMac itp_week_3 % /usr/local/bin/python3 /Users/darren/Desktop/itp_week_3/day_3/exercise.py

# Name: Rick Sanchez
# Species: Human
# Gender: Male
# Location: Earth (Replacement Dimension)

# Name: Morty Smith
# Species: Human
# Gender: Male
# Location: Earth (Replacement Dimension)

# Name: Summer Smith
# Species: Human
# Gender: Female
# Location: Earth (Replacement Dimension)

# Name: Beth Smith
# Species: Human
# Gender: Female
# Location: Earth (Replacement Dimension)

# Name: Jerry Smith
# Species: Human
# Gender: Male
# Location: Earth (Replacement Dimension)

# Name: Abadango Cluster Princess
# Species: Alien
# Gender: Female
# Location: Abadango

# Name: Abradolf Lincler
# Species: Human
# Gender: Male
# Location: Testicle Monster Dimension

# Name: Adjudicator Rick
# Species: Human
# Gender: Male
# Location: Citadel of Ricks

# Name: Agency Director
# Species: Human
# Gender: Male
# Location: Earth (Replacement Dimension)

# Name: Alan Rails
# Species: Human
# Gender: Male
# Location: Worldender's lair

# Name: Albert Einstein
# Species: Human
# Gender: Male
# Location: Earth (Replacement Dimension)

# Name: Alexander
# Species: Human
# Gender: Male
# Location: Anatomy Park

# Name: Alien Googah
# Species: Alien
# Gender: unknown
# Location: Earth (Replacement Dimension)

# Name: Alien Morty
# Species: Alien
# Gender: Male
# Location: Citadel of Ricks

# Name: Alien Rick
# Species: Alien
# Gender: Male
# Location: Citadel of Ricks

# Name: Amish Cyborg
# Species: Alien
# Gender: Male
# Location: Earth (Replacement Dimension)

# Name: Annie
# Species: Human
# Gender: Female
# Location: Anatomy Park

# Name: Antenna Morty
# Species: Human
# Gender: Male
# Location: Citadel of Ricks

# Name: Antenna Rick
# Species: Human
# Gender: Male
# Location: unknown

# Name: Ants in my Eyes Johnson
# Species: Human
# Gender: Male
# Location: Interdimensional Cable





