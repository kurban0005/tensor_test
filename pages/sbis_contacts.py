from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger
from pages.page import Page
from pages.tensor_home import TensorHomePage


class SbisContactsPage(Page):
    '''Класс описывает страницу "КОНТАКТЫ" сайта SBIS.'''
    TENSOR_BANNER = (By.XPATH, "//a[contains(@class, 'sbisru-Contacts__logo-tensor mb-12')]")
    CURRENT_REGION = (By.XPATH, "//span[contains(@class, 'sbis_ru-Region-Chooser__text')]")
    NEW_REGION = (By.XPATH, '//span[text()="41 Камчатский край"]')
    PARTNERS = (By.NAME, 'itemsContainer')
    PARTNERS_CITY = (By.CLASS_NAME, 'sbisru-Contacts-List__city')

    def click_tensor_banner(self):
        """Кликает по баннеру "Тензор" и возвращает экземпляр страницы TensorHomePage."""
        url = self.get_url(self.TENSOR_BANNER)
        self.go_to_url(url)
        logger.info('\nУСПЕШНО. Клик по баннеру "Тензор".')
        return TensorHomePage(self.browser)

    def check_current_region(self):
        """Проверяет, что текущий регион соответствует ожидаемому значению."""
        current_region = 'Республика Башкортостан'

        current_region_correct = WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(self.CURRENT_REGION, current_region))
        assert current_region_correct, 'ОШИБКА. Текущий регион определён НЕВЕРНО'
        logger.info('\nУСПЕШНО. Текущий регион определён верно.')

    def chek_current_partners(self):
        """Проверяет, что список партнеров текущего региона отображается."""
        partners = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.PARTNERS_CITY))
        assert partners, 'ОШИБКА. Список партнеров НЕ ОТОБРАЖЁН.'
        logger.info('\nУСПЕШНО. Список партнеров текущего региона отображен.')

    def change_region(self):
        """Изменяет текущий регион на новый."""
        current_region = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.CURRENT_REGION))
        current_region.click()
        new_region = current_region = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.NEW_REGION))
        new_region.click()
        logger.info('\nУСПЕШНО. Текущий регион изменён на новый.')

    def check_new_region(self):
        """Проверяет, что новый регион соответствует ожидаемому значению."""
        new_region = 'Камчатский край'
        new_region_correct = WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(self.CURRENT_REGION, new_region)
        )
        assert new_region_correct, 'ОШИБКА. Новый регион определён НЕВЕРНО'
        logger.info('\nУСПЕШНО. Новый регион определён верно.')

    def check_new_partners(self):
        """Проверяет, что список партнеров изменен на новый."""
        partners_city = 'Петропавловск-Камчатский'
        partners_city_correct = WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(self.PARTNERS_CITY, partners_city)
        )
        assert partners_city_correct, 'ОШИБКА. Список партнеров НЕ ИЗМЕНЁН'
        logger.info('\nУСПЕШНО. Список партнеров изменён.')

    def check_region_url(self):
        """Проверяет, что URL содержит ожидаемый регион."""
        region_url = '41-kamchatskij-kraj'
        correct_url = WebDriverWait(self.browser, 10).until(
            EC.url_contains(region_url))
        assert correct_url, 'ОШИБКА. Регион в строке url НЕ ИЗМЕНЁН'
        logger.info('\nУСПЕШНО. Регион в строке URL изменён.')

    def check_region_title(self):
        """Проверяет, что заголовок страницы соответствует ожидаемому значению."""
        region_title = 'Камчатский край'
        correct_title = WebDriverWait(self.browser, 10).until(
            EC.title_contains(region_title))
        assert correct_title, 'ОШИБКА. Регион в названии заголовка НЕ ИЗМЕНЁН'
        logger.info('\nУСПЕШНО. Регион в названии заголовка изменён.')
