import time
import selenium
import requests
import io
from selenium.webdriver.common.by import By
from PIL import Image
from selenium import webdriver

driver = webdriver.Firefox()

def get_images():
    global driver
    url = "https://www.ign.com/wikis/super-smash-bros-ultimate/Characters_and_Roster"
    driver.get(url)
    #Her finder vi klasse element via CSS først på ikke DLC og derefter på DLC
    thumbnails = driver.find_elements(By.CSS_SELECTOR, "img.gh-thumbnail, img.ve-align-center" )
    for img in thumbnails:
        #I dette loop køre vi igennem siden vi burger XPATH til fortælle at den skal tage elemnetet over den, altså parrentet
        #den sidste linje er til for at ligge og hente billederne ned
        name = img.find_element(By.XPATH, "..").get_attribute("title")
        download_image("smash/", img.get_attribute("src"),name+".jpg")


def download_image(download_path, url, file_name):
    # I denne funktion henter vi billedere ned ved hjælp af en URL
    image_content = requests.get(url).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file)
    #denne linje(30) brugs til at lave om på billedet i tilfældet af at det kommet tilbage som et RGBA og ikke et RGB
    im = image.convert('RGB')
    file_path = download_path + file_name

    with open(file_path, "wb") as f:
        im.save(f, "JPEG")


if __name__ =='__main__':
 get_images()
 driver.close()

