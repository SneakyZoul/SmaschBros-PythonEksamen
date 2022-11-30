import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
import time

tupleResults = []
driver = webdriver.Firefox()
driver.get("https://liquipedia.net/smash/Major_Tournaments/Ultimate")

# .Header-Premier - Yellow Tournaments
# .Tournament - All Tournaments
tournamentElements = driver.find_elements(By.CSS_SELECTOR, ".Tournament > b > a")

# Short list to showcase
#tournamentLinks = ["https://liquipedia.net/smash/Gimvitational", "https://liquipedia.net/smash/Ultimate_Fighting_Arena/2022", "https://liquipedia.net/smash/Let%27s_Make_Moves_Miami", "https://liquipedia.net/smash/Ludwig_Smash_Invitational/Ultimate", "https://liquipedia.net/smash/MaesumaTOP/7"]

tournamentLinks = list(map(lambda ele: ele.get_attribute("href"), tournamentElements))

# Handle loop logic
setIntervalEvent = threading.Event()
def setInterval(func,time):
    global setIntervalEvent
    while not setIntervalEvent.wait(time):
        func()

tournamentIndex = 0
def getCharacterData():
    global tournamentIndex
    global setIntervalEvent

    # If all tournaments from the tournamentLinks list has been checked
    if (tournamentIndex >= len(tournamentLinks)): 
        setIntervalEvent.set()
        print("Finished")
    else:
        print(f"Getting {tournamentIndex+1}/{len(tournamentLinks)}: {tournamentLinks[tournamentIndex]}")
        driver.get(tournamentLinks[tournamentIndex])
        
        # Technically not needed but makes it more clear what is happening
        time.sleep(1)
        dropDowns = driver.find_elements(By.CSS_SELECTOR, ".prizepooltableshow")

        # Click all table extenderes
        for dropDown in dropDowns:
            # Scroll to table drop down element using injected JS (Else clicking the element won't be possible)
            driver.execute_script("arguments[0].scrollIntoView(true);", dropDown)
            time.sleep(1)
            dropDown.click()

        # Scroll back to the first table for a better view
        driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.CSS_SELECTOR, ".prizepooltable"))

        # All prize winning tables ("Singles" and "Doubles")
        prizeTables = driver.find_elements(By.CSS_SELECTOR, ".prizepooltable")

        for table in prizeTables:
            # Begin the count from 1st place
            position = 1

            # For some seemingly unexplainable reason the "Doubles" table has a nested div element that serves no purpose as well as
            # an unneeded semicolon after the in-line css which is not present in the "Singles" table.
            # The selector looks for cells in the table with the given in-line css (which in this case is the cell with the characters).
            # First selector looks for "Singles",
            # second selector looks for "Doubles".
            # This is required due to the inconsistencies mentioned above.
            cellList = table.find_elements(By.CSS_SELECTOR, 'tbody > tr > td[style="text-align:left;height:26px"]') or table.find_elements(By.CSS_SELECTOR, 'tbody > tr > td[style="text-align:left;height:26px;"] > div.prizepooltable-player-heads')
            for cell in cellList:
                # Get images from cell
                imageList = cell.find_elements(By.CSS_SELECTOR, "span.heads-padding-right > img")
                for image in imageList:
                    # Extract "alt" attribute of image to get character name, and add it to a tuple with the placement position 
                    tupleResults.append((position, image.get_attribute("alt")))
                # Once all characters from the cell has been added to the tuple list, countinue with the next placement position
                position += 1
        tournamentIndex += 1
        print(f"Entries: {len(tupleResults)}\n{tupleResults}")
setInterval(getCharacterData, 1)

# Read data.csv with character names
characterPositionComplete = []
df = pd.read_csv('data.csv')

for character in df["character"]:
    # Create a new 2d list with first value being the character name and the remaning slots being 1-8(+) placements
    characterPositionComplete.append([character, 0, 0, 0, 0, 0, 0, 0, 0])

# Go through all results stored in the tupleResults list, find the index of the character (result[1]) in the characterPositionComplete list and update the values
for result in tupleResults:
    if any(result[1] in (match := nested_list) for nested_list in characterPositionComplete):
        
        # Index of character in characterPositionComplete
        list_index = characterPositionComplete.index(match)
        print(f"Adding Result: {result}")

        # Cap any placements above 8th place down to 8th place (Hence the column being named eightPlusPlaces)
        position = 8 if 8 < result[0] else result[0]

        # Take the current value and add 1
        characterPositionComplete[list_index][position] += 1

# Create a new DataFrame with the new values and save it to the same file
df = pd.DataFrame(characterPositionComplete, columns = [
    "character",
    "firstPlaces",
    "secondPlaces",
    "thirdPlaces",
    "forthPlaces",
    "fifthPlaces",
    "sixthPlaces",
    "seventhPlaces",
    "eightPlusPlaces"
])
 
df.to_csv("data.csv", encoding="utf-8", index = False)
print(df)

# Close the browser
driver.close()