from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
m= int(input('no of pages in your google form'))
n = int(input('no of responses'))
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSd5Wp6bhYxhk0_mjWbXOKY_vaTVFY7mTEaSny1vbcWXvQSmyA/viewform'
# Set up ChromeDriver and open the Google Form URL
driver = webdriver.Chrome()
driver.get(form_url)

# Wait for the page to load

time.sleep(3)
def repeatemail():
 def get_random_email(file_path):
    with open(file_path, 'r') as file:
        emails = file.readlines()  # Read all lines (emails)
    
    emails = [email.strip() for email in emails]  # Remove any extra whitespace
    if emails:
        return random.choice(emails)  # Choose a random email
    else:
        return None

# Sample file path (you can replace this with your actual file path)
 file_path = 'D:\emails.txt'

# Fetch and print a random email
 random_email = get_random_email(file_path)

 email = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
 email.send_keys(random_email)


# Find all question containers (each question is within a unique container)
questions = driver.find_elements(By.CSS_SELECTOR, 'div[role="listitem"]')  # Find all questions

# Iterate through each question
def quiestion():
 questions = driver.find_elements(By.CSS_SELECTOR, 'div[role="listitem"]')
 for question in questions:
    # Inside each question, find the available options (radio buttons)
    options = question.find_elements(By.CSS_SELECTOR, 'div[role="radio"]')

    # Randomly select one option from available options for the question
    if options:
        random_choice = random.choice(options)  # Pick one random option
        random_choice.click()

# next section
 try:
     submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
     submit_button.click()
 except:
     pass
 finally:
     next_button = driver.find_element(By.XPATH, "//span[text()='Next']")
     next_button.click()
 time.sleep(2)
def repeat():
 try:
    for _ in range(m):
     quiestion()
 except:
    pass
 finally:
    onemore_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    onemore_button.click()
    time.sleep(2)
for _ in range(n):
    repeatemail()
    repeat()



# Wait a few seconds to ensure form is submitted
time.sleep(2)

# Close the driver
#driver.quit()
