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
from faker import Faker
import random
import string

# Создаем экземпляр Faker для генерации данных
fake = Faker()

def generate_random_password(length=10):
    # Генерация случайного пароля с латинскими буквами и цифрами
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))


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

    sign_up = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_tab_reg"]')
    sign_up.click()
    sleep(2)

    # Генерируем случайные значения для полей
    random_name = fake.first_name()
    random_email = fake.email()

    # Заполняем поле Имя
    name = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your name"]')
    name.send_keys(random_name)
    sleep(1)

    # Заполняем поле Email
    email = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your email"]')
    email.send_keys(random_email)
    sleep(1)

    # Заполняем поле Password
    password = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your password"]')
    password.send_keys('q')
    sleep(1)

    # Заходим в новый аккаунт
    signup = driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="com.binaryoptions.coursesapp:id/bt_signIn"]')
    signup.click()
    sleep(5)

