from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger
from pages.page import Page
from pages.tensor_about import TensorAboutPage


class TensorHomePage(Page):
    '''Класс описывает домашнюю страницу "TENSOR".'''
    STRENGTH_PEOPLE = (By.XPATH, '//div[contains(@class, "tensor_ru-Index__block4-content")]/p[1]')
    TENSOR_ABOUT = (By.XPATH, '//a[@href="/about" and contains(@class, "tensor_ru-link")]')

    def check_url(self):
        '''Проверяет, что по ссылке открылась нужная страница ссылке.'''
        url = 'https://tensor.ru/'
        url_valid = WebDriverWait(self.browser, 10).until(
            EC.url_to_be(url))
        assert url_valid
        logger.info('\nУСПЕШНО. Страница "tensor.ru" по ссылке открыта.')

    def check_strength_people(self):
        '''Проверяет наличие на странице блока "Сила в людях".'''
        title = 'Сила в людях'
        strength_people = WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(self.STRENGTH_PEOPLE, title))
        assert strength_people, 'ОШИБКА. Блок "Сила в людях" НЕ НАЙДЕН.'
        logger.info('\nУСПЕШНО. Блок "Сила в людях" найден.')

    def click_about(self):
        '''Кликает по ссылке "Подробнее". Возвращает страницу "Подробнее".'''
        url = self.get_url(self.TENSOR_ABOUT)
        self.go_to_url(url)
        logger.info('\nУСПЕШНО. Клик по ссылке "Подробнее".')
        return TensorAboutPage(self.browser)
