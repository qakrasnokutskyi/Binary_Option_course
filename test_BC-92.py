import pytest
import allure
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from time import sleep, time
from appium.options.android import UiAutomator2Options

# Для автотестов использовать только телефон Motorola.
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='ZY32FX9296',  # Phone Motorola
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

    # Переходим на экран настройки
    settings = driver.find_element(By.XPATH,'(//android.widget.ImageView[@resource-id="com.binaryoptions.coursesapp:id/navigation_bar_item_icon_view"])[4]')
    settings.click()
    sleep(1)

    course = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_course_title"]')
    course.click()
    sleep(2)

    advanced = driver.find_element(By.XPATH,'//android.view.ViewGroup[@resource-id="com.binaryoptions.coursesapp:id/ll_pro"]')
    advanced.click()
    sleep(2)

    # Выполняем свайп экрана вверх до указанного элемента
    while True:
        try:
            # Поиск элемента по тексту
            target_element = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Lesson 10")')
            print("Элемент найден!")
            break  # Если элемент найден, выходим из цикла
        except:
            # Выполняем свайп вверх
            size = driver.get_window_size()
            start_x = size['width'] / 2
            start_y = size['height'] * 0.8
            end_y = size['height'] * 0.2

            driver.swipe(start_x, start_y, start_x, end_y, 800)
            print("Свайп вверх выполнен.")
            sleep(1)


    # Проходим 10 урок
    lesson_10 = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_name" and @text="Lesson 10"]')
    lesson_10.click()
    sleep(2)

    complete = driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="com.binaryoptions.coursesapp:id/bt_complete"]')
    complete.click()
    sleep(2)

    question1 = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_answer" and @text="Trend continuation pattern"]')
    question1.click()
    sleep(2)

    question2 = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_answer" and @text="Bearish & bullish"]')
    question2.click()
    sleep(2)

    question3 = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_answer" and @text="Continuation of the downtrend"]')
    question3.click()
    sleep(2)

    question4 = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_answer" and @text="Long term upward or downward trend"]')
    question4.click()
    sleep(2)

    question5 = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_answer" and @text="A pattern formed during a vertical ascend of an asset price"]')
    question5.click()
    sleep(2)

    next = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.binaryoptions.coursesapp:id/tv_next"]')
    next.click()
    sleep(2)

    PUT = driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="com.binaryoptions.coursesapp:id/bt_green"]')
    PUT.click()
    sleep(2)

    clear = driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="com.binaryoptions.coursesapp:id/bt_ok"]')
    clear.click()
    sleep(2)

    continue_lesson = driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="com.binaryoptions.coursesapp:id/bt_start"]')
    continue_lesson.click()
    sleep(2)