from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase
from selenium.common.exceptions import NoSuchElementException

from tracking.models import User


class LoginTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.user = User.objects.create_user(username='test_user', password='te8904!sting')

    def tearDown(self):
        self.browser.quit()

    def test_login_page(self):
        self.browser.get(self.live_server_url + '/login/')
        self.assertIn("Вход", self.browser.title)
        
        try:
            username_input = self.browser.find_element(By.NAME, 'username')
            password_input = self.browser.find_element(By.NAME, 'password')
        except NoSuchElementException as e:
            self.fail(f"Не удалось найти элемент: {e}")

        username_input.send_keys('test_user')
        password_input.send_keys('te8904!sting')
        
        self.browser.find_element(By.XPATH, '//button[text()="Войти"]').click()
        
        # Проверка заголовка страницы после входа
        self.assertIn("Tracking App", self.browser.title)
