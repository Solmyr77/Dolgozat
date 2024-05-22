# imports
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# set driver
browser = webdriver.Firefox()
browser.get('http://localhost:5500')

# functions
def test1():
    elemOne = browser.find_element(By.ID, 'element-one')

    ActionChains(browser).double_click(elemOne).perform()

    browser.save_screenshot("testOne.png")

    assert "animation" in elemOne.get_attribute("class")

def test2():
    elemTwo = browser.find_element(By.ID, 'element-two')

    ActionChains(browser).move_to_element(elemTwo).perform()

    browser.save_screenshot("testTwo.png")

    assert "box-shadow: 5px 10px" in elemTwo.get_attribute("style")

def test3():
    elemThree = browser.find_element(By.ID, 'element-three')

    elemThree.click()

    browser.save_screenshot("testThree.png")

    assert "visibility: hidden" in elemThree.get_attribute("style")

def test4():
    elemFour = browser.find_element(By.ID, 'element-four')

    elemFour.click()

    browser.save_screenshot("testFour.png")

    assert "background-color: green" in elemFour.get_attribute("style")

def test5():
    elemFourHover = browser.find_element(By.ID, 'element-four')

    ActionChains(browser).move_to_element(elemFourHover).perform()

    time.sleep(1)

    browser.save_screenshot("testFive.png")

# test1: dupla kattintás után szerepel-e az "animation" class
test1()
time.sleep(1)
# ha rámegy az egér, utána létezik-e box-shadow
test2()
time.sleep(1)
# kattintás után eltűnik-e
test3()
time.sleep(1)
# kattintás után a háttere zöld lesz-e
test4()
time.sleep(1)
# ha a 4. elemre egeret viszünk, hogy néz ki? (screenshot kell csak!)
test5()

browser.quit()

