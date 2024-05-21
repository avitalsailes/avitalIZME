from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get('https://manage.izme.cloud')
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()


#The registration page
#1.1 Functionality - Create a user
#1.2 Functionality - Register with mane that contains letters and numbers
#1.3 Functionality - Register with walla mail
#1.6 BV – Register with password that contains 8 letters
userlist = [["avitalot1","avitalsa90@gmail.com","0509442257","Avitalot@1"],["avitalot2","avitalsa90@gmail.com","0509442257","Avitalot@2"],["avitalot3","avital202020@walla.com","0509442257","Avitalot@3"],["avital88","avitalsa90@gmail.com","0509442257","Avitalot@1"]]

@pytest.mark.parametrize("anything", userlist)
def test_1(setup, anything):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="/sign-up"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(anything[0])
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="email"]').send_keys(anything[1])
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="phone"]').send_keys(anything[2])
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(anything[3])
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="confirmPassword"]').send_keys(anything[3])
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/form/div[7]/span[1]/input').click()
    time.sleep(1)
    driver.find_element(By.XPATH ,'//*[@id="root"]/div[3]/div/div[1]/form/div[8]/button').click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div[2]/input[1]').is_displayed()
    time.sleep(1)

#1.4 Functionality – press on – “sign in” button at the bottom of the window
def test_4(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="/sign-up"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//a[@href="/sign-in"]').click()
    time.sleep(1)

#1.5 Functionality – change the registration page to Hebrew
def test_5(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="/sign-up"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//button[@class="language-button "]').click()
    time.sleep(1)

#1.7 EH – Register without insert any password
def test_7(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="/sign-up"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("avitalxx2")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="email"]').send_keys("avitalsa90@gamil.com")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="phone"]').send_keys("0509442257")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="confirmPassword"]').send_keys("Avital9!")
    time.sleep(1)
    driver.find_element(By.XPATH ,'//*[@id="root"]/div[3]/div/div[1]/form/div[8]/button').click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div[2]/input[1]').is_displayed()
    time.sleep(1)

#1.8 EH – Register without insert any mail
def test_8(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="/sign-up"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("avitalxx")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="phone"]').send_keys("0509442257")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("Avital9!")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="confirmPassword"]').send_keys("Avital9!")
    time.sleep(1)
    driver.find_element(By.XPATH ,'//*[@id="root"]/div[3]/div/div[1]/form/div[8]/button').click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div[2]/input[1]').is_displayed()
    time.sleep(1)

#1.9 EH – Register with a different password on Confirm password
def test_9(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="/sign-up"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("avitalxx2")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="email"]').send_keys("avitalsa90@gamil.com")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="phone"]').send_keys("0509442257")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("Avital9!")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="confirmPassword"]').send_keys("a")
    time.sleep(1)
    driver.find_element(By.XPATH ,'//*[@id="root"]/div[3]/div/div[1]/form/div[8]/button').click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div[2]/input[1]').is_displayed()
    time.sleep(1)

#1.10 EH – Register with mane in Hebrew
def test_10(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="/sign-up"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("אביטל")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="email"]').send_keys("avitalsa90@gamil.com")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="phone"]').send_keys("0509442257")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("Avital9!")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="confirmPassword"]').send_keys("Avital9!")
    time.sleep(1)
    driver.find_element(By.XPATH ,'//*[@id="root"]/div[3]/div/div[1]/form/div[8]/button').click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div[2]/input[1]').is_displayed()
    time.sleep(1)

#1.11 EH – Register with mane that already exists
def test_11(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="/sign-up"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("avital")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="email"]').send_keys("avitalsa90@gamil.com")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="phone"]').send_keys("0509442257")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("Avital9!")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="confirmPassword"]').send_keys("Avital9!")
    time.sleep(1)
    driver.find_element(By.XPATH ,'//*[@id="root"]/div[3]/div/div[1]/form/div[8]/button').click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div[2]/input[1]').is_displayed()
    time.sleep(1)

#1.12 EH – Register with mail that not exists
def test_12(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="/sign-up"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("avitalxx2")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="email"]').send_keys("avitalsa90.com")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="phone"]').send_keys("0509442257")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("Avital9!")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="confirmPassword"]').send_keys("Avital9!")
    time.sleep(1)
    driver.find_element(By.XPATH ,'//*[@id="root"]/div[3]/div/div[1]/form/div[8]/button').click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div[2]/input[1]').is_displayed()
    time.sleep(1)

#1.13 EH – Register with password that contains 7 letters
def test_13(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="/sign-up"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("avitalxx2")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="email"]').send_keys("avitalsa90@gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="phone"]').send_keys("0509442257")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("Avita7!")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="confirmPassword"]').send_keys("Avita7!")
    time.sleep(1)
    driver.find_element(By.XPATH ,'//*[@id="root"]/div[3]/div/div[1]/form/div[8]/button').click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div[2]/input[1]').is_displayed()
    time.sleep(1)

#1.14 EH – Register with password that contains only small letters
def test_14(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="/sign-up"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("avitalxx2")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="email"]').send_keys("avitalsa90@gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="phone"]').send_keys("0509442257")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("avital9!")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="confirmPassword"]').send_keys("avital9!")
    time.sleep(1)
    driver.find_element(By.XPATH ,'//*[@id="root"]/div[3]/div/div[1]/form/div[8]/button').click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div[2]/input[1]').is_displayed()
    time.sleep(1)

#1.15 EH – Register with password that contains only big letters
def test_15(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="/sign-up"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("avitalxx2")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="email"]').send_keys("avitalsa90@gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="phone"]').send_keys("0509442257")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("AVITAL9!")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="confirmPassword"]').send_keys("AVITAL9!")
    time.sleep(1)
    driver.find_element(By.XPATH ,'//*[@id="root"]/div[3]/div/div[1]/form/div[8]/button').click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div[2]/input[1]').is_displayed()
    time.sleep(1)

#1.16 EH – Register with password that not contains numbers
def test_16(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="/sign-up"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("avitalxx2")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="email"]').send_keys("avitalsa90@gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="phone"]').send_keys("0509442257")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("Avital!")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="confirmPassword"]').send_keys("Avital!")
    time.sleep(1)
    driver.find_element(By.XPATH ,'//*[@id="root"]/div[3]/div/div[1]/form/div[8]/button').click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div[2]/input[1]').is_displayed()
    time.sleep(1)

#1.17 EH – Register with password that not contains special characters
def test_17(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="/sign-up"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("avitalxx2")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="email"]').send_keys("avitalsa90@gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="phone"]').send_keys("0509442257")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("Avital9")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="confirmPassword"]').send_keys("Avital9")
    time.sleep(1)
    driver.find_element(By.XPATH ,'//*[@id="root"]/div[3]/div/div[1]/form/div[8]/button').click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div[2]/input[1]').is_displayed()
    time.sleep(1)

#1.18 EH – Register without confirming the "terms of use"
def test_18(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="/sign-up"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("avitalxx2")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="email"]').send_keys("avitalsa90@gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="phone"]').send_keys("0509442257")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("Avital9!")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="confirmPassword"]').send_keys("Avital9!")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/form/div[7]/span[1]/input').click()
    time.sleep(1)
    driver.find_element(By.XPATH ,'//*[@id="root"]/div[3]/div/div[1]/form/div[8]/button').click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div[2]/input[1]').is_displayed()
    time.sleep(1)

#1.19 EH – Register without insert any name
def test_19(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="/sign-up"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="email"]').send_keys("avitalsa90@gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="phone"]').send_keys("0509442257")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("Avital9!")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="confirmPassword"]').send_keys("Avital9!")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/form/div[7]/span[1]/input').click()
    time.sleep(1)
    driver.find_element(By.XPATH ,'//*[@id="root"]/div[3]/div/div[1]/form/div[8]/button').click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div[2]/input[1]').is_displayed()
    time.sleep(1)

#Login Page
#2.1 Functionality – login
def test_login_1(setup):
    driver = setup
    driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Avital")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("AVItal123@")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/form/div[4]/button').click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, '//span[@class="head-bold-text no-wrap"]').is_displayed()
    time.sleep(1)

#2.3 Functionality – press on "Click to resend" button in forget password page
def test_login_3(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="/forgot-password"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Avital")
    time.sleep(1)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//button[@class="resend-btn"]').click()
    time.sleep(1)

#2.4 Functionality – return to the Login Page from the forget password page
def test_login_4(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="/forgot-password"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//button[@class="back-to-login-btn flex-row-reverse"]').click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, '//div[@class="welcome-title-wrapper"]').is_displayed()
    time.sleep(1)

#2.5 EH – insert a different username than the one you registered with
def test_login_5(setup):
    driver = setup
    driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("a")
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("AVItal123@")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/form/div[4]/button').click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, '//span[@class="head-bold-text no-wrap"]').is_displayed()
    time.sleep(1)

#def Login_Page_6(setup):
def test_login_6(setup):
        driver = setup
        driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Avital")
        time.sleep(1)
        driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("a")
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/form/div[4]/button').click()
        time.sleep(1)
        assert driver.find_element(By.XPATH, '//span[@class="head-bold-text no-wrap"]').is_displayed()
        time.sleep(1)

#.7 EH – insert a different code on forget password page
def test_login_7(setup):
    driver = setup
    driver.find_element(By.XPATH, '//a[@href="/forgot-password"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Avital")
    time.sleep(1)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div[2]/input[1]').send_keys("0")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div[2]/input[2]').send_keys("0")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div[2]/input[3]').send_keys("0")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div[2]/input[4]').send_keys("0")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div[2]/input[5]').send_keys("0")
    time.sleep(1)

