'''
This program will provide recipe ideas for vegetarians based on
pulling this info from https://www.delish.com/cooking/g1486/healthy-vegetarian-dinner-recipes/

'''
import random
import time
import asyncio
from selenium import webdriver
from datetime import datetime

# path of the chromedriver
PATH = r"/applications/chromedriver"
driver = webdriver.Chrome(PATH)  # to open the browser

# url of recipes to choose from
url = 'https://www.delish.com/cooking/g1486/healthy-vegetarian-dinner-recipes/?slide=1'

# to open the url in the browser
driver.get(url)


all_recipes = []
def getAllRecipes():

    for x in range(1, 55):
        recipe_path = ''
        # Exception handling to handle unexpected changes
        # in the structure of the website
        try:

            recipe_path = f'//*[@id="slide-{x}"]/div[3]/div[1]'
            # to get that element
            recipe = driver.find_element_by_xpath(recipe_path)
            all_recipes.append(recipe.text)
        except:
            continue
        #print(all_recipes)

def getWeeklyRecipes():
    weekly_recipes = []
    for y in range(0, 7):
        weekly_recipes.append(all_recipes[random.randint(1,20)])
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        print(f"On {days[y]} let's eat: ")

        print(weekly_recipes[y])
        print()


now = datetime.now()

# this is just to get the time at the time of web scraping
current_time = now.strftime("%H:%M:%S")
print(f'At time : {current_time} ')

getAllRecipes()
getWeeklyRecipes()