### ***You have to download required chrome webdriver with correct version of your chrome.***

from selenium import webdriver

browser = webdriver.Chrome(
    executable_path="you chrome driver path")   # Enter you chrome driver path here for ex. D:\Directory\chromedriver

browser.get("https://cuchd.blackboard.com/")
browser.implicitly_wait(3)

ok_button = browser.find_element_by_id("agree_button")
ok_button.click()

username_black = browser.find_element_by_id("user_id")
username_black.send_keys("UID")   # Enter your UID for one time.

pswd_black = browser.find_element_by_name("password")
pswd_black.send_keys("password")    # Enter your account password.

login_button = browser.find_element_by_id("entry-login")

login_button.click()
print("\n\nLogged in...")
