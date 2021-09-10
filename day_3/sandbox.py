import requests
import json

response = requests.get("https://rickandmortyapi.com/api/character")
clean_data = json.loads(response.text)

print()
for key in clean_data.keys():
    if key == 'results':
        for result_dict in clean_data[key]:
            #print(type(result_dict)) #dict
            print(f"Name: {result_dict['name']}")
            print(f"\tSpecies: {result_dict['species']}")
            print(f"\tGender: {result_dict['gender']}")
            print(f"\tLocation: {result_dict['location']['name']}\n")


#
# output/results
#
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
