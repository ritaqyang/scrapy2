from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request
import json
import os


from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument("--no-sandbox")  
# Bypass sandbox Error: Sandbox cannot access executable. Check filesystem permissions are valid.

options.add_argument("--disable-dev-shm-usage")  # Fix for some crashes
options.add_argument("--disable-gpu")  # Might help in some environments
options.add_argument("--disable-features=NetworkService,PaintHolding,AutofillServerCommunication")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

# Ensure image directory exists
os.makedirs("./bs4/images", exist_ok=True)

json_data_list = []

def getInfo(json_data):
    elements = driver.find_elements(By.XPATH, "//tbody[@class='product']//span[contains(@class, 'pd-cateNo')]")

    for index, element in enumerate(elements, start=1):
        try:
            productCode = driver.find_element(By.XPATH, f"(//tbody[@class='product']//span[contains(@class, 'pd-cateNo')])[{index}]").text
            category = driver.find_element(By.XPATH, f"(//tbody[@class='product']//span[contains(@class, 'pd-category')])[{index}]").text
            description = driver.find_element(By.XPATH, f"(//tbody[@class='product']//span[contains(@class, 'pd-name')])[{index}]").text
            amount = driver.find_element(By.XPATH, f"(//tbody[@class='product']//span[contains(@class, 'spec-name')])[{index}]").text
            
            
            # Open and download image
            image_button = driver.find_element(By.XPATH, f"(//tbody[@class='product']//a[contains(@href, 'viewImgModal')])[{index}]")
            # image_button.click()

            # Scroll into view & use JavaScript to force click
            driver.execute_script("arguments[0].scrollIntoView(true);", image_button)
            time.sleep(1)  # Allow scroll animation
            driver.execute_script("arguments[0].click();", image_button)

            # Wait for image to appear
            image = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//img[@class='img-responsive']")))
            imageSource = image.get_attribute("src")
            if imageSource:
                urllib.request.urlretrieve(imageSource, f"./bs4/images/{productCode}.jpg")

            # Close image modal
            
            # close_button = driver.find_element(By.XPATH, "//div[@id='viewImgModal']//button[@class='close']")
            # close_button.click()
            close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='viewImgModal']//button[@class='close']")))
            driver.execute_script("arguments[0].click();", close_button)
            time.sleep(2)

            # Add to JSON list
            json_data.append({
                "productCode": productCode,
                "category": category,
                "description": description,
                "amount": amount,
                "image": f"./bs4/images/{productCode}.jpg"
            })

        except Exception as e:
            print(f"Error processing item {index}: {e}")

# Open the login page
driver.get("https://app.icatalog.cn/web/usermngt/user/tologin?account=true")

# Locate and enter login credentials
email_field = driver.find_element(By.NAME, "identity")
password_field = driver.find_element(By.NAME, "password")
email_field.send_keys("xxxxxxx@gmail.com")
password_field.send_keys("xxxxxxxxx")
password_field.send_keys(Keys.RETURN)

# Wait for successful login
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pageSize")))

# Set item count per page
item_count = driver.find_element(By.ID, "pageSize")
item_count.clear()
item_count.send_keys("100")
item_count.send_keys(Keys.TAB)
time.sleep(5)
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

# Save JSON data
with open('./bs4/results.json', 'w', encoding='utf-8') as outfile:
    json.dump(json_data_list, outfile, indent=4, ensure_ascii=False)

print("Scraping completed. Data saved to results.json")

# Close the browser
driver.quit()
