import pytest
import allure
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from time import sleep, time
from appium.options.android import UiAutomator2Options


# Для автотестов использовать только телефон Motorola.
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='ZY32FX9296', # Phone Motorola
    platformVersion='11',
    appPackage='com.binaryoptions.coursesapp',
    appActivity='com.brokertest.testapp.ui.activities.ActivitySplash',
    language='en',
    locale='US'
)

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
appium_server_url = 'http://localhost:4723'


@pytest.fixture()
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield android_driver
    if android_driver:
        android_driver.quit()


def rotate_screen(driver, orientation):
    # orientation: 'LANDSCAPE' or 'PORTRAIT'
    driver.orientation = orientation

def test(driver):
    sleep(7)

    # Выбираем Англйиский язык
    english = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_name" and @text="English"]')
    english.click()
    sleep(1)

    # Нажимает кнопку "Войти/Зарегистрироваться
    login = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_enter"]')
    login.click()
    sleep(1)

    # Заполняем поле email
    email = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your email"]')
    email.send_keys('qakrasnokutskiy@gmail.com')
    sleep(1)
    print('Поле успешно заполнено')

    # Заполняем поле password
    password = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your password"]')
    password.send_keys('e251dq12r')
    sleep(1)
    print('Поле успешно заполнено')

    # Выполняем вход
    signin = driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="com.binaryoptions.coursesapp:id/bt_signIn"]')
    signin.click()
    sleep(3)

    # Переходим в настройки
    training = driver.find_element(By.XPATH,'(//android.widget.ImageView[@resource-id="com.binaryoptions.coursesapp:id/navigation_bar_item_icon_view"])[2]')
    training.click()
    sleep(1)

    # Открываем список валютных пар
    pairs = driver.find_element(By.XPATH,'(//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_currency"])[1]')
    pairs.click()
    sleep(1)

    # Переключаем на другую валютную пару
    btc = driver.find_element(By.XPATH,'(//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_currency"])[2]')
    btc.click()
    sleep(2)

    # Открываем список валютных пар
    pairs = driver.find_element(By.XPATH,'(//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_currency"])[1]')
    pairs.click()
    sleep(1)

    # Переключаем на другую валютную пару
    aud = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_currency" and @text="AUD/USD"]')
    aud.click()
    sleep(2)

    # Открываем список валютных пар
    pairs = driver.find_element(By.XPATH,'(//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_currency"])[1]')
    pairs.click()
    sleep(1)

    # Переключаем на другую валютную пару
    CHF = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_currency" and @text="CHF/USD"]')
    CHF.click()
    sleep(2)

    # Открываем список валютных пар
    pairs = driver.find_element(By.XPATH,'(//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_currency"])[1]')
    pairs.click()
    sleep(1)

    # Переключаем на другую валютную пару
    EUR = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_currency" and @text="EUR/USD"]')
    EUR.click()
    sleep(2)

    # Открываем список валютных пар
    pairs = driver.find_element(By.XPATH,'(//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_currency"])[1]')
    pairs.click()
    sleep(1)

    # Переключаем на другую валютную пару
    JPY = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_currency" and @text="JPY/USD"]')
    JPY.click()
    sleep(2)

    # Открываем список валютных пар
    pairs = driver.find_element(By.XPATH, '(//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_currency"])[1]')
    pairs.click()
    sleep(1)

    # Переключаем на другую валютную пару
    NZD = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_currency" and @text="NZD/USD"]')
    NZD.click()
    sleep(2)

    # Открываем список валютных пар
    pairs = driver.find_element(By.XPATH, '(//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_currency"])[1]')
    pairs.click()
    sleep(1)

    # Переключаем на другую валютную пару
    RUB = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_currency" and @text="RUB/USD"]')
    RUB.click()
    sleep(2)