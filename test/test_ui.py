from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_authorization():
    driver = webdriver.Chrome()
    driver.get("https://www.kinopoisk.ru/")

    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'login')]"))).click()
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "login")))

        driver.find_element(By.NAME, "login").send_keys("newivannovikov@yandex.ru")
        driver.find_element(By.NAME, "password").send_keys("Dimaloh1337")
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[text()='newivannovikov@yandex.ru']")))
        print("Authorization test passed")
    except Exception as e:
        print(f"Authorization test failed: {e}")
    finally:
        driver.quit()



def test_get_movie_info():
    driver = webdriver.Chrome()
    driver.get("https://www.kinopoisk.ru/")

    try:
        search_box = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "kp_query")))
        search_box.send_keys("Inception")
        search_box.send_keys(Keys.RETURN) # type: ignore

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='element most_wanted']")))
        driver.find_element(By.XPATH, "//div[@class='element most_wanted']").click()

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Inception')]")))
        print("Get movie info test passed")
    except Exception as e:
        print(f"Get movie info test failed: {e}")
    finally:
        driver.quit()



def test_get_popular_movies():
    driver = webdriver.Chrome()
    driver.get("https://www.kinopoisk.ru/")

    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/popular/')]"))).click()
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Популярные фильмы']")))

        popular_movies = driver.find_elements(By.XPATH, "//div[@class='movie-item']")
        assert len(popular_movies) > 0, "No popular movies found"
        print("Get popular movies test passed")
    except Exception as e:
        print(f"Get popular movies test failed: {e}")
    finally:
        driver.quit()



