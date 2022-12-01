import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from config.definitions import ROOT_DIR
import re

driver = webdriver.Firefox()
driver.get("https://nintendo.fandom.com/wiki/List_of_Super_Smash_Bros._series_characters")

characters = []

# Find all h2 elements (Game names)
h2list = driver.find_elements(By.TAG_NAME, "h2")
for h2 in h2list:

    # Find the correct game (Super Smash Bros. Ultimate)
    if h2.get_attribute("textContent") == "Super Smash Bros. Ultimate":

        # Find all lists (ul) in the Super Smash Bros. Ultimate section
        ullist = h2.find_elements(By.XPATH,"./following::ul")
        for ul in ullist:
            oldNames = re.sub(".\(.*?\)|\*","", ul.get_attribute("textContent")).splitlines()
            
            # Names on Fandom and Liquipedia are in somes cases different, converting these cases to Liquipedia's naming
            tempNames = []
            for name in oldNames:
                tempNames.append(
                    name.replace(
                        "Pyra/Mythra", "Pyra and Mythra").replace(
                        "Solid Snake", "Snake").replace(
                        "Cloud Strife", "Cloud").replace(
                        "Pikmin and Olimar", "Olimar").replace(
                        "Wolf O'Donnell", "Wolf").replace(
                        "Kazuya Mishima", "Kazuya").replace(
                        "Richter Belmont", "Richter").replace(
                        "Fox McCloud", "Fox").replace(
                        "Samus Aran", "Samus").replace(
                        "Mega Man", "Megaman").replace(
                        "Rosalina and Luma", "Rosalina").replace(
                        "Ken Masters", "Ken").replace(
                        "Banjo and Kazooie", "Banjo & Kazooie").replace(
                        "Princess Peach", "Peach").replace(
                        "Princess Daisy", "Daisy").replace(
                        "Falco Lombardi", "Falco"
                    )
                )

            # Remove Pokémon characters since these are included in the Pokémon Trainer
            if any(pokemon in tempNames for pokemon in ["Squirtle", "Ivysaur", "Charizard"]):
                tempNames.remove("Squirtle")
                tempNames.remove("Ivysaur")
                tempNames.remove("Charizard")

            # Add the fixed names to the full character list
            characters.extend(tempNames)

            # Stop the loop (break) once we hit the "External Links" h2
            if ul.find_element(By.XPATH, "./following::*").get_attribute("textContent") == "External Links": break

# Remove duplicates from list (Result of the Pokémon Trainer having a nested list that is being counted twice)
characters = list(dict.fromkeys(characters))

# DataFrame template used in Liquidpedia scraper
data = {
    "character": characters,
    "firstPlaces": [0] * len(characters),
    "secondPlaces": [0] * len(characters),
    "thirdPlaces": [0] * len(characters),
    "forthPlaces": [0] * len(characters),
    "fifthPlaces": [0] * len(characters),
    "sixthPlaces": [0] * len(characters),
    "seventhPlaces": [0] * len(characters),
    "eightPlusPlaces": [0] * len(characters),
}

# Create the DataFrame and save it to data.csv
df = pd.DataFrame(data)
df.to_csv(os.path.join(ROOT_DIR, 'data', 'data.csv'), encoding="utf-8", index = False)
print(df)

# Close the browser
driver.close()