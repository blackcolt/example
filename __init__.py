from selenium import webdriver
import time

if __name__ == '__main__':
    for i in range(1000):
        time.sleep(2)
        driver = webdriver.Opera()
        driver.get("http://google.com")
        print(1)
