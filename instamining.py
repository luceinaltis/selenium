import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv

INSTAGRAM_ID = ""
INSTAGRAM_PASSWORD = ""

options = Options()
# options.add_argument("--headless")

browser = webdriver.Chrome(
    ChromeDriverManager().install(), options=options)

browser.get("https://www.instagram.com/accounts/login/")

WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "_2hvTZ")))

insta_id = browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input")
insta_password = browser.find_element_by_name("password")

insta_id.send_keys(INSTAGRAM_ID)
insta_password.send_keys(INSTAGRAM_PASSWORD)

insta_password.send_keys(Keys.ENTER)

WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "qNELH")))


main_hashtag = "dog"

browser.get(f"https://www.instagram.com/explore/tags/{main_hashtag}")


insta_search = browser.find_element_by_class_name("XTCLo")
insta_search.send_keys(f"#{main_hashtag}")

WebDriverWait(browser, 5).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "fuqBx")))

hashtags = browser.find_element_by_class_name(
    "fuqBx").find_elements_by_tag_name("a")

jobs = []

for hashtag in hashtags:
    name = hashtag.find_element_by_class_name("Ap253").text
    count = hashtag.find_element_by_class_name("Fy4o8").text[:-6]
    jobs.append([name, count])

file = open(f"report.csv", "w")
writer = csv.writer(file)
writer.writerow(["Hashtag", "Post Count"])

for job in jobs:
    writer.writerow([job[0], job[1]])

time.sleep(3)
browser.quit()
