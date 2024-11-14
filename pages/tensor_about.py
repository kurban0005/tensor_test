from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger
from pages.page import Page


class TensorAboutPage(Page):
    '''Класс описывает страницу "ПОДРОБНЕЕ" сайта TENSOR.'''
    WORKING_PHOTOS = (By.XPATH, '//img[contains(@class, "tensor_ru-About__block3-image")]')

    def check_url(self):
        '''Проверяет, что по ссылке открылась нужная страница ссылке.'''
        url = 'https://tensor.ru/about'
        url_valid = WebDriverWait(self.browser, 10).until(
            EC.url_to_be(url))
        assert url_valid, 'ОШИБКА. Страница "tensor.ru/about" по ссылке НЕ ОТКРЫТА.'
        logger.info('\nУСПЕШНО. Страница "tensor.ru/about" по ссылке открыта.')

    def check_size_photo(self):
        '''Проверяем размер фото в разделе "Работаем".'''
        photos = self.find_all(self.WORKING_PHOTOS)
        width_list = []
        height_list = []
        for photo in photos:
            width_list.append(photo.get_attribute('width'))
            height_list.append(photo.get_attribute('height'))
        width_set = set(width_list)
        height_set = set(height_list)
        same_width = len(width_set) == 1
        same_height = len(height_set) == 1
        assert same_width and same_height, 'ОШИБКА. Фото в разделе "Работаем" имею разынй размер.'
        logger.info('\nУСПЕШНО. Все фото в разделе "Работаем" ОДНОГО РАЗМЕРА.')
