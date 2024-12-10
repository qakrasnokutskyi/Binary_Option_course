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

from time import sleep, time
from appium.options.android import UiAutomator2Options

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

    # Выполнение свайпа влево между разделами онбоард страницы
    # Получаем координаты элементов для свайпа
    element = driver.find_element(By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout')
    size = driver.get_window_size()

    # Начальные и конечные координаты для свайпа влево
    start_x = size['width'] * 0.8  # Начальная точка (80% от ширины экрана)
    end_x = size['width'] * 0.2  # Конечная точка (20% от ширины экрана)
    start_y = size['height'] / 2  # Центр экрана по высоте

    # Свайп с использованием метода swipe() (если используется более старая версия Appium)
    driver.swipe(start_x, start_y, end_x, start_y, 1000)  # Время свайпа - 1000 миллисекунд
    sleep(1)

    # Получаем координаты элементов для свайпа
    element = driver.find_element(By.XPATH,
                                  '//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout')
    size = driver.get_window_size()

    # Начальные и конечные координаты для свайпа влево
    start_x = size['width'] * 0.8  # Начальная точка (80% от ширины экрана)
    end_x = size['width'] * 0.2  # Конечная точка (20% от ширины экрана)
    start_y = size['height'] / 2  # Центр экрана по высоте

    # Свайп с использованием метода swipe() (если используется более старая версия Appium)
    driver.swipe(start_x, start_y, end_x, start_y, 1000)  # Время свайпа - 1000 миллисекунд
    sleep(1)

    # Получаем координаты элементов для свайпа
    element = driver.find_element(By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout')
    size = driver.get_window_size()

    # Начальные и конечные координаты для свайпа влево
    start_x = size['width'] * 0.8  # Начальная точка (80% от ширины экрана)
    end_x = size['width'] * 0.2  # Конечная точка (20% от ширины экрана)
    start_y = size['height'] / 2  # Центр экрана по высоте

    # Свайп с использованием метода swipe() (если используется более старая версия Appium)
    driver.swipe(start_x, start_y, end_x, start_y, 1000)  # Время свайпа - 1000 миллисекунд
    sleep(1)

    # Получаем координаты элементов для свайпа
    element = driver.find_element(By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout')
    size = driver.get_window_size()

    # Начальные и конечные координаты для свайпа влево
    start_x = size['width'] * 0.2  # Начальная точка (80% от ширины экрана)
    end_x = size['width'] * 0.8  # Конечная точка (20% от ширины экрана)
    start_y = size['height'] / 2  # Центр экрана по высоте

    # Свайп с использованием метода swipe() (если используется более старая версия Appium)
    driver.swipe(start_x, start_y, end_x, start_y, 1000)  # Время свайпа - 1000 миллисекунд
    sleep(1)

    # Получаем координаты элементов для свайпа
    element = driver.find_element(By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout')
    size = driver.get_window_size()

    # Начальные и конечные координаты для свайпа влево
    start_x = size['width'] * 0.2  # Начальная точка (80% от ширины экрана)
    end_x = size['width'] * 0.8  # Конечная точка (20% от ширины экрана)
    start_y = size['height'] / 2  # Центр экрана по высоте

    # Свайп с использованием метода swipe() (если используется более старая версия Appium)
    driver.swipe(start_x, start_y, end_x, start_y, 1000)  # Время свайпа - 1000 миллисекунд
    sleep(1)

    # Получаем координаты элементов для свайпа
    element = driver.find_element(By.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout')
    size = driver.get_window_size()

    # Начальные и конечные координаты для свайпа влево
    start_x = size['width'] * 0.2  # Начальная точка (80% от ширины экрана)
    end_x = size['width'] * 0.8  # Конечная точка (20% от ширины экрана)
    start_y = size['height'] / 2  # Центр экрана по высоте

    # Свайп с использованием метода swipe() (если используется более старая версия Appium)
    driver.swipe(start_x, start_y, end_x, start_y, 1000)  # Время свайпа - 1000 миллисекунд
    sleep(1)

    # Проходим онбоард экран
    go_to_training = driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="com.binaryoptions.coursesapp:id/bt_start"]')
    go_to_training.click()
    sleep(1)

    elementary = driver.find_element(By.XPATH,'//android.view.ViewGroup[@resource-id="com.binaryoptions.coursesapp:id/ll_beginner"]')
    elementary.click()
    sleep(2)

    settings = driver.find_element(By.XPATH,'(//android.widget.ImageView[@resource-id="com.binaryoptions.coursesapp:id/navigation_bar_item_icon_view"])[4]')
    settings.click()
    sleep(2)

    sign_in = driver.find_element(By.XPATH,'//android.widget.Button[@resource-id="com.binaryoptions.coursesapp:id/bt_sign_in"]')
    sign_in.click()
    sleep(2)

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