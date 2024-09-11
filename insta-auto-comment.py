from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Replace with the path to your WebDriver executable
driver_path = 'https://developer.chrome.com/docs/chromedriver/downloads#chromedriver_1140573590'

# Instagram credentials
username = 'shah_____eer'
password = 'Shaheer@1549'

# Post URL and comment text
post_url = 'https://www.instagram.com/p/your_post_id/'
comment_text = 'Your comment goes here.'

# Start a new instance of Chrome WebDriver
driver = webdriver.Chrome(driver_path)

try:
    # Open Instagram login page
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(2)  # Wait for the page to load

    # Fill in username and password
    username_input = driver.find_element_by_name('username')
    username_input.send_keys(username)
    password_input = driver.find_element_by_name('password')
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    time.sleep(3)  # Wait for login to complete

    # Navigate to the post URL
    driver.get(post_url)
    time.sleep(3)  # Wait for the post page to load

    # Find the comment input field and submit button
    comment_input = driver.find_element_by_tag_name('textarea')
    comment_input.send_keys(comment_text)
    time.sleep(1)  # Wait to fill the comment text
    comment_input.send_keys(Keys.RETURN)
    time.sleep(2)  # Wait for the comment to be posted

    print(f'Comment "{comment_text}" posted successfully.')

except Exception as e:
    print(f'Error: {e}')

finally:
    # Close the WebDriver
    driver.quit()