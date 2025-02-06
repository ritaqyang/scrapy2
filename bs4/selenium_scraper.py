from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib
import json

# Set up the Selenium driver (use Chrome, Firefox, etc.)
driver = webdriver.Chrome()

json_data_list = []

def getInfo(json_data):
    #Find all elements matching the XPath
    elements = driver.find_elements(By.XPATH, "//tbody[@class='product']//span[contains(@class, 'pd-cateNo')]")

    for element in range(1, len(elements)+1):
        # get text
        productCode = driver.find_element(By.XPATH, "(//tbody[@class='product']//span[contains(@class, 'pd-cateNo')])[" + str(element) + "]").text
        category = driver.find_element(By.XPATH, "(//tbody[@class='product']//span[contains(@class, 'pd-category')])[" + str(element) + "]").text
        description = driver.find_element(By.XPATH, "(//tbody[@class='product']//span[contains(@class, 'pd-name')])[" + str(element) + "]").text
        amount = driver.find_element(By.XPATH, "(//tbody[@class='product']//span[contains(@class, 'spec-name')])[" + str(element) + "]").text
        
        # open image
        driver.find_element(By.XPATH, "(//tbody[@class='product']//a[contains(@href, 'viewImgModal')])[" + str(element) + "]").click()
        time.sleep(10)

        # download image
        image = driver.find_element(By.XPATH, "//img[@class='img-responsive']")
        imageSource = image.get_attribute("src")
        urllib.request.urlretrieve(imageSource, "./bs4/images/" + productCode + ".jpg")
        time.sleep(5)

        # close image
        driver.find_element(By.XPATH, "//div[@id='viewImgModal']//button[@class='close']").click()
        time.sleep(2)

        # Add content to json
        item = {
            "productCode": productCode,
            "category": category,
            "description": description,
            "amount": amount,
            "image": "./bs4/images/" + productCode + ".jpg"
        }

        json_data.append(item)



# Open the login page
login_url = "https://app.icatalog.cn/web/usermngt/user/tologin?account=true"
driver.get(login_url)

# Wait for the page to load
driver.implicitly_wait(10)

# Locate the username and password fields
email_field = driver.find_element(By.NAME, "identity")  # Adjust if necessary
password_field = driver.find_element(By.NAME, "password")  # Adjust if necessary

# Enter login credentials
email_field.send_keys("xxxxxxxxx@gmail.com")
password_field.send_keys("xxxxxxxx")

# Submit the form (press Enter or find a login button)
password_field.send_keys(Keys.RETURN)

# Allow time for the login process
time.sleep(10)

item_count = driver.find_element(By.XPATH, "//input[@id='pageSize']") 
item_count.send_keys("100")
item_count.send_keys(Keys.TAB)

time.sleep(10)

count = 1
item_count = driver.find_element(By.XPATH, "//input[@id='pageSize']") 

while True:
    try:
        driver.find_element(By.XPATH, "//ul[@class='pagination']/li[contains(., '" + str(count) + "')]/a") 
        driver.find_element(By.XPATH, "//ul[@class='pagination']/li[contains(., '" + str(count) + "')]/a").click()
        time.sleep(10)
        getInfo(json_data_list)
        count += 1
    except:
        break

# Save the json data to a file
print(json_data_list)
with open('./bs4/results.json', 'w') as outfile:
    json.dump(json_data_list, outfile, indent=4)

# Close the browser
driver.quit()
