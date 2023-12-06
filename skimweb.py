from selenium import webdriver # A library to automate web browser interaction from Python
from selenium.webdriver.common.by import By # give access to search for things using specific parameters like xpath, css_selector, id, name, class_name, tag_name, link_text and partial_link_text
from webdriver_manager.chrome import ChromeDriverManager # A library to automate maintenance and updates for Chrome

def get_driver():
# Selenium requires a driver to interface with the chosen browser.
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars") # infobars can confuse cursor positioning
    options.add_argument("--disable-extensions") # extensions can also confuse cursor positioning
    options.add_argument("start-maximized") # open Browser in maximized mode
    options.add_argument("disable-dev-shm-usage") # overcome limited resource problems on linux
    options.add_argument("no-sandbox") # Bypass OS security model
    options.add_argument("disable-blink-features=AutomationControlled") # disable automation control warning. Script more likely to work
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) # disable automation control warning. Script more likely to work
    options.add_experimental_option('useAutomationExtension', False) # disable automation control warning. Script more likely to work

    service = webdriver.ChromeService(ChromeDriverManager().install()) # update ChromeDriverManager to latest version
    # The executable_path parameter is set automatically by ChromeDriverManager
    driver = webdriver.Chrome(service=service, options=options) # notice we called 'service=service' to update automatically
    driver.get("https://automated.pythonanywhere.com") # Open's a Test Website to ensure the code works. Change to your desired website.

    return driver

def main():
    driver = get_driver()
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[1]") # Open the website and find the element you want. Then use copy -> xpath and past in the Quotes.
    return element.text

print(main())
