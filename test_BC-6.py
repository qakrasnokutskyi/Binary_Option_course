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

    # Проходим онбоард экран
    go_to_training = driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="com.binaryoptions.coursesapp:id/bt_start"]')
    go_to_training.click()
    sleep(1)

    # Выбираем курс
    elementary = driver.find_element(By.XPATH,'//android.view.ViewGroup[@resource-id="com.binaryoptions.coursesapp:id/ll_beginner"]')
    elementary.click()
    sleep(1)

    # Переходим в настройки
    settings = driver.find_element(By.XPATH, '(//android.widget.ImageView[@resource-id="com.binaryoptions.coursesapp:id/navigation_bar_item_icon_view"])[4]')
    settings.click()
    sleep(1)

    # Выбираем смену языка
    change_language = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_lang_label"]')
    change_language.click()
    sleep(1)

    # Выбираем Русский язык
    russian = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_name" and @text="Русский"]')
    russian.click()
    sleep(1)

    # Переходим в настройки
    settings = driver.find_element(By.XPATH, '(//android.widget.ImageView[@resource-id="com.binaryoptions.coursesapp:id/navigation_bar_item_icon_view"])[4]')
    settings.click()
    sleep(1)

    # Выбираем смену языка
    change_language = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_lang_label"]')
    change_language.click()
    sleep(1)

    # Выбираем Португальский язык
    ukraine = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_name" and @text="Português"]')
    ukraine.click()
    sleep(1)

    # Переходим в настройки
    settings = driver.find_element(By.XPATH, '(//android.widget.ImageView[@resource-id="com.binaryoptions.coursesapp:id/navigation_bar_item_icon_view"])[4]')
    settings.click()
    sleep(1)

    # Выбираем смену языка
    change_language = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_lang_label"]')
    change_language.click()
    sleep(1)

    # Выбираем Испанский язык
    deutsch = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_name" and @text="Español"]')
    deutsch.click()
    sleep(1)

    print('Смена языка прошла успешно')