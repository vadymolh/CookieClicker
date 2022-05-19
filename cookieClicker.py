from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_scores(scores):
    try:
        num = int(scores.text.split()[0])
        return num
    except ValueError:
        return 0

def main():
    browser = webdriver.Chrome()
    browser.get("https://orteil.dashnet.org/cookieclicker/")
    cookie = browser.find_element(By.ID, "bigCookie")
      
    scores = browser.find_element(By.ID, "cookies")
    while True:
        cookie.click()
        time.sleep(0.1)
        num = get_scores(scores)
        upgrades = browser.find_elements(By.CLASS_NAME, "upgrade")
        if num > 100 and len(upgrades)>1:
            upgrades[0].click()
            print("upgraded!!!")


if __name__=='__main__':
    main()