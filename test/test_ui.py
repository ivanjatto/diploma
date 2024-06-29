from selenium import webdriver # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
import time

# Инициализация драйвера
driver = webdriver.Chrome()

# URL приложения Яндекс.Музыка
base_url = "https://music.yandex.ru/"

# Вспомогательная функция для авторизации
def login(username, password):
    driver.get(base_url)
    driver.find_element(By.XPATH, "//span[text()='Войти']").click()
    driver.find_element(By.NAME, "login").send_keys(username)
    driver.find_element(By.NAME, "passwd").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

# Тест 1: Вход и проверка главной страницы
def test_login():
    login("newivannovikov@yandex.ru", "Dimaloh1337")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Главное']")))
    print("Login test passed")

# Тест 2: Поиск и воспроизведение трека
def test_search_and_play_track():
    login("newivannovikov@yandex.ru", "Dimaloh1337")
    search_box = driver.find_element(By.XPATH, "//input[@placeholder='Исполнитель, трек, альбом или плейлист']")
    search_box.send_keys("Imagine Dragons")
    search_box.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='d-track__name']")))
    track = driver.find_element(By.XPATH, "//div[@class='d-track__name']")
    track.click()
    play_button = driver.find_element(By.XPATH, "//button[@aria-label='Воспроизвести']")
    play_button.click()
    print("Search and play track test passed")

# Тест 3: Создание и редактирование плейлиста
def test_create_and_edit_playlist():
    login("newivannovikov@yandex.ru", "Dimaloh1337")
    driver.find_element(By.XPATH, "//span[text()='Моя музыка']").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Плейлисты']")))
    driver.find_element(By.XPATH, "//span[text()='Создать плейлист']").click()
    playlist_name = "My Test Playlist"
    driver.find_element(By.XPATH, "//input[@placeholder='Название']").send_keys(playlist_name)
    driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//span[text()='{playlist_name}']")))
    driver.find_element(By.XPATH, "//span[text()='Добавить треки']").click()
    driver.find_element(By.XPATH, "//input[@placeholder='Исполнитель, трек, альбом или плейлист']").send_keys("Imagine Dragons")
    driver.find_element(By.XPATH, "//input[@placeholder='Исполнитель, трек, альбом или плейлист']").send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='d-track__name']")))
    driver.find_element(By.XPATH, "//div[@class='d-track__name']").click()
    driver.find_element(By.XPATH, "//button[text()='Добавить в плейлист']").click()
    print("Create and edit playlist test passed")

# Тест 4: Работа в оффлайн-режиме
def test_offline_mode():
    login("newivannovikov@yandex.ru", "Dimaloh1337")
    driver.find_element(By.XPATH, "//div[text()='Моя музыка']").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Оффлайн-треки']")))
    driver.find_element(By.XPATH, "//div[text()='Оффлайн-треки']").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='d-track__name']")))
    track = driver.find_element(By.XPATH, "//div[@class='d-track__name']")
    track.click()
    play_button = driver.find_element(By.XPATH, "//button[@aria-label='Воспроизвести']")
    play_button.click()
    print("Offline mode test passed")

# Тест 5: Работа радиостанций
def test_radio():
    login("newivannovikov@yandex.ru", "Dimaloh1337")
    driver.find_element(By.XPATH, "//div[text()='Радио']").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='d-radiostation__title']")))
    radio_station = driver.find_element(By.XPATH, "//div[@class='d-radiostation__title']")
    radio_station.click()
    play_button = driver.find_element(By.XPATH, "//button[@aria-label='Воспроизвести']")
    play_button.click()
    print("Radio test passed")

# Запуск тестов
test_login()
test_search_and_play_track()
test_create_and_edit_playlist()
test_offline_mode()
test_radio()

# Закрытие драйвера
driver.quit()