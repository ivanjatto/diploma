from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_authorization():
    driver = webdriver.Chrome()
    driver.get("https://www.kinopoisk.ru/")
    
    driver.find_element(By.XPATH, "//a[text()='Войти']").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "login")))
    
    driver.find_element(By.NAME, "login").send_keys("your_username")
    driver.find_element(By.NAME, "password").send_keys("your_password")
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='your_username']")))
    print("Authorization test passed")
    driver.quit()

test_authorization()


def test_get_movie_info():
    driver = webdriver.Chrome()
    driver.get("https://www.kinopoisk.ru/")
    
    search_box = driver.find_element(By.NAME, "kp_query")
    search_box.send_keys("Inception")
    search_box.send_keys(Keys.RETURN)
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='element most_wanted']")))
    driver.find_element(By.XPATH, "//div[@class='element most_wanted']").click()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Inception']")))
    print("Get movie info test passed")
    driver.quit()

test_get_movie_info()

def test_get_popular_movies():
    driver = webdriver.Chrome()
    driver.get("https://www.kinopoisk.ru/")
    
    driver.find_element(By.XPATH, "//a[text()='Фильмы']").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Популярные фильмы']")))
    
    popular_movies = driver.find_elements(By.XPATH, "//div[@class='movie-item']")
    assert len(popular_movies) > 0, "No popular movies found"
    print("Get popular movies test passed")
    driver.quit()

test_get_popular_movies()
