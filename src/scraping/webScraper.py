import os
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from config.definitions import ROOT_DIR

driver = webdriver.Firefox()
driver.get("https://nintendo.fandom.com/wiki/List_of_Super_Smash_Bros._series_characters")


def some():
    characters = []

    # Find all h2 elements (Game names)
    h2list = driver.find_elements(By.TAG_NAME, "h2")
    for h2 in h2list:

        # Find the correct game (Super Smash Bros. Ultimate)
        if h2.get_attribute("textContent") == "Super Smash Bros. Ultimate":

            # Find all lists (ul) in the Super Smash Bros. Ultimate section
            ul_list = h2.find_elements(By.XPATH, "./following::ul")
            for ul in ul_list:
                characters.extend(re.sub(".\(.*?\)|\*", "", ul.get_attribute("textContent")).splitlines())

                # Stop the loop (break) once we hit the "External Links" h2
                if ul.find_element(By.XPATH, "./following::*").get_attribute("textContent") == "External Links": break

    # Remove duplicates from list (Result of the Pokémon Trainer having a nested list that is being counted twice)
    characters = list(dict.fromkeys(characters))

    data = {
        "character": characters,
        "tournamentsPlayed": ["1"] * len(characters),
        "tournamentsWon": ["2"] * len(characters),
        "tournamentsLost": ["3"] * len(characters)
    }

    df = pd.DataFrame(data)
    print(df)

    df.to_csv(os.path.join(ROOT_DIR, 'data', 'data.csv'), encoding="utf-8", index=False)
    driver.close()


if __name__ == '__main__':
    some()
