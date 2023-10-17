import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestMain:
    @pytest.mark.parametrize('url', [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
        # добавьте больше ссылок, если нужно
    ])
    def test_correct_answer(self, url):
        with webdriver.Chrome() as browser:
            wait = WebDriverWait(browser, 10)
            browser.get(url)

            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a#ember33")))
            browser.execute_script("arguments[0].click();", element)
            time.sleep(1)  # добавьте задержку после клика
            # Авторизация
            login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='login']")))
            password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='password']")))
            login.send_keys("example@gmail.com")
            password.send_keys("122557")
            button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sign-form__btn")))
            browser.execute_script("arguments[0].click();", button)

            # Ввод ответа
            answer = math.log(int(time.time()))
            textarea = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea")))
            textarea.send_keys(str(answer))

            # Отправка ответа
            button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
            browser.execute_script("arguments[0].click();", button)

            # Проверка фидбека
            feedback = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
            assert feedback.text == "Correct!"

        if __name__ == "__main__":
            pytest.main()
